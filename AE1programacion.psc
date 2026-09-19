Algoritmo CajeroAutomatico
	Definir saldo, monto Como Real
    Definir  opc Como Entero
    saldo = 50000
    opc = 0
    
	Mientras opc <> 4 Hacer
	      Escribir " CAJERO AUTOMATICO"
	      Escribir "(1)Consultar saldo disponible"
	     Escribir "(2) Depositar dinero"
	     Escribir "(3)Extraer dinero"
         Escribir "(4) Salir del sistema"
	     Escribir "Seleccione una opción(1-4): "
	    Leer opc
        
        Si opc = 1 Entonces
            Escribir "Su saldo actual es: $", saldo
        Sino
            Si opc = 2 Entonces
                Escribir "Ingrese el monto a depositar: "
                Leer monto
                saldo <- saldo + monto
                Escribir "Depósito realizado. Su saldo actual es: $", saldo
            Sino
                Si opc = 3 Entonces
                    Escribir "Ingrese el monto a extraer: "
                    Leer monto
                    Si monto <= saldo Entonces
                        saldo <- saldo - monto
                        Escribir "Extraccion realizada. Su saldo actual es: $", saldo
                    Sino
                        Escribir "Los fondos son insuficientes para realizar la operacion"
                    FinSi
                Sino
                    Si opc = 4 Entonces
                        Escribir "Sesión cerrada."
                    Sino
                        Escribir "Opcion no disponible, seleccione del 1 al 4."
                    FinSi
                FinSi
            FinSi
        FinSi
   FinMientras
FinAlgoritmo