def main():
    saldo = 50000.0
    opcion = 0
    
    historial = []
    
    while opcion != 5:
        print(" CAJERO AUTOMÁTICO ")
        print("1. Consultar saldo disponible")
        print("2. Depositar dinero")
        print("3. Extraer dinero")
        print("4. Ver historial de movimientos")
        print("5. Salir del sistema")
        
        opcion = int(input("Seleccione una opción (1-5): "))
        
        if opcion == 1:
            print("Su saldo actual es: $", saldo)
            
        elif opcion == 2:
            monto = float(input("Ingrese el monto a depositar: "))
            saldo = saldo + monto
            historial.append("Depósito: +$" + str(monto))
            print("Depósito realizado con éxito. Su saldo actual es: $", saldo)
            
        elif opcion == 3:
            monto = float(input("Ingrese el monto a extraer: "))
            if monto <= saldo:
                saldo = saldo - monto
                historial.append("Extracción: -$" + str(monto))
                print("Extracción realizada con éxito. Su saldo actual es: $", saldo)
            else:
                print("Fondos insuficientes para realizar la operación.")
                
        elif opcion == 4:
            print(" HISTORIAL DE MOVIMIENTOS ")
            if len(historial) == 0:
                print("No hay movimientos registrados en esta sesión.")
            else:
                for i in range(len(historial)):
                    print(i + 1, ".", historial[i])
                    
        elif opcion == 5:
            print("Sesión cerrada.")
            
        else:
            print("Opción no válida, seleccione una opción del 1 al 5.")

main()