"""Calculo de costo total"""
import json
import time


def load_json(file_path):
    """Cargar json"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error en archivo {file_path}: {e}")
        return None


def calcular_costo(catalogo, ventas):
    """Costo total"""
    costo_total = 0

    for sale in ventas:

        product_name = sale['Product']
        quantity = sale['Quantity']

        # Buscar por nombre
        info_producto = next(
            (p for p in catalogo if p['title'] == product_name), None
            )

        if info_producto:
            precio_unitario = info_producto['price']
            costo_total += quantity * precio_unitario

    return costo_total


def main():

    """Inicio de Programa"""
    start_time = time.time()

    productos_catalogo_file = input(
        "Escriba la ruta del archivo de productos:  \n")
    detalle_ventas = input(
        "Escriba la ruta del archivp de ventas:  \n")

    productos_catalogo = load_json(productos_catalogo_file)
    detalle_ventas = load_json(detalle_ventas)

    costo_total = calcular_costo(productos_catalogo, detalle_ventas)

    with open('SalesResults.txt', 'w', encoding='utf-8') as result_file:
        result_file.write(f"Total Cost: ${costo_total:.2f}\n")
        end_time = time.time()
        elapsed_time = end_time - start_time
        result_file.write(f"Time Elapsed: {elapsed_time:.4f} seconds")

    print(f"Costo Total: ${costo_total:.2f}")
    print(f"Time Elapsed: {elapsed_time:.4f} seconds")


main()
