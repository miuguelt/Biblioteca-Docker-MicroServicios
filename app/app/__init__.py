from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
import os
from flask_cors import CORS

async_mode = None
socketio = SocketIO()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    from app.routes import socket_routes

    app = Flask(__name__)    
    app.config.from_object('config.Config')
    CORS(app)
    socketio.init_app(app, cors_allowed_origins="*")
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(idUser):
        from .models.users import User
        return User.query.get(int(idUser))

    # Register blueprints
    from app.routes import (
        auth, book_routes, author_routes, users_route, 
        loans_routes, cloans_routes, computers_routes, 
        room_routes, users_route_socket, socket_routes
    )
    app.register_blueprint(auth.bp)
    app.register_blueprint(book_routes.bp)
    app.register_blueprint(author_routes.bp)
    app.register_blueprint(users_route.bp)
    app.register_blueprint(loans_routes.bp)
    app.register_blueprint(cloans_routes.bp)
    app.register_blueprint(computers_routes.bp)
    app.register_blueprint(room_routes.bp)
    app.register_blueprint(users_route_socket.bp)

    @app.errorhandler(Exception)
    def handle_error(e):
        print(f"An error occurred: {str(e)}")
        return {"error": str(e)}, 500

    return app