# simulador_dados.py

import random

def lanzar_dado(carillas):
    return random.randint(1, carillas)

def main():
    carillas = int(input("Ingrese el número de caras del dado: "))
    cantidad = int(input("Ingrese cuántas veces lanzar el dado: "))

    for _ in range(cantidad):
        resultado = lanzar_dado(carillas)
        print(f"Resultado del lanzamiento: {resultado}")

if __name__ == "__main__":
    main()
