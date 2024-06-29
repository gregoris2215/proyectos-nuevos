# adivina_el_numero.py

import random

def adivina_el_numero():
    numero = random.randint(1, 100)
    intentos = 0

    while True:
        intento = int(input("Adivina el número (entre 1 y 100): "))
        intentos += 1
        if intento < numero:
            print("Demasiado bajo!")
        elif intento > numero:
            print("Demasiado alto!")
        else:
            print(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
            break

if __name__ == "__main__":
    adivina_el_numero()
