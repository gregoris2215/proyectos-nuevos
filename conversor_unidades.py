# conversor_unidades.py

def convertir_unidad(valor, unidad_origen, unidad_destino):
    unidades = {
        'kilómetros': 1.0,
        'metros': 1000.0,
        'centímetros': 100000.0,
        'milímetros': 1000000.0,
        'millas': 0.621371,
        'yardas': 1094.0,
        'pies': 3280.84,
        'pulgadas': 39370.1,
    }

    if unidad_origen not in unidades or unidad_destino not in unidades:
        raise ValueError("Unidad no soportada")

    valor_metros = valor / unidades[unidad_origen]
    valor_convertido = valor_metros * unidades[unidad_destino]
    return valor_convertido

def main():
    valor = float(input("Ingrese el valor a convertir: "))
    unidad_origen = input("Ingrese la unidad de origen (kilómetros, metros, centímetros, milímetros, millas, yardas, pies, pulgadas): ")
    unidad_destino = input("Ingrese la unidad de destino (kilómetros, metros, centímetros, milímetros, millas, yardas, pies, pulgadas): ")
    resultado = convertir_unidad(valor, unidad_origen, unidad_destino)
    print(f"{valor} {unidad_origen} son {resultado:.2f} {unidad_destino}")

if __name__ == "__main__":
    main()
