# generador_numeros_aleatorios.py

import random

def generar_numeros_aleatorios(cantidad, inicio, fin):
    return [random.randint(inicio, fin) for _ in range(cantidad)]

def generador():
    print("Generador de Números Aleatorios")
    cantidad = int(input("Ingrese la cantidad de números a generar: "))
    inicio = int(input("Ingrese el inicio del rango: "))
    fin = int(input("Ingrese el fin del rango: "))
    
    numeros = generar_numeros_aleatorios(cantidad, inicio, fin)
    print(f"Números generados: {numeros}")

if __name__ == "__main__":
    generador()
