class Cuadro:
    def areaCuadro(lado):
        area = lado * lado
        return area
    def perimetroCuadro(lado):
        perim = lado * 4
        return perim

lado = float(input("Ingrese la medida del lado: "))
print(f"Área del cuadro: {Cuadro.areaCuadro(lado)}")
print(f"Perímetro del cuadro: {Cuadro.perimetroCuadro(lado)}")