
L = [] # agregar a la lista los nombre de los archivo 
#que valor le debo poner al coninuar afuera para continuar
continuar = "si" # para que se repita al menos una vez
while ("EVALUACION: que debe ser verdadera para que se repita", continuar == "si"):
#se crea una variable para continuar
    x=input("deme el nombre del archivo") # lo puedo sustituir
    L.append(input("deme el nombre del archivo")) # que tengo que agregar, el imput
    #CONDICION DE PARADA O MODIFICACION
    continuar = input("quiere agregar mas?")

# #2 categorias de bandera: contador y bandera
# direc = []
# continuar = "si"
# while continuar == "si":
#     direc.append(input("agregue el nombre del archivo"))
#     continuar = input("desea continuar?")

# agregue el nombre del archivo cool.txt
# quiere continuar? "si"
# agregue el nombre del archivo coca.txt
# quiere continuar? "si"
# agregue el nombre del archivo tarea.txt
# quiere continuar? "no"