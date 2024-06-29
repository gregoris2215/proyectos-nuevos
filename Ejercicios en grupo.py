#Ejercicios
#POO
#1. Considera estás desarrollando un programa python donde necesitas 
#trabajar con objetos de tipo Persona. Define una clase Persona, pero en 
#este caso considerando los siguientes atributos de clase: nombre (Str), 
#apellidos (Str), edad (int), casado (boolean), 
#numeroDocumentoIdentidad(Str) y 3 metodos como acciones diferentes
#por persona de acuerdo a una profesión. Define un constructor y los 
#métodos para poder establecer y obtener los valores de los atributos. 
#Mínimo 7 personas diferentes con acciones diferentes.

class Persona:
    def __init__(self, nombre, apellidos, edad, casado, numeroDocumentoIdentidad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.casado = casado
        self.numeroDocumentoIdentidad = numeroDocumentoIdentidad
    
    # Métodos setters
    def establecer_nombre(self, nombre):
        self.nombre = nombre
    
    def establecer_apellidos(self, apellidos):
        self.apellidos = apellidos
    
    def establecer_edad(self, edad):
        self.edad = edad
    
    def establecer_casado(self, casado):
        self.casado = casado
    
    def establecer_numeroDocumentoIdentidad(self, numeroDocumentoIdentidad):
        self.numeroDocumentoIdentidad = numeroDocumentoIdentidad
    
    # Métodos getters
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_apellidos(self):
        return self.apellidos
    
    def obtener_edad(self):
        return self.edad
    
    def obtener_casado(self):
        return self.casado
    
    def obtener_numeroDocumentoIdentidad(self):
        return self.numeroDocumentoIdentidad
    
    # Métodos de acciones por profesión (ejemplos generales)
    def accion(self, profesion):
        if profesion == "profesor":
            return f"{self.nombre} está dando una clase de historia."
        elif profesion == "medico":
            return f"{self.nombre} está consultando a un paciente."
        elif profesion == "ingeniero":
            return f"{self.nombre} está supervisando la construcción de un edificio."
        elif profesion == "abogado":
            return f"{self.nombre} está defendiendo a un cliente en el tribunal."
        elif profesion == "chef":
            return f"{self.nombre} está preparando un plato gourmet."
        elif profesion == "piloto":
            return f"{self.nombre} está pilotando un avión comercial."
        elif profesion == "artista":
            return f"{self.nombre} está pintando un mural."
        else:
            return "Profesión no definida."

# Creación de 7 personas diferentes con acciones basadas en su profesión
persona1 = Persona("Juan", "Pérez", 30, False, "12345678A")
persona2 = Persona("Ana", "Gómez", 35, True, "87654321B")
persona3 = Persona("Luis", "Martínez", 45, True, "23456789C")
persona4 = Persona("Sofía", "López", 28, False, "98765432D")
persona5 = Persona("Carlos", "Jiménez", 38, True, "34567890E")
persona6 = Persona("María", "Fernández", 32, False, "56789012F")
persona7 = Persona("Jorge", "Ruiz", 40, True, "67890123G")

# Llamada a los métodos de acción para cada persona con su respectiva profesión
print(persona1.accion("profesor"))
print(persona2.accion("medico"))
print(persona3.accion("ingeniero"))
print(persona4.accion("abogado"))
print(persona5.accion("chef"))
print(persona6.accion("piloto"))
print(persona7.accion("artista"))





#2. Crea una clase Cuenta con los métodos ingreso, reintegro y 
#transferencia. La clase contendrá un constructor por defecto, un 
#constructor con parámetros y los métodos mostrar y ingresar.

class Cuenta:
    def __init__(self, titular="Desconocido", saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def mostrar(self):
        print(f"Titular: {self.titular}, Saldo: {self.saldo:.2f}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Ingresaste {cantidad:.2f}. Saldo actual: {self.saldo:.2f}")
        else:
            print("La cantidad a ingresar debe ser positiva.")

    def reintegro(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Reintegraste {cantidad:.2f}. Saldo actual: {self.saldo:.2f}")
        else:
            print("La cantidad a reintegrar es inválida o supera el saldo disponible.")

    def transferencia(self, cuenta_destino, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            cuenta_destino.saldo += cantidad
            print(f"Transferiste {cantidad:.2f} a {cuenta_destino.titular}. Tu saldo actual: {self.saldo:.2f}. Saldo destinatario: {cuenta_destino.saldo:.2f}")
        else:
            print("La cantidad a transferir es inválida o supera el saldo disponible.")

# Ejemplo de uso
cuenta1 = Cuenta("Juan Perez", 1000)
cuenta2 = Cuenta("Ana López", 500)

print("Estado inicial de las cuentas:")
cuenta1.mostrar()
cuenta2.mostrar()

print("\nRealizando operaciones...")
cuenta1.ingresar(500)
cuenta1.reintegro(200)
cuenta1.transferencia(cuenta2, 300)

print("\nEstado final de las cuentas:")
cuenta1.mostrar()
cuenta2.mostrar()





#3.Crea una clase Fracción con métodos para sumar, restar, multiplicar y 
#dividir fracciones.

from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()
    
    def simplificar(self):
        divisor_comun = gcd(self.numerador, self.denominador)
        self.numerador = self.numerador // divisor_comun
        self.denominador = self.denominador // divisor_comun

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def sumar(self, otra):
        nuevo_numerador = self.numerador * otra.denominador + otra.numerador * self.denominador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def restar(self, otra):
        nuevo_numerador = self.numerador * otra.denominador - otra.numerador * self.denominador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def multiplicar(self, otra):
        return Fraccion(self.numerador * otra.numerador, self.denominador * otra.denominador)

    def dividir(self, otra):
        return Fraccion(self.numerador * otra.denominador, self.denominador * otra.numerador)

# Ejemplo de uso
fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(3, 4)

suma = fraccion1.sumar(fraccion2)
print(f"Suma: {suma}")

resta = fraccion1.restar(fraccion2)
print(f"Resta: {resta}")

multiplicacion = fraccion1.multiplicar(fraccion2)
print(f"Multiplicación: {multiplicacion}")

division = fraccion1.dividir(fraccion2)
print(f"División: {division}")





#Crea una clase Complejo con métodos para sumar, restar, multiplicar y 
#dividir números complejos.

class Complejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        return f"{self.real} + {self.imaginario}i"

    def sumar(self, otro):
        nuevo_real = self.real + otro.real
        nuevo_imaginario = self.imaginario + otro.imaginario
        return Complejo(nuevo_real, nuevo_imaginario)

    def restar(self, otro):
        nuevo_real = self.real - otro.real
        nuevo_imaginario = self.imaginario - otro.imaginario
        return Complejo(nuevo_real, nuevo_imaginario)

    def multiplicar(self, otro):
        nuevo_real = self.real * otro.real - self.imaginario * otro.imaginario
        nuevo_imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return Complejo(nuevo_real, nuevo_imaginario)

    def dividir(self, otro):
        divisor = otro.real**2 + otro.imaginario**2
        nuevo_real = (self.real * otro.real + self.imaginario * otro.imaginario) / divisor
        nuevo_imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / divisor
        return Complejo(nuevo_real, nuevo_imaginario)

# Ejemplo de uso
c1 = Complejo(2, 3)
c2 = Complejo(4, -5)

suma = c1.sumar(c2)
print(f"Suma: {suma}")

resta = c1.restar(c2)
print(f"Resta: {resta}")

multiplicacion = c1.multiplicar(c2)
print(f"Multiplicación: {multiplicacion}")

division = c1.dividir(c2)
print(f"División: {division}")





#5. En un banco tienen clientes que pueden hacer depósitos y extracciones 
#de dinero. El banco requiere también al final del día calcular la cantidad 
#de dinero que se ha depositado. Se deberán crear dos clases, la clase 
#cliente y la clase banco. La clase cliente tendrá los atributos nombre y 
#cantidad y los métodos __init__, depositar, extraer, mostrar_total. La clase 
#banco tendrá como atributos 3 objetos de la clase cliente y los métodos 
#__init__, operar y deposito_total.

class Cliente:
    def __init__(self, nombre, cantidad=0):
        self.nombre = nombre
        self.cantidad = cantidad

    def depositar(self, monto):
        self.cantidad += monto

    def extraer(self, monto):
        if monto <= self.cantidad:
            self.cantidad -= monto
        else:
            print("Fondos insuficientes")

    def mostrar_total(self):
        print(f"Cliente: {self.nombre}, Balance total: {self.cantidad}")


class Banco:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def operar(self, nombre_cliente, monto, operacion):
        cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)
        if cliente:
            if operacion == "depositar":
                cliente.depositar(monto)
            elif operacion == "extraer":
                cliente.extraer(monto)
        else:
            print(f"No se encontró el cliente con nombre {nombre_cliente}")

    def deposito_total(self):
        total = sum(cliente.cantidad for cliente in self.clientes)
        print(f"El total depositado en el banco es: {total}")


# Creación de objetos Cliente
cliente1 = Cliente("Juan", 100)
cliente2 = Cliente("Ana", 150)
cliente3 = Cliente("Pedro", 200)

# Creación del objeto Banco y agregación de clientes
banco = Banco()
banco.agregar_cliente(cliente1)
banco.agregar_cliente(cliente2)
banco.agregar_cliente(cliente3)

# Operaciones
banco.operar("Juan", 50, "depositar")
banco.operar("Ana", 75, "extraer")
banco.operar("Pedro", 100, "depositar")

# Mostrar el total de cada cliente
cliente1.mostrar_total()
cliente2.mostrar_total()
cliente3.mostrar_total()

# Mostrar el deposito total en el banco
banco.deposito_total()




#6.Desarrollar un programa que conste de una clase padre Cuenta y dos 
#subclases PlazoFijo y CajaAhorro. Definir los atributos titular y cantidad y 
#un método para imprimir los datos en la clase Cuenta. La clase 
#CajaAhorro tendrá un método para heredar los datos y uno para mostrar 
#la información. La clase PlazoFijo tendrá dos atributos propios, plazo e 
#interés. Tendrá un método para obtener el importe del interés 
#(cantidad*interés/100) y otro método para mostrar la información, datos 
#del titular plazo, interés y total de interés. Crear al menos un objeto de 
#cada subclase.

class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def imprimir_datos(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")

class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)

    def mostrar_informacion(self):
        print("Información de la Caja de Ahorro:")
        super().imprimir_datos()

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def importe_interes(self):
        return self.cantidad * self.interes / 100

    def mostrar_informacion(self):
        print("Información del Plazo Fijo:")
        super().imprimir_datos()
        print(f"Plazo: {self.plazo}")
        print(f"Interés: {self.interes}%")
        print(f"Total de interés: {self.importe_interes()}")

# Creación de objetos de cada subclase
cuenta_ahorro = CajaAhorro("Juan Pérez", 1500)
cuenta_plazofijo = PlazoFijo("Ana Gómez", 2000, 12, 4)

# Mostrar la información de cada cuenta
cuenta_ahorro.mostrar_informacion()
print("----------")
cuenta_plazofijo.mostrar_informacion()





#CICLO WHILE
#7.Escribir un programa que solicite ingresar la nota de 10 alumnos, el 
#programa debe informar de cuantos han aprobado y cuantos han 
#suspendido.

# Inicializamos los contadores para aprobados y suspendidos
aprobados = 0
suspendidos = 0

# Variable para llevar el control de los alumnos ingresados
alumnos_ingresados = 0

# Ciclo while para solicitar las notas de los alumnos
while alumnos_ingresados < 10:
    nota = float(input(f"Ingrese la nota del alumno {alumnos_ingresados + 1}: "))

    # Verificamos si la nota es válida (entre 0 y 10)
    if 0 <= nota <= 10:
        if nota >= 5:
            aprobados += 1
        else:
            suspendidos += 1
        alumnos_ingresados += 1
    else:
        print("Nota inválida. Intente nuevamente.")

# Mostramos el resultado
print("Resultados:")
print(f"Aprobados: {aprobados}")
print(f"Suspendidos: {suspendidos}")





#8. En una empresa trabajan n empleados cuyos sueldos oscilan entre 100 y 
#1000. Realizar un programa que informe de cuantos empleados cobran 
#menos de 500 y cuantos más de 500. Informar también del total que 
#gasta la empresa en pagar a sus empleados.

# Inicializamos los contadores
menor_500 = 0
mayor_500 = 0
total_gasto = 0

# Variable para llevar el control de los empleados ingresados
empleados_ingresados = 0

# Ciclo while para solicitar los sueldos de los empleados
while True:
    sueldo = float(input(f"Ingrese el sueldo del empleado {empleados_ingresados + 1} (entre 100 y 1000): "))

    # Verificamos si el sueldo es válido (entre 100 y 1000)
    if 100 <= sueldo <= 1000:
        total_gasto += sueldo

        # Determinamos si el sueldo es menor o mayor a 500
        if sueldo < 500:
            menor_500 += 1
        else:
            mayor_500 += 1

        empleados_ingresados += 1

        # Preguntamos si se desea ingresar otro sueldo
        continuar = input("¿Desea ingresar otro sueldo? (s/n): ").lower()
        if continuar != 's':
            break
    else:
        print("Sueldo inválido. Intente nuevamente.")

# Mostramos los resultados
print("Resultados:")
print(f"Empleados que cobran menos de 500: {menor_500}")
print(f"Empleados que cobran más de 500: {mayor_500}")
print(f"Total gastado por la empresa: {total_gasto}")




#9. Escribir un programa que solicite ingresar la nota de 10 alumnos, el programa debe 
#informar de cuantos han aprobado y cuantos han suspendido.

# Inicializamos los contadores
aprobados = 0
suspendidos = 0
contador_alumnos = 0

# Ciclo while para ingresar las notas de los 10 alumnos
while contador_alumnos < 10:
    nota = float(input(f"Ingrese la nota del alumno {contador_alumnos + 1}: "))

    # Verificamos si el alumno aprobó o suspendió
    if nota >= 6.0:
        aprobados += 1
    else:
        suspendidos += 1

    # Incrementamos el contador de alumnos
    contador_alumnos += 1

# Mostramos los resultados
print("Resultados:")
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")


import random

def ingresar_entero(mensaje):
    # Función para solicitar un número entero al usuario
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def suma_ultimos_5_numeros():
    # Función para sumar los últimos 5 números ingresados por el usuario
    numeros = [ingresar_entero(f"Ingrese el número {i+1}: ") for i in range(10)]
    suma_ultimos_5 = sum(numeros[-5:])
    print(f"\nLa suma de los últimos 5 números ingresados es: {suma_ultimos_5}")

def tabla_multiplicar():
    # Función para mostrar la tabla de multiplicar de un número dado por el usuario
    numero = ingresar_entero("Ingrese un número del 1 al 10: ")
    print(f"\nTabla de multiplicar del {numero}:\n")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def contar_vocales():
    # Función para contar las vocales en una palabra o frase ingresada por el usuario
    string = input("\nIngrese una palabra o frase: ")
    vocales = "aeiouAEIOU"
    cantidad_vocales = sum(1 for caracter in string if caracter in vocales)
    print(f"\nEl texto ingresado tiene {cantidad_vocales} vocales.")

def adivinar_numero():
    # Función para jugar a adivinar un número generado aleatoriamente
    numero_aleatorio = random.randint(1, 100)
    intentos = 0
    while intentos < 5:
        intento = ingresar_entero("Intenta adivinar el número (entre 1 y 100): ")
        intentos += 1
        if intento < numero_aleatorio:
            print("El número es mayor.")
        elif intento > numero_aleatorio:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            return
    print(f"¡Lo siento! Ya no tienes más intentos. El número era: {numero_aleatorio}")

def puntos_cuadrantes():
    # Función para contar cuántos puntos ingresados están en cada cuadrante
    total_puntos = ingresar_entero("Ingrese el total de puntos a procesar: ")
    cuadrantes = [0, 0, 0, 0]  # Cuadrantes: I, II, III, IV
    for _ in range(total_puntos):
        x = ingresar_entero("Ingrese la coordenada x: ")
        y = ingresar_entero("Ingrese la coordenada y: ")
        if x > 0 and y > 0:
            cuadrantes[0] += 1  # Cuadrante I
        elif x < 0 and y > 0:
            cuadrantes[1] += 1  # Cuadrante II
        elif x < 0 and y < 0:
            cuadrantes[2] += 1  # Cuadrante III
        elif x > 0 and y < 0:
            cuadrantes[3] += 1  # Cuadrante IV
    print(f"\nPuntos en el cuadrante I: {cuadrantes[0]}")
    print(f"Puntos en el cuadrante II: {cuadrantes[1]}")
    print(f"Puntos en el cuadrante III: {cuadrantes[2]}")
    print(f"Puntos en el cuadrante IV: {cuadrantes[3]}")

def tipo_triangulos():
    # Función para determinar el tipo de triángulo según sus lados
    total_triangulos = ingresar_entero("Ingrese el total de triángulos a procesar: ")
    equilateros = 0
    isosceles = 0
    escalenos = 0
    for _ in range(total_triangulos):
        lado1 = ingresar_entero("Ingrese la longitud del primer lado: ")
        lado2 = ingresar_entero("Ingrese la longitud del segundo lado: ")
        lado3 = ingresar_entero("Ingrese la longitud del tercer lado: ")
        if lado1 == lado2 == lado3:
            equilateros += 1
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            isosceles += 1
        else:
            escalenos += 1
    print(f"\nTotal de triángulos equiláteros: {equilateros}")
    print(f"Total de triángulos isósceles: {isosceles}")
    print(f"Total de triángulos escalenos: {escalenos}")

def cuadrados_productos():
    # Función para mostrar el cuadrado de un número y el producto de dos números
    valor1 = ingresar_entero("Ingrese un valor entero: ")
    print(f"El cuadrado de {valor1} es: {valor1**2}")
    valor2 = ingresar_entero("Ingrese otro valor entero: ")
    producto = valor1 * valor2
    print(f"El producto de {valor1} y {valor2} es: {producto}")

def vocales_frase(frase):
    # Función para contar las vocales en una frase
    vocales = "aeiouAEIOU"
    cantidad_vocales = sum(1 for caracter in frase if caracter in vocales)
    return cantidad_vocales

def separar_numeros(lista_numeros):
    # Función para separar los números positivos de los negativos en una lista
    positivos = [num for num in lista_numeros if num > 0]
    negativos = [num for num in lista_numeros if num < 0]
    return positivos, negativos

def mayores_edad(edades):
    # Función para contar las personas mayores o iguales a 18 años
    mayores = sum(1 for edad in edades if edad >= 18)
    return mayores

def validar_usuario(nombre_usuario):
    # Función para validar un nombre de usuario según ciertos criterios
    if not 6 <= len(nombre_usuario) <= 12:
        return "El nombre de usuario debe contener entre 6 y 12 caracteres."
    if not nombre_usuario.isalnum():
        return "El nombre de usuario puede contener solo letras y números."
    return True

# Ejecutar las funciones
suma_ultimos_5_numeros()
tabla_multiplicar()
contar_vocales()
adivinar_numero()
puntos_cuadrantes()
tipo_triangulos()
cuadrados_productos()
vocales1 = vocales_frase("Esta es una frase de ejemplo")
vocales2 = vocales_frase("Otra frase diferente")
vocales3 = vocales_frase("Y una tercera frase")
print(f"\nVocales en la frase 1: {vocales1}")
print(f"Vocales en la frase 2: {vocales2}")
print(f"Vocales en la frase 3: {vocales3}")
numeros = [5, -3, 0, 8, -2, -7, 10, 4]
positivos, negativos = separar_numeros(numeros)
print("\nNúmeros positivos:", positivos)
print("Números negativos:", negativos)
edades = [20, 15, 30, 25, 18, 40, 12]
print("\nCantidad de personas mayores de 18 años:", mayores_edad(edades))
usuario = input("\nIngrese un nombre de usuario: ")
resultado_validacion = validar_usuario(usuario)
print(resultado_validacion)
