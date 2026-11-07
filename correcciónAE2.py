def mostrar_menu():
    print("Cajero automatico")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Extraer")
    print("4. Ver historial")
    print("5. Salir")

def consultar_saldo(saldo, historial):
    print("Su saldo actual es: $", saldo)
    historial.append("Consulta de saldo")
    
    archivo = open("movimientos.txt", "a")
    archivo.write("Consulta de saldo\n")
    archivo.close()

def depositar(saldo, historial):
    importe = float(input("Ingrese el importe a depositar: "))
    while importe <= 0:
        print("El importe tiene que ser mayor que cero")
        importe = float(input("Ingrese el importe a depositar: "))
    saldo = saldo + importe
    print("El deposito se realizo correctamente y su saldo ahora es: $", saldo)
    
    historial.append("Deposito de: $" + str(importe))
    archivo = open("movimientos.txt", "a")
    archivo.write("Deposito de: $" + str(importe) + "\n")
    archivo.close()
    return saldo

def extraer(saldo, historial):
    importe = float(input("Ingrese el importe a extraer: "))
    while importe <= 0:
        print("El importe tiene que ser mayor que cero")
        importe = float(input("Ingrese el importe a extraer: "))
    
    if importe <= saldo:
        saldo = saldo - importe
        print("La extraccion se realizo correctamente y su saldo ahora es: $", saldo)
        historial.append("Extraccion de: $" + str(importe))
        archivo = open("movimientos.txt", "a")
        archivo.write("Extraccion de: $" + str(importe) + "\n")
        archivo.close()
    else:
        print("El fondo insuficiente y su saldo actual es: $", saldo)
        historial.append("Extraccion fallida por falta de fondos")
        archivo = open("movimientos.txt", "a")
        archivo.write("Extraccion fallida\n")
        archivo.close()
    return saldo

def ver_historial(historial):
    print("HISTORIAL DE MOVIMIENTOS")
    for movimiento in historial:
        print(movimiento)

def main():
    saldo = 50000
    historial = []
    
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese una opcion: "))
        
        if opcion == 1:
            consultar_saldo(saldo, historial)
        elif opcion == 2:
            saldo = depositar(saldo, historial)
        elif opcion == 3:
            saldo = extraer(saldo, historial)
        elif opcion == 4:
            ver_historial(historial)
        elif opcion == 5:
            break
        else:
            print("La opcion no es valida, ingrese un numero del 1 al 5.")

main()