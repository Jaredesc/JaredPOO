from abc import ABC, abstractmethod

class Individuo:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def obtener_nombre(self):
        return self.__nombre

    def actualizar_edad(self, edad_nueva):
        if edad_nueva > 0:
            self.__edad = edad_nueva

persona1 = Individuo("Luis", 30)
print(persona1.obtener_nombre())

class Criatura:
    def __init__(self, especie, tipo):
        self.especie = especie
        self.tipo = tipo

    def emitir_sonido(self):
        return "Sonido desconocido"

class Canino(Criatura):
    def emitir_sonido(self):
        return "Ladrido fuerte"

mascota = Canino("Rex", "Pastor Alemán")
print(mascota.especie)
print(mascota.emitir_sonido())
print(mascota.tipo)

def reproducir_sonido(animal):
    print(animal.emitir_sonido())

felino = Criatura("Michi", "Gato")
canino = Canino("Toby", "Beagle")

reproducir_sonido(felino)
reproducir_sonido(canino)

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Rectangulo(Forma):
    def __init__(self, medida):
        self.lado = medida

    def calcular_area(self):
        return self.lado ** 2

figura = Rectangulo(6)
print(figura.calcular_area())
