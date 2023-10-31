###Debe abrir un .cvs y obtener datos de un partido, acumular los datos y luego imprimirlos

def abrir_csv():
    print('\nBienvenido!')
    nombre_archivo = input('\nIngrese el path del archivo del torneo a abrir: ')
    with open(nombre_archivo, 'r') as archivo:
        archivo_abierto = archivo.readlines()
        lineas_totales = []
        for linea in archivo_abierto:
            lineas_totales.append(linea.replace('\n','').split(','))
    return lineas_totales

def separar_info(linea):
    equipocasa = []
    equipocasa.append(linea[0])
    equipocasa.append(linea[2])
    equipocasa.append(linea[4])

    equipovisita = []
    equipovisita.append(linea[1])
    equipovisita.append(linea[3])
    equipovisita.append(linea[5])
    return equipocasa, equipovisita

def buscar_en_matriz(linea, matriz):
    new_list = [matriz.index(lista) for lista in matriz if linea[0] in lista]
    if len(new_list) == 0:
        return False
    return True

def actualizar_data(linea, matriz):
    z = buscar_en_matriz(linea, matriz)

    if z == False:
        nueva_lista = [0, 0, 0, 0]
        nueva_lista[0] = linea[0]
        nueva_lista[1] = linea[1]
        nueva_lista[2] = linea[2]
        matriz.append(nueva_lista)
    else:
        x = [matriz.index(lista) for lista in matriz if linea[0] in lista]
        z = x[0]
        matriz[z][1] = int(matriz[z][1]) + int(linea[1])
        matriz[z][2] = int(matriz[z][2]) + int(linea[2])
        return True 

def definir_ganador(equipocasa, equipovisitante, matriz):
    goles_casa = equipocasa[1]
    tarjetas_casa = equipocasa[2]

    goles_visita = equipovisitante[1]
    tarjetas_visita = equipovisitante[2]
    
    puntaje_ganador = 3
    puntaje_empate = 1

    if goles_casa > goles_visita:
        ganador = equipocasa[0]
        y = [matriz.index(lista) for lista in matriz if ganador in lista]
        z = y[0]
        matriz[z][3] = int(matriz[z][3]) + puntaje_ganador
    
    elif goles_casa < goles_visita:
            ganador = equipovisitante[0]
            y = [matriz.index(lista) for lista in matriz if ganador in lista]
            z = y[0]
            matriz[z][3] = int(matriz[z][3]) + puntaje_ganador
    
    elif goles_casa == goles_visita:
        if tarjetas_casa < tarjetas_visita:
            ganador = equipocasa[0]
            y = [matriz.index(lista) for lista in matriz if ganador in lista]
            z = y[0]
            matriz[z][3] = int(matriz[z][3]) + puntaje_ganador
        elif tarjetas_casa > tarjetas_visita:
            ganador = equipovisitante[0]
            y = [matriz.index(lista) for lista in matriz if ganador in lista]
            z = y[0]
            matriz[z][3] = int(matriz[z][3]) + puntaje_ganador
        else:
            y = [matriz.index(lista) for lista in matriz if equipocasa[0] in lista]
            z = y[0]
            matriz[z][3] = int(matriz[z][3]) + puntaje_empate

            a = [matriz.index(lista) for lista in matriz if equipovisitante[0] in lista]
            x = a[0]
            matriz[x][3] = int(matriz[x][3]) + puntaje_empate
    else:
        print("El equipo no se encuentra en el torneo")
    return True

#-----------------------------------Inicio del programa
lineas = abrir_csv()
matriz = [['Equipo', 'Goles', 'Tarjetas', 'Puntaje']]

print('\nLos resultados finales del Torneo son los siguientes')

for i in range(1, len(lineas)):
    equipos = separar_info(lineas[i])
    equipo_casa = equipos[0]
    equipo_visita = equipos[1]
    actualizar_data(equipo_casa, matriz)
    actualizar_data(equipo_visita, matriz)
    definir_ganador(equipo_casa, equipo_visita, matriz)     

#-----------------------------------Imprimir Resultados finales
print('\n')
for fila in matriz:
    tabla = '|{:15}|' * len(matriz[0])
    print(tabla.format(*fila))