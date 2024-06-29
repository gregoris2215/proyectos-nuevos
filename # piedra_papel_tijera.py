# piedra_papel_tijera.py

import random

def obtener_eleccion_usuario():
    eleccion = input("Ingrese su elección (piedra, papel, tijera): ").lower()
    while eleccion not in ['piedra', 'papel', 'tijera']:
        eleccion = input("Elección inválida. Intente de nuevo: ").lower()
    return eleccion

def obtener_eleccion_computadora():
    return random.choice(['piedra', 'papel', 'tijera'])

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):
        return "Ganaste"
    else:
        return "Perdiste"

def juego():
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    while True:
        eleccion_usuario = obtener_eleccion_usuario()
        eleccion_computadora = obtener_eleccion_computadora()
        print(f"Computadora eligió: {eleccion_computadora}")
        resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
        print(f"Resultado: {resultado}")

        siguiente = input("¿Desea jugar otra vez? (s/n): ")
        if siguiente.lower() != 's':
            break

if __name__ == "__main__":
    juego()
