import flet as ft
import httpx

class UserApp(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.msg_input = ft.TextField(label="Nombre de usuario", autofocus=True)
        self.pass_input = ft.TextField(label="Contraseña", password=True)
        self.status = ft.Text("Estado: Desconectado", style="headlineMedium")
        self.create_button = ft.ElevatedButton("Crear Usuario", on_click=self.create_user)
        self.list_button = ft.ElevatedButton("Listar Usuarios", on_click=self.list_users)
        self.users_list = ft.ListView()  # Para mostrar la lista de usuarios

        # Agregar controles a la columna
        #self.page.add(self.status, self.msg_input, self.pass_input, self.create_button, self.list_button, self.users_list)

         
    async def create_user(self, e):
        print("Entra a crear usuario")

        name_user = self.msg_input.value
        password_user = self.pass_input.value
        
        # Verifica que se hayan ingresado valores
        if not name_user or not password_user:
            self.status.value = "Por favor, ingresa un nombre de usuario y una contraseña."
            self.page.update()
            return
        
        # Prepara los datos para enviar
        user_data = {
            "nameUser": name_user,
            "passwordUser": password_user
        }

        async with httpx.AsyncClient() as client:
            response = await client.post("http://app:80/Usersockets/add", json=user_data)

        if response.status_code == 201:
            self.status.value = "Usuario creado exitosamente."
        else:
            self.status.value = f"Error al crear usuario: {response.text}"

        self.page.update()

    async def list_users(self, e):
        print("Entra a listar")
        async with httpx.AsyncClient() as client:
            response = await client.get("http://app:80/Usersockets/index")
        print(f"Entra a listar 1 {response.status_code}")

        if response.status_code == 200:
            users = response.json()
            self.users_list.controls.clear()  # Limpiar la lista actual antes de agregar nuevos usuarios
            for user in users:
                print(user)
                # Asegúrate de que el subtítulo sea un objeto ft.Text
                self.users_list.controls.append(ft.ListTile(
                    title=ft.Text(user['name']), 
                    subtitle=ft.Text(f"ID: {user['id']}")
                ))

            self.users_list.update()  # Actualiza la lista de usuarios
            self.status.value = "Usuarios listados exitosamente."
        else:
            self.status.value = f"Error al listar usuarios: {response.text}"

        self.page.update()



    def build(self):
        # Crea una columna para los controles de entrada
        input_column = ft.Column([
            self.status,
            self.msg_input,
            self.pass_input,
            ft.Row([self.create_button, self.list_button])
        ])
        
        # Crea una columna para la lista de usuarios
        list_column = ft.Column([
            ft.Text("Lista de Usuarios:", style="headlineMedium"),
            self.users_list
        ])

        # Devuelve una columna que contiene ambas columnas
        return ft.Column([
            input_column,
            list_column
        ])
