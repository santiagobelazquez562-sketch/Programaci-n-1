Algoritmo cajero_automatico
    Definir saldo, importe Como Real
    Definir opcion, i, totalMovimientos Como Entero
    Dimension historial[100]
    
    saldo <- 50000
    totalMovimientos <- 0
    
    Repetir
        Escribir ""
        Escribir "Cajero automatico"
        Escribir "1. Consultar saldo"
        Escribir "2. Depositar"
        Escribir "3. Extraer"
        Escribir "4. Ver historial"
        Escribir "5. Salir"
        Escribir "Ingrese una opcion:"
        Leer opcion
        
        Segun opcion Hacer
            1:
                Escribir "Su saldo actual es: $", saldo
                Si totalMovimientos < 100 Entonces
                    totalMovimientos <- totalMovimientos + 1
                    historial[totalMovimientos] <- "Consulta de saldo"
                Fin Si
                
            2:
                Escribir "Ingrese el importe a depositar:"
                Leer importe
                Mientras importe <= 0 Hacer
                    Escribir "El importe tiene que ser mayor que cero"
                    Escribir "Ingrese el importe a depositar:"
                    Leer importe
                Fin Mientras
                
                saldo <- saldo + importe
                Escribir "El deposito se realizo correctamente y su saldo ahora es: $", saldo
                
                Si totalMovimientos < 100 Entonces
                    totalMovimientos <- totalMovimientos + 1
                    historial[totalMovimientos] <- "Deposito realizado"
                Fin Si
                
            3:
                Escribir "Ingrese el importe a extraer:"
                Leer importe
                Mientras importe <= 0 Hacer
                    Escribir "El importe tiene que ser mayor que cero"
                    Escribir "Ingrese el importe a extraer:"
                    Leer importe
                Fin Mientras
                
                Si importe <= saldo Entonces
                    saldo <- saldo - importe
                    Escribir "La extraccion se realizo correctamente y su saldo ahora es: $", saldo
                    
                    Si totalMovimientos < 100 Entonces
                        totalMovimientos <- totalMovimientos + 1
                        historial[totalMovimientos] <- "Extraccion realizada"
                    Fin Si
                SiNo
                    Escribir "Fondo insuficiente y su saldo actual es: $", saldo
                    Si totalMovimientos < 100 Entonces
                        totalMovimientos <- totalMovimientos + 1
                        historial[totalMovimientos] <- "Extraccion fallida"
                    Fin Si
                Fin Si
                
            4:
                Escribir "HISTORIAL DE MOVIMIENTOS"
                Si totalMovimientos = 0 Entonces
                    Escribir "No hay movimientos registrados todavia."
                SiNo
                    Para i <- 1 Hasta totalMovimientos Hacer
                        Escribir historial[i]
                    Fin Para
                Fin Si
                
            5:
                
            De Otro Modo:
                Escribir "La opcion no es valida, ingrese un numero del 1 al 5."
        Fin Segun
        
    Hasta Que opcion = 5
FinAlgoritmo