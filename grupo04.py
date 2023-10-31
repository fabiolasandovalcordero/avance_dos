import csv

#Lista para almacenar la información de los torneo
torneo = []


#Apertura del archivo CSV
with open('Copa_Mundial_2023.csv','r') as file:
    csvFile = csv.reader(file)
    next(csvFile)  # Lee la primera línea como nombre de las columnas

    # Procesamiento de cada fila en el archivo CSV
    for marcador in csvFile:
        # Extracción de los valores del marcador de cada partido
        equipo_casa, equipo_visita, goles_casa, goles_visita, tarjetas_casa, tarjetas_visita = marcador

        #Convertir valores string a enteros para calculos suma ctrl +k+c and de ctrl+k+u
        goles_casa = int(goles_casa)
        goles_visita = int(goles_visita)
        tarjetas_casa = int(tarjetas_casa)
        tarjetas_visita = int(tarjetas_visita)

        # Busca y actualiza la información de los equipos en lista torneo
        for equipo in torneo:
            if equipo[0] == equipo_casa:
                if goles_casa > goles_visita:
                    equipo[1] += 3
                elif goles_casa == goles_visita:
                    equipo[1] += 1
                equipo[2] += goles_casa
                equipo[3] += tarjetas_casa
                break
        else:
            torneo.append([equipo_casa, 3 if goles_casa > goles_visita else 1 if goles_casa == goles_visita else 0, goles_casa, tarjetas_casa])

        for equipo in torneo:
            if equipo[0] == equipo_visita:
                if goles_visita > goles_casa:
                    equipo[1] += 3
                elif goles_casa == goles_visita:
                    equipo[1] += 1
                equipo[2] += goles_visita
                equipo[3] += tarjetas_visita
                break
        else:
            torneo.append([equipo_visita, 3 if goles_visita > goles_casa else 1 if goles_casa == goles_visita else 0, goles_visita, tarjetas_visita])

#impresión de los resultados de los torneo#

for equipo in torneo:
    print(f"Equipo: {(equipo[0])}, Puntos: {(equipo[1])}, Goles: {(equipo[2])}, Tarjetas: {(equipo[3])}")
