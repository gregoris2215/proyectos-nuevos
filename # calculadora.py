# calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

def calculadora():
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        opcion = input("Ingrese la opción (1/2/3/4): ")

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == '1':
                print(f"Resultado: {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {restar(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"Resultado: {dividir(num1, num2)}")

            siguiente = input("¿Desea realizar otra operación? (s/n): ")
            if siguiente.lower() != 's':
                break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    calculadora()
