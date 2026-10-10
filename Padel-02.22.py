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
            print(i + 1, ")", jugadores[i]["nombre"], "categoria:", jugadores[i]["categoria"])

def buscarJugador(jugadores):
    buscado = input("Ingrese el nombre del jugador a buscar: ")
    encontrado = False
    for jugador in jugadores:
        if jugador["nombre"] == buscado:
            print("El jugador", jugador["nombre"], "está inscripto en la categoría", jugador["categoria"])
            encontrado = True
            break
    if encontrado == False:
        print("El jugador no está inscripto.")

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
    pareja = {
        "nombre": nombre_pareja,
        "jugadores": [jugadores[pos1]["nombre"], jugadores[pos2]["nombre"]]
    }
    parejas.append(pareja)
    guardarParejas(parejas)
    print("Pareja armada y guardada con éxito.")

def mostrarParejas(parejas):
    if len(parejas) == 0:
        print("No hay parejas armadas.")
    else:
        print("PAREJAS DEL TORNEO")
        for pareja in parejas:
            print("Pareja:", pareja["nombre"], "integrantes:", pareja["jugadores"][0], "y", pareja["jugadores"][1])

def main():
    jugadores = cargarJugadores()
    parejas = cargarParejas()
    opcion = ""
    while opcion != "7":
        print("MENU TORNEO DE PADEL")
        print("1. Registrar jugadores")
        print("2. Mostrar lista de inscriptos")
        print("3. Buscar jugador por nombre")
        print("4. Eliminar jugador (lesión)")
        print("5. Armar parejas")
        print("6. Mostrar parejas")
        print("7. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrarJugadores(jugadores)
        elif opcion == "2":
            mostrarJugadores(jugadores)
        elif opcion == "3":
            buscarJugador(jugadores)
        elif opcion == "4":
            eliminarJugador(jugadores)
        elif opcion == "5":
            armarParejas(jugadores, parejas)
        elif opcion == "6":
            mostrarParejas(parejas)
        elif opcion == "7":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")

main()