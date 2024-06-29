import sys

print("\nMenú:")
print("1. Programa 1: Trabajo con objetos Persona")
print("2. Programa 2: Operaciones de una Cuenta")
print("3. Programa 3: Operaciones con Fracciones")
print("4. Programa 4: Operaciones con Números Complejos")
print("5. Programa 5: Banco y Clientes")
print("6. Programa 6: Clases Cuenta y Caja de Ahorro")
print("7. Programa 7: Conteo de aprobados y suspendidos")
print("8. Programa 8: Conteo de empleados por sueldo")
print("9. Programa 9: Suma de los últimos 5 números ingresados")
print("10. Programa 10: Tabla de multiplicar")
print("11. Programa 11: Cuadrantes de un plano cartesiano")
print("12. Programa 12: Tipo de triángulo")
print("13. Programa 13: Funciones y operaciones numéricas")
print("14. Programa 14: Conteo de vocales en un string")
print("15. Programa 15: Separación de valores positivos y negativos")
print("16. Programa 16: Conteo de personas mayores de edad")
print("17. Programa 17: Información de un string")
print("18. Programa 18: Validación de nombres de usuarios")
print("19. Programa 19: Juego de adivinanza")
print("20. Salir")

numero_programa = int(input("\nIntroduzca la opción: "))


#Primera parte Gilberto Hernandez

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

def Programa1():
    class Persona:
        def __init__(self, nombre, apellidos, edad, casado, numeroDocumentoIdentidad):
            self.nombre = nombre
            self.apellidos = apellidos
            self.edad = edad
            self.casado = casado
            self.numeroDocumentoIdentidad = numeroDocumentoIdentidad
    
        # Métodos para establecer y obtener los valores de los atributos
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
    
        # Métodos de acciones por profesión
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

def Programa2():
    class Cuenta:
        def __init__(self, titular="Desconocido", saldo=0.0):
            # Constructor para inicializar la cuenta con el titular y saldo
            self.titular = titular
            self.saldo = saldo

        def mostrar(self):
            # Método para mostrar la información de la cuenta
            print(f"Titular: {self.titular}, Saldo: {self.saldo:.2f}")

        def ingresar(self, cantidad):
            # Método para realizar un ingreso en la cuenta
            if cantidad > 0:
                self.saldo += cantidad
                print(f"Ingresaste {cantidad:.2f}. Saldo actual: {self.saldo:.2f}")
            else:
                print("Cantidad inválida para ingreso.")

        def reintegro(self, cantidad):
            # Método para realizar un reintegro de la cuenta
            if 0 < cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Reintegraste {cantidad:.2f}. Saldo actual: {self.saldo:.2f}")
            else:
                print("Cantidad inválida para reintegro.")

        def transferencia(self, cuenta_destino, cantidad):
            # Método para realizar una transferencia a otra cuenta
            if 0 < cantidad <= self.saldo:
                self.saldo -= cantidad
                cuenta_destino.saldo += cantidad
                print(f"Transferiste {cantidad:.2f} a {cuenta_destino.titular}. Tu saldo: {self.saldo:.2f}. Saldo destinatario: {cuenta_destino.saldo:.2f}")
            else:
                print("Cantidad inválida para transferencia.")

    # Ejemplo de uso
    cuenta1 = Cuenta("Juan Perez", 1000)
    cuenta2 = Cuenta("Ana López", 500)

    print("Estado inicial:")
    cuenta1.mostrar()
    cuenta2.mostrar()

    print("\nOperaciones realizadas:")
    cuenta1.ingresar(500)
    cuenta1.reintegro(200)
    cuenta1.transferencia(cuenta2, 300)

    print("\nEstado final:")
    cuenta1.mostrar()
    cuenta2.mostrar()






#3.Crea una clase Fracción con métodos para sumar, restar, multiplicar y 
#dividir fracciones.

def Programa3():
    from math import gcd

    class Fraccion:
        def __init__(self, numerador, denominador):
            # Constructor de la clase Fracción
            self.numerador = numerador
            self.denominador = denominador
            self.simplificar()  # Simplificar la fracción después de la creación
    
        def simplificar(self):
            # Método para simplificar la fracción
            divisor_comun = gcd(self.numerador, self.denominador)
            self.numerador //= divisor_comun
            self.denominador //= divisor_comun

        def __str__(self):
            # Método especial para representar la fracción como cadena
            return f"{self.numerador}/{self.denominador}"

        def sumar(self, otra):
            # Método para sumar fracciones
            nuevo_numerador = self.numerador * otra.denominador + otra.numerador * self.denominador
            nuevo_denominador = self.denominador * otra.denominador
            return Fraccion(nuevo_numerador, nuevo_denominador)

        def restar(self, otra):
            # Método para restar fracciones
            nuevo_numerador = self.numerador * otra.denominador - otra.numerador * self.denominador
            nuevo_denominador = self.denominador * otra.denominador
            return Fraccion(nuevo_numerador, nuevo_denominador)

        def multiplicar(self, otra):
            # Método para multiplicar fracciones
            return Fraccion(self.numerador * otra.numerador, self.denominador * otra.denominador)

        def dividir(self, otra):
            # Método para dividir fracciones
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






#4.Crea una clase Complejo con métodos para sumar, restar, multiplicar y 
#dividir números complejos.

def Programa4():
    class Complejo:
        def __init__(self, real, imaginario):
            # Constructor de la clase Complejo
            self.real = real
            self.imaginario = imaginario

        def __str__(self):
            # Método especial para representar el número complejo como cadena
            return f"{self.real} + {self.imaginario}i"

        def sumar(self, otro):
            # Método para sumar números complejos
            nuevo_real = self.real + otro.real
            nuevo_imaginario = self.imaginario + otro.imaginario
            return Complejo(nuevo_real, nuevo_imaginario)

        def restar(self, otro):
            # Método para restar números complejos
            nuevo_real = self.real - otro.real
            nuevo_imaginario = self.imaginario - otro.imaginario
            return Complejo(nuevo_real, nuevo_imaginario)

        def multiplicar(self, otro):
            # Método para multiplicar números complejos
            nuevo_real = self.real * otro.real - self.imaginario * otro.imaginario
            nuevo_imaginario = self.real * otro.imaginario + self.imaginario * otro.real
            return Complejo(nuevo_real, nuevo_imaginario)

        def dividir(self, otro):
            # Método para dividir números complejos
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

def Programa5():
    class Cliente:
        def __init__(self, nombre, cantidad=0):
            # Constructor de la clase Cliente
            self.nombre = nombre
            self.cantidad = cantidad

        def depositar(self, monto):
            # Método para depositar dinero
            self.cantidad += monto

        def extraer(self, monto):
            # Método para extraer dinero
            if monto <= self.cantidad:
                self.cantidad -= monto
            else:
                print("Fondos insuficientes")

        def mostrar_total(self):
            # Método para mostrar el balance total del cliente
            print(f"Cliente: {self.nombre}, Balance total: {self.cantidad}")


    class Banco:
        def __init__(self):
            # Constructor de la clase Banco
            self.clientes = []

        def agregar_cliente(self, cliente):
            # Método para agregar un cliente al banco
            self.clientes.append(cliente)

        def operar(self, nombre_cliente, monto, operacion):
            # Método para realizar operaciones (depositar o extraer) en un cliente
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)
            if cliente:
                if operacion == "depositar":
                    cliente.depositar(monto)
                elif operacion == "extraer":
                    cliente.extraer(monto)
            else:
                print(f"No se encontró el cliente con nombre {nombre_cliente}")

        def deposito_total(self):
            # Método para calcular y mostrar el total depositado en el banco
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

    # Mostrar el depósito total en el banco
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

def Programa6():
    class Cuenta:
        def __init__(self, titular, cantidad):
            # Constructor de la clase Cuenta
            self.titular = titular
            self.cantidad = cantidad

        def imprimir_datos(self):
            # Método para imprimir los datos de la cuenta
            print(f"Titular: {self.titular}")
            print(f"Cantidad: {self.cantidad}")

    class CajaAhorro(Cuenta):
        def __init__(self, titular, cantidad):
            # Constructor de la clase CajaAhorro, heredando de la clase Cuenta
            super().__init__(titular, cantidad)

        def mostrar_informacion(self):
            # Método para mostrar información específica de la Caja de Ahorro
            print("Información de la Caja de Ahorro:")
            super().imprimir_datos()

    class PlazoFijo(Cuenta):
        def __init__(self, titular, cantidad, plazo, interes):
            # Constructor de la clase PlazoFijo, heredando de la clase Cuenta
            super().__init__(titular, cantidad)
            self.plazo = plazo
            self.interes = interes

        def importe_interes(self):
            # Método para calcular el importe del interés
            return self.cantidad * self.interes / 100

        def mostrar_informacion(self):
            # Método para mostrar información específica del Plazo Fijo
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

def Programa7():
    # Inicializamos los contadores para aprobados y suspendidos
    aprobados = 0
    suspendidos = 0

    # Variable para llevar el control de los alumnos ingresados
    alumnos_ingresados = 0

    # Ciclo while para solicitar las notas de los alumnos
    while alumnos_ingresados < 10:
        # Solicitar la nota del alumno
        nota = float(input(f"Ingrese la nota del alumno {alumnos_ingresados + 1}: "))

        # Verificar si la nota es válida (entre 0 y 10)
        if 0 <= nota <= 10:
            # Incrementar el contador correspondiente (aprobados o suspendidos)
            if nota >= 5:
                aprobados += 1
            else:
                suspendidos += 1
            alumnos_ingresados += 1
        else:
            print("Nota inválida. Intente nuevamente.")

    # Mostrar el resultado
    print("Resultados:")
    print(f"Aprobados: {aprobados}")
    print(f"Suspendidos: {suspendidos}")






#8. En una empresa trabajan n empleados cuyos sueldos oscilan entre 100 y 
#1000. Realizar un programa que informe de cuantos empleados cobran 
#menos de 500 y cuantos más de 500. Informar también del total que 
#gasta la empresa en pagar a sus empleados.

def Programa8():
    # Inicializamos los contadores
    menor_500 = 0
    mayor_500 = 0
    total_gasto = 0

    # Variable para llevar el control de los empleados ingresados
    empleados_ingresados = 0

    # Ciclo while para solicitar los sueldos de los empleados
    while True:
        # Solicitar el sueldo del empleado
        sueldo = float(input(f"Ingrese el sueldo del empleado {empleados_ingresados + 1} (entre 100 y 1000): "))

        # Verificar si el sueldo es válido (entre 100 y 1000)
        if 100 <= sueldo <= 1000:
            # Actualizar el total gastado por la empresa
            total_gasto += sueldo

            # Determinar si el sueldo es menor o mayor a 500
        if sueldo < 500:
            menor_500 += 1
        else:
            mayor_500 += 1

        empleados_ingresados += 1

        # Preguntar si se desea ingresar otro sueldo
        continuar = input("¿Desea ingresar otro sueldo? (s/n): ").lower()
        if continuar != 's':
            break
        else:
            print("Sueldo inválido. Intente nuevamente.")

    # Mostrar los resultados
    print("Resultados:")
    print(f"Empleados que cobran menos de 500: {menor_500}")
    print(f"Empleados que cobran más de 500: {mayor_500}")
    print(f"Total gastado por la empresa: {total_gasto}")





#9. Escribir un programa que solicite ingresar la nota de 10 alumnos, el programa debe 
#informar de cuantos han aprobado y cuantos han suspendido.

def Programa9():
    # Inicializamos los contadores para aprobados y suspendidos
    aprobados = 0
    suspendidos = 0

    # Variable para llevar el control de los alumnos ingresados
    alumnos_ingresados = 0

    # Ciclo while para solicitar las notas de los alumnos
    while alumnos_ingresados < 10:
        # Solicitar la nota del alumno
        nota = float(input(f"Ingrese la nota del alumno {alumnos_ingresados + 1}: "))

        # Verificar si la nota es válida (entre 0 y 10)
        if 0 <= nota <= 10:
            # Incrementar el contador correspondiente (aprobados o suspendidos)
            if nota >= 5:
                aprobados += 1
            else:
                suspendidos += 1
            alumnos_ingresados += 1
        else:
            print("Nota inválida. Intente nuevamente.")

    # Mostrar el resultado
    print("Resultados:")
    print(f"Aprobados: {aprobados}")
    print(f"Suspendidos: {suspendidos}")




#Segunda parte Gregoris De La Cruz




#CICLO FOR

#10. Desarrollar un programa que solicite la carga de 10 números e imprima la suma de 
#los últimos 5 valores ingresados.

def Programa10():
    suma_ultimos_cinco = 0

    for i in range(10):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        if i >= 5:
            suma_ultimos_cinco += numero

    print(f"La suma de los últimos 5 valores ingresados es: {suma_ultimos_cinco}")


#11. Realizar un programa que solicite la carga de un valor entero del 1 al 10. Mostrar 
#después la tabla de multiplicar de dicho número.

def Programa11():
    numero = int(input("Ingrese un número del 1 al 10: "))
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


#12. Realizar un programa que pida ingresar dos datos enteros (coordenadas x e y). Al 
#comenzar el programa se pedirá ingresar el total de puntos a procesar. Informar de 
#cuantos puntos se han ingresado en cada uno de los cuatro cuadrantes.

def Programa12():
    cuadrante_1 = cuadrante_2 = cuadrante_3 = cuadrante_4 = 0

    total_puntos = int(input("Ingrese el total de puntos a procesar: "))

    for _ in range(total_puntos):
        x = int(input("Ingrese coordenada x: "))
        y = int(input("Ingrese coordenada y: "))
    
        if x > 0 and y > 0:
            cuadrante_1 += 1
        elif x < 0 and y > 0:
            cuadrante_2 += 1
        elif x < 0 and y < 0:
            cuadrante_3 += 1
        elif x > 0 and y < 0:
            cuadrante_4 += 1

    print(f"Cuadrante 1: {cuadrante_1} puntos")
    print(f"Cuadrante 2: {cuadrante_2} puntos")
    print(f"Cuadrante 3: {cuadrante_3} puntos")
    print(f"Cuadrante 4: {cuadrante_4} puntos")


#13. Realizar un programa que lea los lados de n triángulos. Informar después de cada 
#triángulo si es equilátero (tres lados iguales), isósceles (dos lados iguales) o 
#escaleno (ningún lado igual). Informar después del total de triángulos de cada tipo.

def Programa13():
    def tipo_triangulo(lado1, lado2, lado3):
        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Isósceles"
        else:
            return "Escaleno"

    total_triangulos = int(input("Ingrese el total de triángulos: "))

    equilateros = isosceles = escalenos = 0

    for _ in range(total_triangulos):
        lado1 = float(input("Ingrese longitud del lado 1: "))
        lado2 = float(input("Ingrese longitud del lado 2: "))
        lado3 = float(input("Ingrese longitud del lado 3: "))
    
        tipo = tipo_triangulo(lado1, lado2, lado3)
    
        if tipo == "Equilátero":
            equilateros += 1
        elif tipo == "Isósceles":
            isosceles += 1
        else:
            escalenos += 1

    print(f"Total de triángulos equiláteros: {equilateros}")
    print(f"Total de triángulos isósceles: {isosceles}")
    print(f"Total de triángulos escalenos: {escalenos}")




#FUNCIONES

#14. Realizar un programa con dos funciones. La primera debe solicitar la carga de un 
#valor entero y mostrar el cuadrado de dicho valor. La segunda que solicite la carga 
#de dos valores y muestre el producto de los mismos. Deberán llamar a estas dos 
#funciones desde el bloque principal (Fuera de toda función, como en el ejemplo 
#realizado al principio de este tema).

def Programa14():
    def cuadrado(valor):
        return valor ** 2

    def producto(valor1, valor2):
        return valor1 * valor2

    numero = int(input("Ingrese un número: "))
    print(f"El cuadrado de {numero} es: {cuadrado(numero)}")

    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    print(f"El producto de {valor1} y {valor2} es: {producto(valor1, valor2)}")


#15. Realizar un programa que tenga una función que reciba un string como parámetro. 
#Debe mostrar la cantidad de vocales que tiene dicho string. Se deberá llamar 3 
#veces desde el bloque principal, con 3 strings diferentes.

def Programa15():
    def contar_vocales(cadena):
        vocales = "aeiouAEIOU"
        contador = sum(1 for letra in cadena if letra in vocales)
        return contador

    cadena1 = input("Ingrese la primera cadena: ")
    cadena2 = input("Ingrese la segunda cadena: ")
    cadena3 = input("Ingrese la tercera cadena: ")

    print(f"Cantidad de vocales en la primera cadena: {contar_vocales(cadena1)}")
    print(f"Cantidad de vocales en la segunda cadena: {contar_vocales(cadena2)}")
    print(f"Cantidad de vocales en la tercera cadena: {contar_vocales(cadena3)}")


#16. Realizar un programa que cargue una lista de n valores enteros. Generar dos listas, 
#una con valores negativos y otra con los valores positivos e imprimir ambas listas.

def Programa16():
    def separar_positivos_negativos(lista):
        positivos = [num for num in lista if num >= 0]
        negativos = [num for num in lista if num < 0]
        return positivos, negativos

    # Puedes ajustar esta lista según tus necesidades
    lista_valores = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]

    positivos, negativos = separar_positivos_negativos(lista_valores)

    print("Lista de valores positivos:", positivos)
    print("Lista de valores negativos:", negativos)


#17. Realizar un programa que reciba una serie de edades y retorne la cantidad de 
#personas con una edad igual o superior a 18 (como mínimo deben introducirse 3 
#valores enteros).

def Programa17():
    # Similar al problema anterior, pero adaptado para el caso de triángulos
    # Podrías reutilizar la función tipo_triangulo del problema 13

    total_triangulos = int(input("Ingrese el total de triángulos: "))
    tipo_triangulo = tipo_triangulo

    equilateros, isosceles, escalenos = [], [], []

    for _ in range(total_triangulos):
        lado1 = float(input("Ingrese longitud del lado 1: "))
        lado2 = float(input("Ingrese longitud del lado 2: "))
        lado3 = float(input("Ingrese longitud del lado 3: "))
    
        tipo = tipo_triangulo(lado1, lado2, lado3)
    
        if tipo == "Equilátero":
            equilateros.append((lado1, lado2, lado3))
        elif tipo == "Isósceles":
            isosceles.append((lado1, lado2, lado3))
        else:
            escalenos.append((lado1, lado2, lado3))

    print("Triángulos Equiláteros:", equilateros)
    print("Triángulos Isósceles:", isosceles)
    print("Triángulos Escalenos:", escalenos)




#SIMPLES

#18. Solicitar la carga por teclado de un string. Mostrar el total de caracteres del string y 
#utilizar las funciones explicadas anteriormente (upper, lower y capitalize).

def Programa18():
    cadena = input("Ingrese un string: ")
    print(f"Total de caracteres: {len(cadena)}")
    print(f"En mayúsculas: {cadena.upper()}")
    print(f"En minúsculas: {cadena.lower()}")
    print(f"Capitalizado: {cadena.capitalize()}")



#OTROS

#19. Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá 
#cumplir con los siguientes criterios de aceptación:
#El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo 
#de 12.
#El nombre de usuario debe ser alfanumérico.
#Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El 
#nombre de usuario debe contener al menos 6 caracteres".
#Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre 
#de usuario no puede contener más de 12 caracteres".
#Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el 
#mensaje "El nombre de usuario puede contener solo letras y números".
#Nombre de usuario válido, retorna True.

def Programa19():
    def validar_nombre_usuario(nombre_usuario):
        if len(nombre_usuario) < 6:
            return "El nombre de usuario debe contener al menos 6 caracteres"
        elif len(nombre_usuario) > 12:
            return "El nombre de usuario no puede contener más de 12 caracteres"
        elif not nombre_usuario.isalnum():
            return "El nombre de usuario puede contener solo letras y números"
        else:
            return True

    # Ejemplo de uso
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    resultado_validacion = validar_nombre_usuario(nombre_usuario)

    if resultado_validacion is True:
        print("Nombre de usuario válido.")
    else:
        print(resultado_validacion)


#20.Escribe un programa que almacene un número y pida al usuario 
#adivinarlo

def Programa20():
    import random

    numero_aleatorio = random.randint(1, 100)

    intentos = 0
    while True:
        intento_usuario = int(input("Adivina el número (entre 1 y 100): "))
        intentos += 1

        if intento_usuario == numero_aleatorio:
            print(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
            break
        elif intento_usuario < numero_aleatorio:
            print("Demasiado bajo. Intenta nuevamente.")
        else:
            print("Demasiado alto. Intenta nuevamente.")


match numero_programa:
    case 1:
        Programa1()
    case 2:
        Programa2()
    case 3:
        Programa3()
    case 4:
        Programa4()
    case 5:
        Programa5()
    case 6:
        Programa6()
    case 7:
        Programa7()
    case 8:
        Programa8()
    case 9:
        Programa10()
    case 10:
        Programa10()
    case 11:
        Programa11()
    case 12:
        Programa12()
    case 13:
        Programa13()
    case 14:
        Programa14()
    case 15:
        Programa15()
    case 16:
        Programa16()
    case 17:
        Programa17()
    case 18:
        Programa18()
    case 19:
        Programa19()
    case 20:
        Programa20()
    case any:
        sys.exit()


