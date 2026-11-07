def descarga_juego(porcentaje):
    if porcentaje == 100:
        print("[100%] Jueg descargado")
    else:
        print(f"[{porcentaje}%] Instalado...")
        descarga_juego(porcentaje + 10)

descarga_juego(0)