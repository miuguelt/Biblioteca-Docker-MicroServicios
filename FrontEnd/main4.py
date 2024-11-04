import flet as ft
import threading
import asyncio
import websockets

# URL del WebSocket (asegúrate de cambiar esto por la URL correcta)

BASE_URL = "http://app:5000"
SOCKET_URL = "ws://localhost:5000/socket.io/?EIO=4&transport=websocket"

# Función que manejará la conexión WebSocket
async def websocket_handler(page: ft.Page):
    async with websockets.connect(
            SOCKET_URL, extra_headers={"Sec-WebSocket-Protocol": "protocol_name"}) as websocket:
        
        # Muestra que la conexión está abierta
        await page.add_async(ft.Text("WebSocket Connected"))

        try:
            # Escuchar mensajes desde el WebSocket
            async for message in websocket:
                # Actualizar la UI con el mensaje recibido
                await page.add_async(ft.Text(f"Received: {message}"))
        except websockets.ConnectionClosed:
            # Manejar la desconexión
            await page.add_async(ft.Text("WebSocket Disconnected"))

# Función para iniciar la conexión WebSocket en un hilo separado
def start_websocket(page: ft.Page):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(websocket_handler(page))

# Función principal de Flet
def main(page: ft.Page):
    page.title = "Flet WebSocket Example"
    page.update()

    # Iniciar el WebSocket en un hilo separado
    websocket_thread = threading.Thread(target=start_websocket, args=(page,))
    websocket_thread.start()

    # Botón de prueba para la interfaz
    page.add(ft.ElevatedButton("Test Button"))

# Ejecutar la app de Flet
ft.app(target=main)
