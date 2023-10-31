#Ejercicio #1 Calcular promedio de 10 numeros
# cantidad_numeros=int(input("Indique la cantidad de numeros de la cual desea realizar el promedio: "))
# suma_total=0
# i=1

# while cantidad_numeros>=i:
#     numero= int(input("Ingrese el numero "+ str(i) + ": "))
#     suma_total= suma_total + numero
#     i= i+1

# promedio= suma_total/cantidad_numeros
# print(f"El promedio de los: {cantidad_numeros} numeros, es de: {promedio}")

#Ejercicio#2 Calculo del factorial de un numero n ! (n factorial) 4!= 1*2*3*4=24
# numero=0
# factorial=1
# i=1

# numero=int(input("Ingrese el numero: "))
# while numero>=i:
#     factorial = factorial * i
#     i=i+1

# print(f"El factorial del numero:  {numero} es: {factorial}")

#Ejercicio#3 Contador Nota del curso

# cantidad_examenes=0
# suma_nota=0
# i=1

# cantidad_examenes=int(input("Indique la cantidad de examenes que realizo el estudiante: "))
# while cantidad_examenes>=i:
#     nota=float(input("Indique la nota del examen " + str(i) + " :"))
#     suma_nota=suma_nota+nota
#     i=i+1
#     promedio=suma_nota/cantidad_examenes

# if promedio>=70:
#     estado= "Aprobo"
# elif promedio<70 and promedio>=60:
#     estado= "Va a ampliacion"
# else:
#     estado= "Reprobo"

# print(f"El promedio de los: {cantidad_examenes} examenes es: {promedio}\n Y el estudiante: {estado}")


#Ejercicio#1 Imprimir los numeros entreros entre 1 y N
# n=int(input("Ingrese el numero entero: "))
# i=1
# pares=[] #lista de pares
# while n>=i:
#     if i%2 ==0:
#         pares.append(i)
#     i+=1

# print(f"Los numero pares entre 1 y {n} son: {pares}")

#Ejercicio#2 Imprimir los numero para atras
# numero= int(input("Ingrese el numero entero: "))

# lista= []
# while numero>=1:
#     lista.append(numero)
#     numero=numero-1

# print(f"Los numero desde {numero} hasta 1, son: {lista}")

#Ejercicio#3 
# n=int(input("Indique el numero: "))
# factorial=1
# i=1

# while n>=i:
#     factorial= factorial*i
#     i=i+1

# print(f"El factorial del numero: {n}, es: {factorial}")

#Ejercicio#4 Multiplos de N
# numero= int(input("Ingrese el numero: "))
# multiplos=[]
# i=1

# while numero>=i:
#     if numero%i==0:
#         multiplos.append(i)
#     i=i+1 #debe estar a altura del if 
# print(f"Todos los numero entre 1 y {numero} son: {multiplos}")

#Ejercicio#5 Estudiantes aprobaron
# cantidad_estudiantes=int(input("Indique la cantidad de estudiantes: "))
# estudiantes_aprobados=0
# estudiantes_ampliacion=0
# estado_reprobados=0
# i=1

# while cantidad_estudiantes>=i:
#     promedio_estudiante=int(input("Indique el promedio del estudiante " + str(i) + " :"))
#     if promedio_estudiante>=70:
#         estudiantes_aprobados=estudiantes_aprobados+1
#     elif promedio_estudiante<70 and promedio_estudiante>=60:
#         estudiantes_ampliacion=estudiantes_ampliacion+1
#     else:
#         estado_reprobados=estado_reprobados+1
#     i=i+1
# print(f"La cantidad de estudiantes aprobados fueron: {estudiantes_aprobados}")
# print(f"La cantidad de estudiantes que van a ampliacion fueron: {estudiantes_ampliacion}")
# print(f"La cantidad de estudiantes reprobaron fueron: {estado_reprobados}")

#Ejercicio#6 para grupos
cantidad_grupos=int(input("Indique la cantidad de grupos: "))
i=1

while cantidad_grupos>=i:
    estudiantes_aprobados=0
    estudiantes_ampliacion=0
    estado_reprobados=0
    cantidad_estudiantes=int(input("Indique la cantidad de estudiantes del grupo " + str(i) + " : "))
    j=1
    while cantidad_estudiantes>=j:
        promedio_estudiante=int(input("Indique el promedio del estudiante " + str(j) + " : "))
        if promedio_estudiante>=70:
            estudiantes_aprobados=estudiantes_aprobados+1
            
        elif promedio_estudiante<70 and promedio_estudiante>=60:
            estudiantes_ampliacion=estudiantes_ampliacion+1
            
        else:
            estado_reprobados=estado_reprobados+1
        j=j+1
    print(f"En el grupo: {i} hay {estudiantes_aprobados}, estudiantes aprobados")
    print(f"En el grupo: {i} hay {estudiantes_ampliacion}, estudiantes que van a ampliacion")
    print(f"En el grupo: {i} hay {estado_reprobados}, estudiantes reprobados")
    
    i=i+1

