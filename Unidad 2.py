""" TP:  While_Reality_Show
Enunciado:

De los 3 Jugadores de un Reality Show, se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero)
que recibió en la etapa de votos Informar:
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan mediante input()"""

# Inicializar variables
nombre1 = input("Ingrese nombre del primer candidato: ")
edad1 = int(input("Ingrese edad del primer candidato: "))
votos1 = int(input("Ingrese cantidad de votos del primer candidato: "))

nombre2 = input("Ingrese nombre del segundo candidato: ")
edad2 = int(input("Ingrese edad del segundo candidato: "))
votos2 = int(input("Ingrese cantidad de votos del segundo candidato: "))

nombre3 = input("Ingrese nombre del tercer candidato: ")
edad3 = int(input("Ingrese edad del tercer candidato: "))
votos3 = int(input("Ingrese cantidad de votos del tercer candidato: "))

# Informar a) nombre del candidato con más votos
if votos1 > votos2 and votos1 > votos3:
    print("El candidato con más votos es:", nombre1)
elif votos2 > votos1 and votos2 > votos3:
    print("El candidato con más votos es:", nombre2)
else:
    print("El candidato con más votos es:", nombre3)

# Informar b) nombre y edad del candidato con menos votos
if votos1 < votos2 and votos1 < votos3:
    print("El candidato con menos votos es:", nombre1, "de", edad1, "años")
elif votos2 < votos1 and votos2 < votos3:
    print("El candidato con menos votos es:", nombre2, "de", edad2, "años")
else:
    print("El candidato con menos votos es:", nombre3, "de", edad3, "años")

# Informar c) promedio de edades de los candidatos
promedio_edades = (edad1 + edad2 + edad3) / 3
print("El promedio de edades de los candidatos es:", promedio_edades)

# Informar d) total de votos emitidos
total_votos = votos1 + votos2 + votos3
print("El total de votos emitidos es:", total_votos)
