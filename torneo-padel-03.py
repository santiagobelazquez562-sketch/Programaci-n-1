import json

def cargarJugadores():
    archivo = open("jugadores.json", "a+")
    archivo.seek(0)
    contenido = archivo.read()
    archivo.close()
    if contenido == "":
        return []
    return json.loads(contenido)

def guardarJugadores(jugadores):
    archivo = open("jugadores.json", "w")
    json.dump(jugadores, archivo)
    archivo.close()

def cargarParejas():
    archivo = open("parejas.json", "a+")
    archivo.seek(0)
    contenido = archivo.read()
    archivo.close()
    if contenido == "":
        return []
    return json.loads(contenido)

def guardarParejas(parejas):
    archivo = open("parejas.json", "w")
    json.dump(parejas, archivo)
    archivo.close()

def registrarJugadores(jugadores):
    cantidad = int(input("¿Cuántos jugadores van a participar en el torneo?: "))
    for i in range(cantidad):
        print("Jugador", i + 1)
        nombre = input("Nombre: ")
        categoria = input("Categoría (4, 5, 6): ")
        jugador = {"nombre": nombre, "categoria": categoria}
        jugadores.append(jugador)
    guardarJugadores(jugadores)
    print("Jugadores guardados con éxito.")

def mostrarJugadores(jugadores):
    if len(jugadores) == 0:
        print("No hay jugadores inscriptos.")
    else:
        print("LISTA DE INSCRIPTOS")
        for i in range(len(jugadores)):
            print(i + 1, ")", jugadores[i]["nombre"], "- Categoría:", jugadores[i]["categoria"])

def buscarJugador(jugadores):
    if len(jugadores) == 0:
        print("No hay jugadores inscriptos.")
        return

    copia_jugadores = []
    for j in jugadores:
        copia_jugadores.append(j.copy())
    
    n = len(copia_jugadores)
    comparaciones = 0
    intercambios = 0

    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            comparaciones = comparaciones + 1
            if copia_jugadores[j]["nombre"] < copia_jugadores[pos_min]["nombre"]:
                pos_min = j
        
        aux = copia_jugadores[i]
        copia_jugadores[i] = copia_jugadores[pos_min]
        copia_jugadores[pos_min] = aux
        intercambios = intercambios + 1

    print("LISTA DE INSCRIPTOS EN ORDEN ALFABETICO")
    for k in range(len(copia_jugadores)):
        print(k + 1, ")", copia_jugadores[k]["nombre"], "- Categoría:", copia_jugadores[k]["categoria"])
    
    print("Comparaciones:", comparaciones, "Intercambios:", intercambios)

    buscado = input("Ingrese el nombre del jugador a buscar: ")
    encontrado = False
    for jugador in copia_jugadores:
        if jugador["nombre"] == buscado:
            print("El jugador", jugador["nombre"], "está inscripto en la categoría", jugador["categoria"])
            encontrado = True
            break
    if encontrado == False:
        print("El jugador no está inscripto.")

def mostrarCarteleraCategorias(jugadores):
    if len(jugadores) == 0:
        print("No hay jugadores inscriptos.")
        return

    categorias = []
    for j in jugadores:
        cat = j["categoria"]
        existe_cat = False
        for c in categorias:
            if c == cat:
                existe_cat = True
                break
        if not existe_cat:
            categorias.append(cat)

    n_cat = len(categorias)
    for i in range(n_cat - 1):
        for j in range(n_cat - 1 - i):
            if categorias[j] > categorias[j + 1]:
                aux_c = categorias[j]
                categorias[j] = categorias[j + 1]
                categorias[j + 1] = aux_c

    print("CARTELERA JUGADORES POR CATEGORIA")
    
    total_comparaciones = 0
    total_intercambios = 0

    for cat in categorias:
        jugadores_cat = []
        for j in jugadores:
            if j["categoria"] == cat:
                jugadores_cat.append(j.copy())
        
        n = len(jugadores_cat)
        comp_burbuja = 0
        inter_burbuja = 0
        
        for i in range(n - 1):
            for j in range(n - 1 - i):
                comp_burbuja = comp_burbuja + 1
                if jugadores_cat[j]["nombre"] > jugadores_cat[j + 1]["nombre"]:
                    aux = jugadores_cat[j]
                    jugadores_cat[j] = jugadores_cat[j + 1]
                    jugadores_cat[j + 1] = aux
                    inter_burbuja = inter_burbuja + 1
        
        total_comparaciones = total_comparaciones + comp_burbuja
        total_intercambios = total_intercambios + inter_burbuja

        print("Categoría:", cat)
        for jg in jugadores_cat:
            print(jg["nombre"])

    print("Comparaciones:", total_comparaciones, "Intercambios:", total_intercambios)

def eliminarJugador(jugadores):
    nombre = input("Ingrese el nombre del jugador lesionado a eliminar: ")
    encontrado = False
    for jugador in jugadores:
        if jugador["nombre"] == nombre:
            jugadores.remove(jugador)
            guardarJugadores(jugadores)
            print("Jugador eliminado correctamente.")
            encontrado = True
            break
    if encontrado == False:
        print("No se encontró al jugador.")

def armarParejas(jugadores, parejas):
    if len(jugadores) < 2:
        print("No hay suficientes jugadores para armar parejas.")
        return
    nombre_pareja = input("Ingrese el nombre de la pareja: ")
    mostrarJugadores(jugadores)
    pos1 = int(input("Ingrese el número del primer jugador: ")) - 1
    pos2 = int(input("Ingrese el número del segundo jugador: ")) - 1
    if pos1 < 0 or pos1 >= len(jugadores) or pos2 < 0 or pos2 >= len(jugadores):
        print("Número no válido.")
        return
    if pos1 == pos2:
        print("No puede elegir al mismo jugador dos veces.")
        return
    
    puntos_iniciales = int(input("Ingrese los puntos iniciales de la pareja: "))

    pareja = {
        "nombre": nombre_pareja,
        "jugadores": [jugadores[pos1]["nombre"], jugadores[pos2]["nombre"]],
        "puntos": puntos_iniciales
    }
    parejas.append(pareja)
    guardarParejas(parejas)
    print("Pareja armada y guardada con éxito.")

def mostrarParejasYPosiciones(parejas):
    if len(parejas) == 0:
        print("No hay parejas armadas.")
        return

    copia_parejas = []
    for p in parejas:
        copia_parejas.append(p.copy())

    n = len(copia_parejas)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if copia_parejas[j]["puntos"] < copia_parejas[j + 1]["puntos"]:
                aux = copia_parejas[j]
                copia_parejas[j] = copia_parejas[j + 1]
                copia_parejas[j + 1] = aux

    print("TABLA DE POSICIONES")
    for i in range(len(copia_parejas)):
        p = copia_parejas[i]
        print(i + 1, p["nombre"], p["jugadores"][0], p["jugadores"][1], p["puntos"])

def main():
    jugadores = cargarJugadores()
    parejas = cargarParejas()
    opcion = ""
    while opcion != "9":
        print("MENU TORNEO DE PADEL")
        print("1. Registrar jugadores")
        print("2. Mostrar lista de inscriptos")
        print("3. Buscar jugador")
        print("4. Mostrar cartelera por categoría")
        print("5. Eliminar jugador")
        print("6. Armar parejas y asignar puntos")
        print("7. Mostrar parejas")
        print("8. Ver tabla de posiciones")
        print("9. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            registrarJugadores(jugadores)
        elif opcion == "2":
            mostrarJugadores(jugadores)
        elif opcion == "3":
            buscarJugador(jugadores)
        elif opcion == "4":
            mostrarCarteleraCategorias(jugadores)
        elif opcion == "5":
            eliminarJugador(jugadores)
        elif opcion == "6":
            armarParejas(jugadores, parejas)
        elif opcion == "7":
            mostrarParejasYPosiciones(parejas)
        elif opcion == "8":
            mostrarParejasYPosiciones(parejas)
        elif opcion == "9":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")

main()