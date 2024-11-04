from app import create_app, db, socketio

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    print(f"SocketIO is running on: ws://{app.config['SERVER_NAME']}/socket.io/")
    socketio.run(app, host="0.0.0.0", port=80, debug=True, allow_unsafe_werkzeug=True)
    print(f"SocketIO is running on: ws://{app.config['SERVER_NAME']}/socket.io/")
    #app.run(debug=True, host='0.0.0.0', port=5000)