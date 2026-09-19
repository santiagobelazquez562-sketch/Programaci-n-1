USUARIO_CORRECTO = "santi"
CONTRASEÑA_CORRECTA = "010101"
usuario = input ("Ingrese su usuario: ")
contraseña = input ("Ingrese su contraseña: ")
if usuario == USUARIO_CORRECTO and contraseña == CONTRASEÑA_CORRECTA:
    print( "información válida, puede ingresar ")
else:
    print(" Datos erroneos, intente denuevo")
