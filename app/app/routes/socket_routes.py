from flask_socketio import emit
from app import socketio

# Instancia de SocketIO (se conectará con la aplicación Flask)

# Evento que se dispara cuando un cliente se conecta
@socketio.on('connect')
def handle_connect():
    print("Client connected -------------------------------")
    emit('response', {'message': 'Connected to the server!------------------------'})

# Evento para manejar mensajes entrantes del cliente
@socketio.on('message')
def handle_message(data):
    print(f"Received message: {data}")
    # Enviar respuesta de vuelta al cliente
    emit('response', {'message': f"Server received: {data}"})

# Evento que se dispara cuando un cliente se desconecta
@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")
