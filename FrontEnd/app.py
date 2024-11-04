# app.py
import flet as ft
from socket_client import connect_to_websocket, send_message, disconnect_socket

class MyApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.msg_input = ft.TextField(label="Mensaje", autofocus=True)
        self.status = ft.Text("Estado: Desconectado")
        self.connect_button = ft.ElevatedButton("Conectar", on_click=self.connect)
        self.send_button = ft.ElevatedButton("Enviar", on_click=self.send_message, disabled=True)
        self.disconnect_button = ft.ElevatedButton("Desconectar", on_click=self.disconnect, disabled=True)

    async def connect(self, e):
        self.status.text = "Estado: Conectando..."
        self.update()
        
        await connect_to_websocket("http://app:80")  # Cambia la URL si es necesario

        self.status.text = "Estado: Conectado"
        self.send_button.disabled = False
        self.disconnect_button.disabled = False
        self.connect_button.disabled = True
        self.update()

    async def send_message(self, e):
        msg = self.msg_input.value
        await send_message(msg)
        self.msg_input.value = ""
        self.msg_input.focus()
        self.update()

    async def disconnect(self, e):
        await disconnect_socket()
        self.status.text = "Estado: Desconectado"
        self.send_button.disabled = True
        self.disconnect_button.disabled = True
        self.connect_button.disabled = False
        self.update()

    def build(self):
        return ft.Column([
            self.status,
            self.msg_input,
            ft.Row([self.connect_button, self.send_button, self.disconnect_button])
        ])

def main(page: ft.Page):
    page.title = "Cliente Socket.IO en Flet"
    page.add(MyApp())

if __name__ == "__main__":
    ft.app(target=main)
