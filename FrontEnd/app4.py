import flet as ft
import uuid
from socket_client import create_new_client as conexion

class MyApp(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.page = page
        print("entra a MyApp4")
        self.msg_input = ft.TextField(label="Mensaje", autofocus=True)
        self.status = ft.Text("Estado: Desconectado")
        self.connect_button = ft.ElevatedButton("Conectar", on_click=self.connect)
        self.send_button = ft.ElevatedButton("Enviar", on_click=self.send_message, disabled=True)
        self.disconnect_button = ft.ElevatedButton("Desconectar", on_click=self.disconnect, disabled=True)
   
    # def build(self):
    #     return ft.Column([
    #         self.status,
    #         self.msg_input,
    #         self.connect_button,
    #         self.send_button,
    #         self.disconnect_button
    # ])
        
    async def connect(self, e):
        print("entra a Conectar 1")
        self.status.value = "Estado: Conectando..."
        self.page.update()  # Update UI after connection
        # Call page.update() for UI changes
        self.send_button.disabled = False
        self.disconnect_button.disabled = False
        self.connect_button.disabled = True
        self.sio, self.desconectar, self.send_message = await conexion(str(uuid.uuid4()),"http://app:80") # Change the URL if necessary
        self.status.value = "Estado: Conectado"
        self.page.update()  # Update UI after connection
        print("entra a conect")
        # Captura el mensaje del servidor cuando se recibe un `response`
        mensaje_recibido = await self.sio.get_response_message()
        print(f"Mensaje recibido desde el servidor: {mensaje_recibido}")


    async def send_message(self, e):
        msg = self.msg_input.value
        print("entra a enviar mensaje")
        await self.send_message(msg)
        self.msg_input.value = ""
        self.msg_input.focus()
        self.page.update()  # Update UI after sending message

    async def disconnect(self, e):
        self.status.value = "Estado: Desconectado"
        self.page.update()  # Update UI after disconnect

        print("entra a disconect")
        self.send_button.disabled = True
        self.disconnect_button.disabled = True
        self.connect_button.disabled = False
        self.page.update()  # Update UI after disconnect
        await self.desconectar()  # Llama a la función de desconexión

    def build(self):
         return ft.Column([
             self.status,
             self.msg_input,
             ft.Row([self.connect_button, self.send_button, self.disconnect_button])
         ])