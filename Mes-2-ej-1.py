estudiantes = [
    {"nombre": "Juan", "notas": [7, 8, 9, 6], "asistencia": 83},
    {"nombre": "Maria", "notas": [5, 6, 4, 7], "asistencia": 70},
    {"nombre": "Pedro", "notas": [1, 9, 4, 7], "asistencia": 99},
    {"nombre": "Ana", "notas": [6, 5, 7, 8], "asistencia": 77},
]
for alumno in estudiantes: 
    nombre = alumno["nombre"]
    notas = alumno["notas"]
    asistencia = alumno["asistencia"]
    promedio= suma = sum(notas) / len(notas)
    if notas[0] >= 6 and notas[1] >= 6 and notas[2] >= 6 and notas[3] >= 6 and promedio >= 6 and asistencia >= 75:
        print(nombre, "está regular con un promedio de", promedio, "y una asistencia de", asistencia)
    else:
        print(nombre, "no está regular, su promedio es de", promedio, " y su asitencia es de", asistencia)
