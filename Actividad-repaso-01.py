texto = input("Ingrese el mensaje a codificar: ")
texto = texto.upper()

texto = texto.replace("Á", "A")
texto = texto.replace("É", "E")
texto = texto.replace("Í", "I")
texto = texto.replace("Ó", "O")
texto = texto.replace("Ú", "U")

mensaje_codificado = ""

for letra in texto:
    if letra == "A":
        mensaje_codificado = mensaje_codificado + "X"
    elif letra == "E":
        mensaje_codificado = mensaje_codificado + "W"
    elif letra == "I":
        mensaje_codificado = mensaje_codificado + "K"
    elif letra == "O":
        mensaje_codificado = mensaje_codificado + "&"
    elif letra == "U":
        mensaje_codificado = mensaje_codificado + "%"
    else:
        mensaje_codificado = mensaje_codificado + letra

print("Mensaje codificado:", mensaje_codificado)