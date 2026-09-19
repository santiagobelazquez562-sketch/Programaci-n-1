bancos= int(input("Ingrese la cantidad de bancos disponibles en el aula: "))
alumnos= int(input("Ingrese la cantidad de alumnos en el aula: "))
if bancos >= alumnos:
    print("Los bancos son suficientes para los alumnos")
elif alumnos - bancos >0:
    print("LOs bancos no son suficientes, faltan", alumnos - bancos, "bancos")
