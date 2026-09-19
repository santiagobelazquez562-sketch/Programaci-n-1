print("Mnú de opciones")
print("(1) Calcular Perímetro y área de un círculo")
print("(2) Calcular Perímetro y área de un pentágono")
print("(3) Calcular Perímetro y área de un rectángulo")

opcion = int(input("Ingrese la opción que quiere calcualr (1-3): "))

if opcion == 1:
    radio = float(input("Ingrese el radio del círculo: "))
    pi= 3.14
    perimetro = 2 * pi * radio 
    area= pi * (radio * radio)
    print( "El perímetro del círculo es: ",perimetro)
    print("El área del círculo es: ", area)

elif opcion == 2: 
      lado = float(input("Ingrese el lado del pentágono: "))
      apotema= float(input("Ingrese el apotema del pentágono: "))
      perimetro = 5 * lado 
      area= (perimetro * apotema) / 2
      print("El perímetro del pentágono es: ", perimetro)
      print("El área del pentágono es : ", area)

elif opcion  == 3:
     base = float( input("Ingrese la base del rectángulo. "))
     altura = float(input("Ingrese la altura del rectángulo: "))
     perimetro = 2 * ( base + altura)
     area = base * altura
     print("El perímetro del rectángulo es: ", perimetro )
     print("El área del rectángulo es: ", area )

else:
     print("Opción incorrecta, seleccionar del 1 al 3")