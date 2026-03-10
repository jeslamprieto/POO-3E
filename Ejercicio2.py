## Clase estudiante
class estudiante():
    def __init__(self, nombre, apellido, edad, calificacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.calificacion = calificacion

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Calificacion: {self.calificacion}")

    def clasificacion(self):
        if self.calificacion >= 3.0:
            print("Aprobado")
        else:
            print("Reprobado")


estudiante1 = estudiante("pepito", "perez", 23, 4.0)
estudiante2 = estudiante("juanchito", "smith", 19, 1.0)

estudiante1.mostrar_info()
estudiante1.clasificacion()
print("---")
estudiante2.mostrar_info()
estudiante2.clasificacion()
