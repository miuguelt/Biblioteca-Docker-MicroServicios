import flet as ft
from app3 import MyApp2
from app4 import MyApp as MyApp4
from app5 import UserApp as MyApp5

def main(page):
    # Crear una instancia de MyApp y pasar 'page' como argumento
    app2 = MyApp2(page)
    app3 = MyApp4(page)
    app5 = MyApp5(page)

    # Crear ListView para permitir el desplazamiento
    list_view2 = ft.ListView([app2], expand=True)
    list_view3 = ft.ListView([app3], expand=True)
    list_view5 = ft.ListView([app5], expand=True)

    # Agregar los controles desplazables a la página
    page.add(app2)
    page.add(app3)
    page.add(list_view5)

if __name__ == "__main__":
    ft.app(target=main, port=8008, host="0.0.0.0")
