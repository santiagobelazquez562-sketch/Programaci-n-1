peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en centimetros: "))
imc = peso / (estatura ** 2)

resul_imc = round(imc, 2)
print("Tu índice de masa corporal es", resul_imc)