codigos = []
nombres = []
precios = []

cantidad = int(input("¿Cuántos productos va a cargar? "))

i = 0
while i < cantidad:
    print("")
    print("Producto número", i + 1)
    nuevo_codigo = int(input("  Código: "))

    repetido = False
    j = 0
    while j < len(codigos):
        if codigos[j] == nuevo_codigo:
            repetido = True
        j = j + 1

    if repetido == True:
        print("Error: ese código ya existe, No se pudo cargar.")
    else:
        nuevo_nombre = input("Nombre: ")
        nuevo_precio = int(input("  Precio: "))
        codigos.append(nuevo_codigo)
        nombres.append(nuevo_nombre)
        precios.append(nuevo_precio)
        print("  Producto cargado.")
        i = i + 1

print("Catalogo cargado ")
i = 0
while i < len(codigos):
    print("  ", codigos[i], nombres[i], "(", precios[i], "$)")
    i = i + 1