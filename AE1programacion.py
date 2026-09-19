saldo = 50000
opcion = 0

while opcion !=4:
    print("CAJERO AUTOMATICO")
    print("(1) Consultar saldo ")
    print("(2) Depositar dinero")
    print("(3) Extraer dinero ")
    print("(4) Salir del sistema")
    opcion= int(input("Seleccione una opción (1-4): "))

    if opcion ==1:
        print("Su saldo actual es: $", saldo)
    elif opcion ==2:
        monto = float(input("Ingrese el monto a depositar: "))
        saldo = saldo + monto 
        print("Depósito realizado. Su saldo actual es: $",saldo)
    elif opcion == 3:
        monto = float(input("Ingrese el monto a extraer: "))
        if monto <= saldo:
            saldo = saldo - monto
            print("Extracción realizada. Su saldo actual es: $",saldo)
        else:
            print("Los fondos no son suficientes para realizar la operación.")
    elif opcion ==4:
        print(" Sesión cerrada")
    else:
        print("Opcion incorrecta, seleccione del 1 al 4")