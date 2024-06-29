# gestion_inventario.py

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __repr__(self):
        return f"{self.nombre} - Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, nombre):
        self.productos = [p for p in self.productos if p.nombre != nombre]

    def listar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)

def main():
    inventario = Inventario()
    while True:
        print("\n1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Listar Productos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == '3':
            inventario.listar_productos()
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
