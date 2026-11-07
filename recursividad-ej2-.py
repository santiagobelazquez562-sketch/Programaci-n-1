def viaje_simulado (km_faltan):
    if km_faltan == 0:
        print("viaje terminado")
    else:
        print(f"Faltan {km_faltan} km para llegar.")
        viaje_simulado(km_faltan - 1)

viaje_simulado(18)