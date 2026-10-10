<<<<<<< HEAD
cantidad= int(input("Ingrese la cantidad de jugadores: "))
nombres=[""]* cantidad
categorias=[""]* cantidad

i=0
while i < cantidad:
    print("Jugador Número", i + 1)
    nombres[i]= input("Nombre: ")
    categorias[i]= input("Categoria: ")
    i=i +1

print("LISTA DE JUGADORES")
i=0
while i < cantidad:
    print(i+1, nombres[i], "(Categoria: ",categorias[i] + ")")
    i=i+1

 
cant_Parejas= cantidad //2
nombres_Parejas= [""]* cant_Parejas
integrantes_Parejas=[""]*cant_Parejas 

i=0
while i < cant_Parejas:
    print("pareja", i+1)
    nombres_Parejas[i]= input("Nombre de la pareja: ")

    jugador_1 = int(input("Número del primer jugador: ")) - 1
    jugador_2 = int(input("Número del segundo jugador: ")) -1

    integrantes_Parejas[i]= nombres[jugador_1]+ "y" + nombres[jugador_2]
    i=i+1

print("PAJERAS PARTICIPANTES")
i=0
while i < cant_Parejas:
    print(nombres_Parejas[i], integrantes_Parejas[i])
    i=i+1
=======
cantidad= int(input("Ingrese la cantidad de jugadores: "))
nombres=[""]* cantidad
categorias=[""]* cantidad

i=0
while i < cantidad:
    print("Jugador Número", i + 1)
    nombres[i]= input("Nombre: ")
    categorias[i]= input("Categoria: ")
    i=i +1

print("LISTA DE JUGADORES")
i=0
while i < cantidad:
    print(i+1, nombres[i], "(Categoria: ",categorias[i] + ")")
    i=i+1

 
cant_Parejas= cantidad //2
nombres_Parejas= [""]* cant_Parejas
integrantes_Parejas=[""]*cant_Parejas 

i=0
while i < cant_Parejas:
    print("pareja", i+1)
    nombres_Parejas[i]= input("Nombre de la pareja: ")

    jugador_1 = int(input("Número del primer jugador: ")) - 1
    jugador_2 = int(input("Número del segundo jugador: ")) -1

    integrantes_Parejas[i]= nombres[jugador_1]+ "y" + nombres[jugador_2]
    i=i+1

print("PAJERAS PARTICIPANTES")
i=0
while i < cant_Parejas:
    print(nombres_Parejas[i], integrantes_Parejas[i])
    i=i+1
>>>>>>> 60fe0e2b1a3acae56c1c563236b509178b0847b3
