## Guardians of the Ancient Kingdom

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa
        self.recarga = 0

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, nueva_vida):
        if nueva_vida < 0:
            self.__vida = 0
        elif nueva_vida > 100:
            self.__vida = 100
        else:
            self.__vida = nueva_vida

    @property
    def ataque(self):
        return self.__ataque

    @property
    def defensa(self):
        return self.__defensa

    def esta_vivo(self):
        return self.__vida > 0

    def ataque_basico(self, objetivo):
        daño = self.ataque - objetivo.defensa
        if daño > 0:
            objetivo.vida -= daño
            print(f"{self.nombre} usa ataque basico! Daño: {daño:.1f}")
        else:
            print(f"{self.nombre} usa ataque basico pero {objetivo.nombre} bloquea el golpe!")

    def atacar(self, objetivo):
        pass

    def elegir_ataque(self, objetivo):
        if self.recarga > 0:
            print(f"Habilidad especial en recarga ({self.recarga} turno(s) restante(s)), se usa ataque basico.")
            self.ataque_basico(objetivo)
            self.recarga -= 1
        else:
            print("Elige tu ataque:")
            print("1. Ataque basico")
            print("2. Habilidad especial")
            opcion = input("Opcion: ")
            if opcion == "1":
                self.ataque_basico(objetivo)
            elif opcion == "2":
                self.atacar(objetivo)
                self.recarga = 2
            else:
                print("Opcion invalida, se usa ataque basico.")
                self.ataque_basico(objetivo)


## Clases hijas

class Guerrero(Personaje):
    def atacar(self, objetivo):
        daño = (self.ataque * 1.2) - objetivo.defensa
        if daño > 0:
            objetivo.vida -= daño
            print(f"{self.nombre} usa Golpe Poderoso! Daño: {daño:.1f}")
        else:
            print(f"{self.nombre} usa Golpe Poderoso pero {objetivo.nombre} bloquea el golpe!")


class Mago(Personaje):
    def atacar(self, objetivo):
        daño = self.ataque
        objetivo.vida -= daño
        print(f"{self.nombre} lanza Hechizo! Daño: {daño} (ignora defensa)")


class Arquero(Personaje):
    def atacar(self, objetivo):
        if self.ataque > objetivo.defensa:
            daño = (self.ataque - objetivo.defensa) * 2
            print(f"{self.nombre} usa Tiro Preciso! Daño: {daño}")
        else:
            daño = 0
            print(f"{self.nombre} usa Tiro Preciso pero no causa daño!")
        objetivo.vida -= daño


## Juego

def bienvenida():
    print("=" * 50)
    print("   GUARDIANS OF THE ANCIENT KINGDOM")
    print("=" * 50)
    print("\nBienvenido, valiente guerrero...")
    print("Legendarios heroes se enfrentan hoy")
    print("en el campo de batalla del Reino Antiguo.")
    print("\nElige a tus campeones y que comience")
    print("la batalla por la gloria eterna!")
    print("\n" + "=" * 50)
    input("\nPresiona Enter para continuar...")


def mostrar_estado(p1, p2):
    print(f"  {p1.nombre}: {p1.vida:.1f} HP  |  {p2.nombre}: {p2.vida:.1f} HP")
    print("-" * 45)

def batalla(p1, p2):
    print(f"\n=== BATALLA: {p1.nombre} vs {p2.nombre} ===\n")
    turno = 1
    while p1.esta_vivo() and p2.esta_vivo():
        print(f"\nTurno {turno}:")

        print(f"\nTurno de {p1.nombre}:")
        p1.elegir_ataque(p2)
        mostrar_estado(p1, p2)
        if not p2.esta_vivo():
            break

        print(f"\nTurno de {p2.nombre}:")
        p2.elegir_ataque(p1)
        mostrar_estado(p1, p2)
        turno += 1

    if p1.esta_vivo():
        print(f"\n{p1.nombre} GANA la batalla!")
    else:
        print(f"\n{p2.nombre} GANA la batalla!")


## Crear personajes
guerrero = Guerrero("Atlas", 100, 30, 20)
mago = Mago("Gandalf", 80, 40, 10)
arquero = Arquero("Hawkeye", 90, 35, 15)

## Bienvenida
bienvenida()

## Seleccion de personajes
print("\nSelecciona el primer personaje:")
print("1. Atlas   (Guerrero) - Vida: 100, Ataque: 30, Defensa: 20")
print("2. Gandalf (Mago)     - Vida: 80,  Ataque: 40, Defensa: 10")
print("3. Hawkeye (Arquero)  - Vida: 90,  Ataque: 35, Defensa: 15")

personajes = {"1": guerrero, "2": mago, "3": arquero}

opcion1 = input("Opcion: ")
while opcion1 not in personajes:
    opcion1 = input("Opcion invalida. Elige 1, 2 o 3: ")

print("\nSelecciona el segundo personaje:")
for key, p in personajes.items():
    if key != opcion1:
        print(f"{key}. {p.nombre}")

opcion2 = input("Opcion: ")
while opcion2 not in personajes or opcion2 == opcion1:
    opcion2 = input("Opcion invalida o mismo personaje. Elige otro: ")

batalla(personajes[opcion1], personajes[opcion2])