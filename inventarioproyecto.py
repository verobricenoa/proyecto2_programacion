import json
import os

def cargar_inventario():
    try:
        with open('_inventario.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_inventario(inventario):
    with open('_inventario.json', 'w') as f:
        json.dump(inventario, f, indent=4)

def mostrar_inventario(inventario):
    for i, producto in enumerate(inventario, 1):
        print("Nombre: ",producto['nombre']," PRECIO: ", producto['precio'], " CANTIDAD: ",producto['cantidad'])

def mostrar_producto_especifico(inventario):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    nombre=nombre.lower()
    for producto in inventario:
        if producto['nombre'] == nombre:
            print(f"NOMBRE: {producto['nombre']}")
            print(f"PRECIO: {producto['precio']}")
            print(f"CANTIDAD: {producto['cantidad']}")
            return
    print("Producto no encontrado.")

def actualizar_producto(inventario):
    mostrar_inventario(inventario)
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    for i, producto in enumerate(inventario):
        if producto['nombre'] == nombre:
            producto["precio"] = float(input("Nuevo precio: "))
            producto["cantidad"] = int(input("Nueva cantidad: "))
            print("Producto actualizado.")
            return
    print("Producto no encontrado.")

def eliminar_producto(inventario):
    mostrar_inventario(inventario)
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for i, producto in enumerate(inventario):
        if producto['nombre'] == nombre:
            inventario.pop(i)
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")

def agregar_producto(inventario, producto):
    inventario.append(producto)

def validar_producto(inventario, atributo, valor):
    return any(item[atributo] == valor for item in inventario)

# main
inventario = cargar_inventario()

while True:

    print("GESTIÓN DE INVENTARIO")
    print("1. Crear un producto")
    print("2. Mostrar todos los productos")
    print("3. Mostrar información de un producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        producto = {}
        while True:
            codigo = input("Introduzca el código del producto: ")
            if len(codigo) == 4:
                if not validar_producto(inventario, "codigo", codigo.upper()):
                    break
                else:
                    print("El código del producto ya está registrado.")
            else:
                print("El código del producto debe ser de 4 caracteres.")
        nombre = input("Ingrese el nombre del producto: ") 
        while True:
            precio = input("Introduzca el precio del producto: ")
            if precio.replace(".", "").isnumeric():
                if 0.01 <= float(precio) <= 100 and round(float(precio),2)==float(precio):
                   break  
            print("Se debe introducir un precio válido.")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad, "codigo": codigo.upper()}
         
        agregar_producto(inventario, producto)
        guardar_inventario(inventario)
    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":   
        mostrar_producto_especifico(inventario) 
    elif opcion == "4":
        actualizar_producto(inventario) 
    elif opcion == "5": 
        eliminar_producto(inventario)
    elif opcion == "6": 
        break
        os.system('cls')
    else: 
        print("OPCIÓN INVÁLIDA")