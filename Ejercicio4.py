## Clase Vehiculo
class vehiculo():
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        if self.velocidad_actual + incremento > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
            print(f"Velocidad maxima alcanzada: {self.velocidad_actual} km/h")
        else:
            self.velocidad_actual += incremento
            print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def frenar(self, decremento):
        if self.velocidad_actual - decremento < 0:
            self.velocidad_actual = 0
            print("El vehiculo esta detenido.")
        else:
            self.velocidad_actual -= decremento
            print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def verificar_limite(self):
        if self.velocidad_actual > self.velocidad_maxima:
            print(f"Velocidad excedida. Vas a {self.velocidad_actual} km/h y el limite es {self.velocidad_maxima} km/h")
        else:
            print(f"Velocidad dentro del limite. Vas a {self.velocidad_actual} km/h de {self.velocidad_maxima} km/h permitidos")


## Menu interactivo
auto = vehiculo("Toyota", "Corolla", 210)

while True:
    print("\n===== MENU =====")
    print(f"Velocidad actual: {auto.velocidad_actual} km/h")
    print("1. Acelerar")
    print("2. Frenar")
    print("3. Verificar limite")
    print("4. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        incremento = int(input("Cuanto deseas acelerar? (km/h): "))
        auto.acelerar(incremento)
    elif opcion == "2":
        decremento = int(input("Cuanto deseas frenar? (km/h): "))
        auto.frenar(decremento)
    elif opcion == "3":
        auto.verificar_limite()
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opcion invalida.")

        