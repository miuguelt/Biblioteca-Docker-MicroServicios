import flet as ft

class MyApp2(ft.Column):
    def __init__(self, page):  # Agregar 'page' como argumento
        super().__init__()
        self.page = page  # Almacenar la página para referencia futura
        self.counter = 0
        self.text = ft.Text(f"Contador: {self.counter}")
        self.button = ft.ElevatedButton("Incrementar", on_click=self.increment)

    def increment(self, e):
        self.counter += 1
        self.text.value = f"Contador: {self.counter}"
        self.update()  # Actualizar la interfaz

    def build(self):
        return ft.Column([
            self.text,
            self.button
        ])