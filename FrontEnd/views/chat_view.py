import flet as ft
import threading
import websocket
import json

class ChatView:
    def __init__(self):
        self.ws = None  # WebSocket client
        self.stop_thread = False  # Controla el estado del hilo de escucha

    def build(self):
        # Campo para mostrar mensajes
        self.chat_messages = ft.Text(value="Chat Messages:\n", width=400, height=300)
        # Campo para ingresar texto
        self.message_input = ft.TextField(label="Your Message")
        # Botón para enviar mensaje
        send_button = ft.TextButton("Send", on_click=self.send_message)
        
        # Iniciar el WebSocket en un hilo separado para no bloquear la interfaz
        websocket_thread = threading.Thread(target=self.start_websocket, daemon=True)
        websocket_thread.start()
        
        # Layout de la vista
        return ft.Column(controls=[self.chat_messages, self.message_input, send_button])

    def start_websocket(self):
        """Inicia el WebSocket y mantiene la conexión para recibir mensajes."""
        try:
            # Conectar al WebSocket
            self.ws = websocket.WebSocketApp(
                url="ws://app:5000/socket.io/",  # Cambiar con la URL correcta del WebSocket
                on_message=self.on_message_received,
                on_open=self.on_connect,
                on_close=self.on_disconnect,
                on_error=self.on_error,
                header={"Origin": "http://frontend:8008"}
            )
            self.ws.run_forever()
        except Exception as e:
            print(f"WebSocket error: {e}")

    def on_connect(self, ws):
        """Maneja el evento de conexión al WebSocket."""
        print("Connected to the server!")
        self.chat_messages.value += "\nConnected to the server!"
        self.chat_messages.update()
        
    def on_disconnect(self, ws, close_status_code, close_msg):
        """Maneja el evento de desconexión del WebSocket."""
        print("Disconnected from the server!")
        self.chat_messages.value += "\nDisconnected from the server!"
        self.chat_messages.update()

    def on_message_received(self, ws, message):
        """Maneja los mensajes recibidos desde el servidor."""
        try:
            data = json.loads(message)
            self.chat_messages.value += f"\n{data['message']}"
            self.chat_messages.update()
        except json.JSONDecodeError:
            print(f"Error parsing message: {message}")

    def send_message(self, e):
        """Enviar mensaje al servidor WebSocket."""
        if self.ws:
            message = self.message_input.value
            self.ws.send(json.dumps({'message': message}))
            # Actualizar la vista con el mensaje enviado
            self.chat_messages.value += f"\nYou: {message}"
            self.chat_messages.update()
            # Limpiar el campo de texto
            self.message_input.value = ""
            self.message_input.update()

    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")

    def __del__(self):
        """Detener el WebSocket cuando se destruye la instancia."""
        self.stop_thread = True
        if self.ws:
            self.ws.close()
