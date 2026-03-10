## Clase libro
class libro():
    def __init__(self, titulo, autor, numero_de_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas

    def mostrar_info(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Numero de paginas: {self.numero_de_paginas}")

    def actualizar_paginas(self, nuevo_numero):
        self.numero_de_paginas = nuevo_numero


libro1 = libro("Pinocho", "Gabriel Garcia Marquez", 471)
libro2 = libro("El principito", "Pepito Perez", 96)

libro1.mostrar_info()
print("---")
libro2.mostrar_info()
print("---")

# Actualizando paginas
opcion = input("Que libro deseas actualizar? (1/2): ")

if opcion == "1":
    nuevo_numero = int(input("Nuevo numero de paginas: "))
    libro1.actualizar_paginas(nuevo_numero)
    print("---")
    print("Libro actualizado:")
    libro1.mostrar_info()
elif opcion == "2":
    nuevo_numero = int(input("Nuevo numero de paginas: "))
    libro2.actualizar_paginas(nuevo_numero)
    print("---")
    print("Libro actualizado:")
    libro2.mostrar_info()
else:
    print("Opcion invalida.")
