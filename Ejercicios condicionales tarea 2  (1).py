#Ejercicios condicionales 

#NOMBRE:GREGORIS DE LA CRUZ 
#MATRICULA:2023-1122

#1- Pida a usuario la edad y el sexo, para que la computadora le indique si ya puede jubilarse.
# Tome en cuenta que un Hombre se puede jubilar cuando tenga 60 años o más, en cambio, 
# una mujer mayor se jubilara si tiene más de 54 años.

def main():
    edad = int(input("Introduzca su edad: "))
    sexo = input("Introduzca  su sexo (Hombre/Mujer): ").capitalize()

    if (sexo == "Hombre" and edad >= 60) or (sexo == "Mujer" and edad >= 54):
        print(" Usted  ya se puede jubilar.")
    else:
        print("todavia  no puede jubilarse.")

if __name__ == "__main__":
    main()

#2- Solicitar al usuario que introduzca la figura geometrica y que introduzca el valor del area que desea 
# calculara. 
# Las figuras geométricas disponibles son el triangulo, circulo, rectángulo y un hexágono. 

import math

def calcular_elarea(figura, *args):
    if figura == "triangulo":
        return 0.5 * args[0] * args[1]
    elif figura == "circulo":
        return math.pi * args[0] ** 2
    elif figura == "rectangulo":
        return args[0] * args[1]
    elif figura == "hexagono":
        return (3 * math.sqrt(3) * args[0] ** 2) / 2
    else:
        return None

def main():
    figura = input("Introduzca la figura geométrica (triangulo, circulo, rectangulo, hexagono): ").lower()
    valores = [float(input(f"Introduzaca el valor {i+1}: ")) for i in range(2)]
    area = calcular_elarea(figura, *valores) if figura in ["triangulo", "circulo", "rectangulo", "hexagono"] else None
    print(f"El área de l {figura} es: {area}" if area is not None else "Figura no válida.")

if __name__ == "__main__":
    main()

#3- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un 
# nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario 
# su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def main():
    nombre, sexo = input("Introduza  su nombre: "), input("Introduzca  su sexo (Hombre/Mujer): ").capitalize()
    print(f"Usted pertenece al {'Grupo A' if (sexo == 'Mujer' and nombre[0].lower() < 'm') or (sexo == 'Hombre' and nombre[0].lower() > 'n') else 'Grupo B'}.")

if __name__ == "__main__":
    main()

#4- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere 
# calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe 
# preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 
# 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5 USD y si es mayor de 18 años, 10 USD.
    
def main():
    edad = int(input("Introduzca  la edad del cliente: "))
    print(f"El precio de  la entrada es: {0 if edad < 4 else 5 if edad <= 18 else 10} USD")

if __name__ == "__main__":
    main()

#5- interruptores para encender un foco. En un circuito eléctrico hay tres interruptores, los cuales
# pueden estar en estado cerrado(1) o abierto(0).Para que un equipo funcione, se requiere que al menos
# dos estén cerrados. Si los datos son el estado de los interruptores, determine si el equipo funcionará.
    
interruptores = [int(input(f"Estado del interruptor {i + 1} (0 para abierto, 1 para cerrado): ")) for i in range(3)]
print("El equipo funcionará correctamente ." if sum(interruptores) >= 2 else "El equipo no funcionará correctamente .")


#6- Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin teniendo  en cuenta mayúsculas y minúsculas.

print("¡Contraseña correcta!" if input("Ingrese la contraseña: ").lower() == "contraseña".lower() else "¡Contraseña incorrecta!")
    
#7- Escribe un programa que lea dos números y determine cuál de ellos es el mayor.

a, b = float(input("Introduzca el primer número: ")), float(input("Introduzca  el segundo número: "))
print(f"{(a, b)[a < b]} es mayor que {(a, b)[a > b]}." if a != b else "Los números son iguales.")

#8- Realice un programa que lea un valor entero y determine si se trata de un número par o impar. 
# Sugerencia: un número es par si el resto de dividirlo entre dos es cero.

numero = int(input("Introduzca  un número entero: "))
print(f"{numero} es un número {'par' if numero % 2 == 0 else 'impar'}.")

#9- Escribe un programa que lea del teclado un carácter e indique en la pantalla si el carácter 
# es una vocal minúscula o no.

caracter = input("Introduzca un carácter: ")
print(f"{caracter} es una vocal minúscula." if caracter.lower() in 'aeiou' else f"{caracter} no es una vocal minúscula.")

#10- Escribe un programa que lea del teclado un carácter e indique en la pantalla si el carácter 
# es una vocal minúscula, es una vocal mayúscula o no es una vocal.

caracter = input("Introduzca  un carácter: ")
print(f"{caracter} es una vocal minúscula." if caracter.lower() in 'aeiou' else f"{caracter} es una vocal mayúscula." if caracter.upper() in 'AEIOU' else f"{caracter} no es una vocal.")

#11- Escribe un programa que reciba un año y nos diga si es bisiesto o no.

anio = int(input("Indroduzca  un año: "))
print(f"{anio} {'es' if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) else 'no es'} un año bisiesto.")

#12- El director de una escuela está organizando un viaje de estudios y requiere determinar
# cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. 
# La forma de cobrar es la siguiente:
#* Si son 100 alumnos o más, el costo por cada alumno es de 65 euros.
#* De 50 a 99 alumnos, el costo es de 70 euros.
#* De 30 a 49 alumnos, el costo es de 95 euros.
#* Menos de 30 alumnos, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
#Realiza un programa que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada
# alumno por el viaje.

num_estudiantes  = int(input("Introduzca  el número de alumnos: "))
costo_por_alumno = 65 if num_estudiantes >= 100 else 70 if num_estudiantes>= 50 else 95 if num_estudiantes >= 30 else 0
pago_acompañia = 4000 if num_estudiantes < 30 else 0

print(f"La escuela debe cobrar {costo_por_alumno} euros a cada alumno.")
print(f"La escuela debe pagar {pago_acompañia} euros a la compañía de autobuses por el servicio.")
