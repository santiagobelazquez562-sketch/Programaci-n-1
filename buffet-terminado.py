import json

def cargarProductos():
    archivo = open("productos.json", "a+")
    archivo.seek(0)
    contenido = archivo.read()
    archivo.close()
    if contenido == "":

        catalogo_inicial = [
            {"codigo": 101, "nombre": "Café con leche", "precio": 1500},
            {"codigo": 102, "nombre": "Medialuna", "precio": 700},
            {"codigo": 103, "nombre": "Sándwich de miga", "precio": 1800},
            {"codigo": 104, "nombre": "Agua mineral 500 ml", "precio": 1000},
            {"codigo": 105, "nombre": "Empanada", "precio": 1200},
            {"codigo": 106, "nombre": "Chipá (100 g)", "precio": 1300}
        ]
        guardarProductos(catalogo_inicial)
        return catalogo_inicial
    return json.loads(contenido)

def guardarProductos(productos):
    archivo = open("productos.json", "w")
    json.dump(productos, archivo)
    archivo.close()

def cargarVentas():
    archivo = open("ventas.json", "a+")
    archivo.seek(0)
    contenido = archivo.read()
    archivo.close()
    if contenido == "":
        return []
    return json.loads(contenido)

def guardarVentas(ventas):
    archivo = open("ventas.json", "w")
    json.dump(ventas, archivo)
    archivo.close()

def mostrarCatalogo(productos):
    print("CATÁLOGO DE PRODUCTOS")
    for p in productos:
        print("Código:", p["codigo"], "|", p["nombre"], "| Precio: $", p["precio"])

def registrarVenta(ventas, productos):
    print("REGISTRAR VENTA")
    mostrarCatalogo(productos)
    dia = int(input("Ingrese el día (1 = lunes ... 5 = viernes): "))[cite: 1]
    if dia < 1 or dia > 5:
        print("Día no válido. Debe ser entre 1 y 5.")
        return
    codigo = int(input("Ingrese el código del producto: "))
    
    encontrado = False
    for p in productos:
        if p["codigo"] == codigo:
            encontrado = True
            break
            
    if encontrado == False:
        print("El código de producto no existe.")
        return
        
    cantidad = int(input("Ingrese la cantidad vendida: "))
    
    venta = {"dia": dia, "codigo": codigo, "cantidad": cantidad}
    ventas.append(venta)
    guardarVentas(ventas)
    print("Venta registrada y guardada con éxito.")

def verInformes(productos, ventas):
    if len(ventas) == 0:
        print("No hay ventas registradas todavía.")
        return
        
    print("\n--- INFORMES DE LA SEMANA ---")
    
    
    print("\n1. Unidades vendidas por producto[cite: 1]:")
    unidades_productos = {}
    for p in productos:
        unidades_productos[p["codigo"]] = 0
        
    for v in ventas:
        cod = v["codigo"]
        if cod in unidades_productos:
            unidades_productos[cod] += v["cantidad"]
            
    for p in productos:
        print("-", p["nombre"], ":", unidades_productos[p["codigo"]], "unidades")

    # 2. Recaudación de cada día
    print("\n2. Recaudación de cada día[cite: 1]:")
    recaudacion_dias = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    dias_nombres = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes"}[cite: 1, 2]
    
    for v in ventas:
        dia = v["dia"]
        precio_prod = 0
        for p in productos:
            if p["codigo"] == v["codigo"]:
                precio_prod = p["precio"]
                break
        recaudacion_dias[dia] += v["cantidad"] * precio_prod
        
    for d in range(1, 6):
        print("-", dias_nombres[d], ": $", recaudacion_dias[d])

    max_unidades = -1
    prod_estrella = ""
    for p in productos:
        tot = unidades_productos[p["codigo"]]
        if tot > max_unidades:
            max_unidades = tot
            prod_estrella = p["nombre"]
            
    max_recaudacion = -1
    dia_estrella = ""
    for d in range(1, 6):
        rec = recaudacion_dias[d]
        if rec > max_recaudacion:
            max_recaudacion = rec
            dia_estrella = dias_nombres[d]
            
    print("\n3. Destacados[cite: 1]:")
    print("- Producto más vendido:", prod_estrella, "con", max_unidades, "unidades.")
    print("- Día de mayor recaudación:", dia_estrella, "con $", max_recaudacion)

    print("\n4. Productos sin ventas[cite: 1]:")
    sin_ventas = False
    for p in productos:
        if unidades_productos[p["codigo"]] == 0:
            print("-", p["nombre"])
            sin_ventas = True
    if sin_ventas == False:
        print("Todos los productos registraron al menos una venta.")

    total_semana = 0
    for d in range(1, 6):
        total_semana += recaudacion_dias[d]
    print("\n5. Recaudación total de la semana: $", total_semana,[cite: 1])

def main():
    productos = cargarProductos()
    ventas = cargarVentas()
    opcion = ""
    while opcion != "3":
        print("BUFFET DE LA FACULTAD")
        print("1. Registrar venta")
        print("2. Ver informes de la semana")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrarVenta(ventas, productos)
        elif opcion == "2":
            verInformes(productos, ventas)
        elif opcion == "3":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")

main()