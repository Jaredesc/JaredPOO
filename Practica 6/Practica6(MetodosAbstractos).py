from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class RectanguloEquilatero(FormaGeometrica):
    def __init__(self, medida_lado):
        self.lado = medida_lado

    def calcular_area(self):
        return self.lado * self.lado

class Disco(FormaGeometrica):
    def __init__(self, r):
        self.radio = r

    def calcular_area(self):
        return math.pi * self.radio ** 2

figura1 = RectanguloEquilatero(5)
figura2 = Disco(3)

print("El área del rectángulo equilátero es:", figura1.calcular_area())
print("El área del disco es:", round(figura2.calcular_area(), 4))
