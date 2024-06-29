#TAREA 1 - EJERCICIOS BASICOS EN PYTHON

# SU NOMBRE:Gregoris de la cruz 
# MATRICULA:2023-1122

#1.	Declarar variable de los diferentes tipos, asignarles valor e imprimir el valor. 
# Declaración de un entero

numero_entero = 123
print(numero_entero)

# Declaración de un número de punto flotante
numero_decimal = 5.67
print(numero_decimal)

# Declaración de un booleano
es_verdadero = True
print(es_verdadero)

# Declaración de una cadena de texto
mensaje = "Hola, cómo va tu dia ?"
print(mensaje)

# Declaración de una lista
lista_elementos = ['apple', 'banana', 'orange', 'grape']
print(lista_elementos)

# Declaración de una tupla
tupla_valores = (15, 25, 35, 45)
print(tupla_valores)

# Declaración de un diccionario
diccionario_datos = {'clave': 100, 'clave': 200, 'clave': 300}
print(diccionario_datos)

#=============================================================================================================================

# 2 Solicitar al usuario ingresar la velocidad y el tiempo
tiempo= float(input("Introduzca el tiempo de viaje en horas: "))
velocidad= float(input("Introduzca la velocidad del vehículo en km/h: "))


distanciarecorrida = tiempo * velocidad

print("La distancia recorrida es: " + str(distanciarecorrida) + " km")

#===============================================================================================================================
#3. Calcular el promedio simple de notas de un estudiante de sustres notas parciales N1, N2, N3

calificacion_1 = float(input("Introduza la primera calificación: "))
calificacion_2 = float(input("Introduzca la segunda calificación: "))
calificacion_3 = float(input("Introduzca la tercera calificación: "))

calificaciones = (calificacion_1 + calificacion_2 + calificacion_3) / 3

print("El promedio de las calificaciones es: " + str(calificaciones))

#===========================================================================================================================
#4. Hacer un programa que permita ingresar el número de partidos ganados, perdidos y empatados, 
# por noticias SIN  en  el  torneo  apertura, se  debe  de  mostrar  su  puntaje  total,  
# teniendo  en  cuenta  que  por  cada  partido ganado obtendrá 3 puntos, empatado 1 punto y perdido 0 puntos.


ganados = int(input("Introduza el número de partidos ganados: "))
perdidos= int(input("Introduzca  el número de partidos perdidos: "))
empatados= int(input("Introduzca el número de partidos empatados: "))

puntajetotal = (ganados * 3) + (empatados * 1) + (perdidos * 0)

print("El puntaje total es: " + str(puntajetotal))

#==============================================================================================================================

#5. Calcular el perimetro y superficie d eun rectangulo. Se debe solicitar al usuario introduzca la base y la altura.


base = float(input("Introduzca la base del rectángulo: "))
altura = float(input("Introduzca  la altura del rectángulo: "))

perimetro = 2 * (base + altura)
superficie = base * altura

print("El perímetro del rectángulo es: " + str(perimetro))
print("La superficie del rectángulo es: " + str(superficie))

#===================================================================================================================================

#6. Calcular el area y el volumen de un cilindro. Soliictar al usuario introduzca el radio y la altura.


radio = float(input("Introduzca el radio del cilindro: "))
altura= float(input("Introduzca la altura del cilindro: "))

area = 2 * 3.14 * radio * (radio+ altura)
volumen = 3.14 * radio**2 * altura

print("El área del cilindro es: " + str(area))
print("El volumen del cilindro es: " + str(volumen))

#=====================================================================================================================================
#7. Calcular el volumen de una esfera. Pedir al usuario introduzca el Radio.

dradio = float(input("Indroduzca el radio de la esfera: "))

dvolumen = (4/3) * 3.14 * (dradio**3)

print("El volumen de la esfera es: " + str(dvolumen))

#===================================================================================================================================
#8. Calcular el Perímetro de un tríangulo equilatero. Pedir al usuario ingrese la altura del triangulo.

radio = float(input("Radio: "))

volumen = (4/3) * 3.14 * radio**3

print("Volumen: " + str(volumen))
#================================================================================================================================

#9. Calcular el cambio de moneda dominicana a dolares y euros. pedir al usuario introduzca cantidad de pesos.


kpesos = float(input("Introduzca la cantidad de pesos dominicanos: "))

cambio_dolar = 60.25
cambio_euro = 67.80

cantidad_do = round(kpesos / cambio_dolar, 2)
cantidad_eur = round(kpesos / cambio_euro , 2)

print(str(kpesos) + " pesos dominicanos equivalen a: " + str(cantidad_do) + " dólares")
print(str(kpesos) + " pesos dominicanos equivalen a: " + str(cantidad_eur) + " euros")



#10. Calcule la velocidad de un automóvil. Pedir al usuario ingrese tiempo en segundos y distincia en metros.


dtiempo = float(input("Introduzca  el tiempo en segundos: "))
ddistancia = float(input("Introduzca la distancia en metros: "))

dvelocidad = ddistancia / dtiempo

print("La velocidad del automóvil es: " + str(dvelocidad) + " metros por segundo")


#Recuerde probar cada codigo individualmente :)
