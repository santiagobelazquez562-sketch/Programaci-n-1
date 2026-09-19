genero=input("Ingrese su genero (hombre o mujer): ")
edad=int(input("Ingrese su edad: "))
if genero == "hombre" and edad >= 18:
    print( "Usted es hombre y puede votar")
elif genero== "mujer" and edad >= 18:
    print("Usted es mujer y puede votar")
else:
    print("usted no cumple con los requisitos para votar")
  