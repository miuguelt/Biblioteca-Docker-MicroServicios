# frontend/main.py

import flet as ft
from views.chat_view import ChatView

def main(page: ft.Page):
    # Crear una instancia de la vista del chat
    chat_view = ChatView()
    # Configurar el título de la página
    page.title = "Chat WebSocket App"
    # Agregar la vista del chat a la página
    page.add(chat_view.build())

# Ejecutar la aplicación Flet
if __name__ == "__main__":
    # Modo WebSocket de Flet
    ft.app(target=main, port=8008)
