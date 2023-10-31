import csv

# Lista para almacenar la información de los equipos
equipos = []

# Apertura del archivo CSV
with open('Copa_Mundial_2023.csv', 'r') as csvfile:
    lector_csv = csv.reader(csvfile)
    cabeceras = next(lector_csv)  # Lee la primera línea como cabeceras

    # Procesamiento de cada fila en el archivo CSV
    for fila in lector_csv:
        # Extracción de los valores de la fila
        equipo_casa, equipo_visita, goles_casa, goles_visita, tarjetas_casa, tarjetas_visita = fila

        # Conversión de valores a enteros
        goles_casa = int(goles_casa)
        goles_visita = int(goles_visita)
        tarjetas_casa = int(tarjetas_casa)
        tarjetas_visita = int(tarjetas_visita)

        # Búsqueda y actualización de la información de los equipos
        for equipo in equipos:
            if equipo[0] == equipo_casa:
                if goles_casa > goles_visita:
                    equipo[1] += 3 #esto 
                elif goles_casa == goles_visita:
                    equipo[1] += 1
                equipo[2] += goles_casa
                equipo[3] += tarjetas_casa
                break
        else:
            equipos.append([equipo_casa, 3 if goles_casa > goles_visita else 1 if goles_casa == goles_visita else 0, goles_casa, tarjetas_casa])

        for equipo in equipos:
            if equipo[0] == equipo_visita:
                if goles_visita > goles_casa:
                    equipo[1] += 3
                elif goles_casa == goles_visita:
                    equipo[1] += 1
                equipo[2] += goles_visita
                equipo[3] += tarjetas_visita
                break
        else:
            equipos.append([equipo_visita, 3 if goles_visita > goles_casa else 1 if goles_casa == goles_visita else 0, goles_visita, tarjetas_visita])

# Impresión de los resultados de los equipos
print("{:<15} {:<8} {:<6} {:<9}".format('Equipo', 'Puntos', 'Goles', 'Tarjetas')) 
for equipo in equipos:
    print("{:<15} {:<8} {:<6} {:<9}".format(equipo[0], equipo[1], equipo[2], equipo[3]))