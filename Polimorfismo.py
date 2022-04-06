####Polimorfismo: pueden ser clases idénticas, pero sus acciones y funciones son diferentes
class Animales:
    def __init__(self,nombre):
        self.nombre = nombre

    def tipo_animal(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        print("Animal  salvaje")

class Perro(Animales):
    def tipo_animal(self):
        print("Animal doméstico")

#objetos
nuevo_animal = Leon("SIMBA")
nuevo_animal.tipo_animal()
print(nuevo_animal.nombre)


