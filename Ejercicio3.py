## Clase Producto
class producto():
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        if self.stock >= cantidad:
            print(f"Hay disponibilidad de {cantidad} unidades de {self.nombre}")
        else:
            print(f"No hay suficiente stock. Stock actual: {self.stock}")

    def vender(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            print(f"Venta exitosa. Stock restante: {self.stock}")
        else:
            print(f"Falta de stock. Stock actual: {self.stock}")

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Stock actualizado. Stock actual: {self.stock}")


laptop = producto("Laptop", 1200, 10)
##Pruebas
print("--- Verificar 5 unidades ---")
laptop.verificar_disponibilidad(5)

print("--- Vender 3 unidades ---")
laptop.vender(3)

print("--- Verificar 8 unidades ---")
laptop.verificar_disponibilidad(8)

print("--- Intentar vender 8 unidades ---")
laptop.vender(8)

print("--- Reabastecer 10 unidades ---")
laptop.reabastecer(10)

print("--- Verificar 8 unidades ---")
laptop.verificar_disponibilidad(8)

print("--- Vender 8 unidades ---")
laptop.vender(8)
