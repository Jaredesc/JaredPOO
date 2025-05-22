import numpy as np

class VectorNumpy:
    def __init__(self, valores):
        self.datos = np.array(valores)

    def agregar(self, valor):
        self.datos = np.append(self.datos, valor)
        print(f"Arreglo actualizado: {self.datos}")

    def borrar(self, posicion):
        if 0 <= posicion < len(self.datos):
            self.datos = np.delete(self.datos, posicion)
            print(f"Arreglo actualizado: {self.datos}")
        else:
            print("Posición inválida.")

    def actualizar(self, posicion, valor):
        if 0 <= posicion < len(self.datos):
            self.datos[posicion] = valor
            print(f"Arreglo actualizado: {self.datos}")
        else:
            print("Posición inválida.")

class ListaSimple:
    def __init__(self):
        self.elementos = ['2', '4', '6']

    def agregarElemento(self, valor):
        self.elementos.append(valor)
        print(f"Lista actualizada: {self.elementos}")

    def eliminarElemento(self, posicion):
        if 0 <= posicion < len(self.elementos):
            eliminado = self.elementos.pop(posicion)
            print(f"Elemento '{eliminado}' eliminado. Lista actualizada: {self.elementos}")
        else:
            print("Posición inválida.")

    def modificarElemento(self, posicion, valor):
        if 0 <= posicion < len(self.elementos):
            self.elementos[posicion] = valor
            print(f"Lista actualizada: {self.elementos}")
        else:
            print("Posición inválida.")

vector = VectorNumpy([10, 20, 30])
lista = ListaSimple()

nuevo_valor = input("Introduce un valor para agregar: ")
lista.agregarElemento(nuevo_valor)
vector.agregar(nuevo_valor)

pos = int(input("Introduce el índice a eliminar: "))
lista.eliminarElemento(pos)
vector.borrar(pos)

nuevo_valor = input("Introduce el nuevo valor para modificar: ")
pos = int(input("Introduce el índice a modificar: "))
lista.modificarElemento(pos, nuevo_valor)
vector.actualizar(pos, nuevo_valor)
