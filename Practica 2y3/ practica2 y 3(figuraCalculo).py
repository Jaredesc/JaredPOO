from math import pi, tan

class Poligono:
    
    def calcular_area(longitud_lado, cantidad_lados):
        return (cantidad_lados * (longitud_lado ** 2)) / (4 * tan(pi / cantidad_lados))

    def calcular_perimetro(longitud_lado, cantidad_lados):
        return longitud_lado * cantidad_lados

lados = int(input("¿Cuántos lados tiene el polígono?: "))
longitud = float(input("¿Cuál es la longitud de cada lado?: "))

if lados <= 2 or longitud <= 0:
    print("Los datos ingresados no corresponden a un polígono válido.")
else:
    area = Poligono.calcular_area(longitud, lados)
    perimetro = Poligono.calcular_perimetro(longitud, lados)
    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")
