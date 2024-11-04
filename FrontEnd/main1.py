import flet as ft
import requests

# Función que se encarga de obtener y actualizar la tabla con datos nuevos
def cargar_datos(table, page):
    try:
        response = requests.get("http://app:5000/User/js")  # Cambia a la URL correcta de tu API
        users_data = response.json()  # Asume que la respuesta es un JSON válido

        # Limpiar filas anteriores
        table.rows.clear()

        # Llenar la tabla con los nuevos datos obtenidos
        for user in users_data:
            table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(user["idUser"]))),
                        ft.DataCell(ft.Text(user["nameUser"])),
                    ]
                )
            )

        page.update()  # Actualizar la página para reflejar los nuevos datos
    except Exception as e:
        page.add(ft.Text(f"Error al obtener datos: {e}", color=ft.colors.RED))
        page.update()

def main(page: ft.Page):
    page.title = "Vista de Usuarios en Flet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 20

    # Crear la cabecera de la tabla
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
        ],
        rows=[]
    )

    # Llenar la tabla con datos iniciales al cargar la página
    cargar_datos(table, page)

    # Agregar la tabla a la página
    page.add(table)

# Ejecutar la aplicación
ft.app(target=main)