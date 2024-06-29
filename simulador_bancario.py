# simulador_bancario.py

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de ${cantidad:.2f} realizado. Saldo actual: ${self.saldo:.2f}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad:.2f} realizado. Saldo actual: ${self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")

def main():
    cuenta = CuentaBancaria("Juan Pérez", 1000)
    while True:
        print("\n1. Ver Saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print(f"Saldo actual: ${cuenta.saldo:.2f}")
        elif opcion == '2':
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        elif opcion == '3':
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
