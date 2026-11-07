def inicializar_inventario():
    inventario = [
        {"id": 201, "articulo": "Tostado de jamón y queso", "valor": 2000},
        {"id": 202, "articulo": "Jugo natural de naranja", "valor": 1200},
        {"id": 203, "articulo": "Alfajor de maicena", "valor": 800}
    ]
    return inventario

def registrar_nuevo_item(inventario):
    print(" CARGA DE NUEVO PRODUCTO AL CATÁLOGO ")
    nuevo_id = int(input("Ingrese el código del nuevo producto: "))
    
    existe = False
    for prod in inventario:
        if prod["id"] == nuevo_id:
            existe = True
            break
            
    if existe:
        print(f"Error: El código {nuevo_id} ya se encuentra registrado en el sistema.")
    else:
        nuevo_nombre = input("Ingrese el nombre del artículo: ")
        nuevo_precio = float(input("Ingrese el precio: "))
        
        item_nuevo = {"id": nuevo_id, "articulo": nuevo_nombre, "valor": nuevo_precio}
        inventario.append(item_nuevo)
        print("¡Producto incorporado al catálogo exitosamente!")

catalogo_actual = inicializar_inventario()
registrar_nuevo_item(catalogo_actual)