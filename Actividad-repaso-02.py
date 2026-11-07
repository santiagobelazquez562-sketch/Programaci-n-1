parrafo = input("Ingrese el párrafo: ")

cantidad_palabras = 0
en_palabra = False

for caracter in parrafo:
    if caracter != " " and caracter != "," and caracter != ";" and caracter != "." and caracter != "\n":
        if en_palabra == False:
            cantidad_palabras = cantidad_palabras + 1
            en_palabra = True
    else:
        en_palabra = False

print("Resultado correcto:", cantidad_palabras)

