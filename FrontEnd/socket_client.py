import socketio
import asyncio

# Crear una instancia del cliente de Socket.IO
clients = {}
# Variable para almacenar la tarea creada
#socket_wait_task = None

async def create_new_client(client_id, url):
    sio = socketio.AsyncClient()
    
    # Evento que recibe la respuesta desde el servidor
    @sio.event
    async def response(data):
        print(f"Mensaje recibido del servidor: {data['message']}")
        
    async def get_response_message():
        # Esperar el mensaje emitido por el servidor con el nombre 'response'
        return await sio.call('response')  # Asegúrate que esto coincide con el evento que envía el servidor

    # Eventos de conexión, mensaje y desconexión
    @sio.event
    async def connect():
        print(f"Conexión exitosa al servidor Socket.IO cliente {client_id}")

    @sio.event
    async def message(data):
        print(f"Mensaje de {client_id}: {data}")

    @sio.event
    async def disconnect():
        print(f"Desconectado del servidor {client_id} ----------")
        await sio.disconnect()

    # Función para enviar un mensaje
    async def send_message(msg):
        msg = str(msg + "   enviado por"+client_id)
        await sio.send(msg)
    
    clients[client_id] = {
        "client": sio,
        "task": asyncio.create_task(sio.wait())  # Crear una tarea para esperar los eventos
    }
    # Conectar al servidor
    await sio.connect(url)
    await sio.send(f"Hola, desde {client_id}!") 
    # Almacenar el cliente y la tarea asociada
    return sio, disconnect, send_message

