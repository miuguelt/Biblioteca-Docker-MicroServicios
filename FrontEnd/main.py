import socketio
import asyncio

# Crear una instancia del cliente de Socket.IO
sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("Conexión exitosa al servidor Socket.IO")

@sio.event
async def message(data):
    print(f"Mensaje del servidor: {data['message']}")

@sio.event
async def disconnect():
    print("Desconectado del servidor")

async def connect_to_websocket():
    # Cambia esto si tu servidor está en otro puerto o dirección
    await sio.connect("http://app:80")  
    await sio.send('Hello, Server!')  # Enviar un mensaje al servidor

    # Mantener la conexión abierta
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(connect_to_websocket())