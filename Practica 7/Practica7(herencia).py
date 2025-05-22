class Coche:
    def __init__(self, marca, modelo):
        self.__marca = marca  
        self.__modelo = modelo  

    
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

mi_coche = Coche("Toyota", "Corolla")
print(mi_coche.get_marca())  
mi_coche.set_modelo("Camry")  
print(mi_coche.get_modelo())

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def describir(self):
        return f"Vehículo de marca: {self.marca}"

class Coche(Vehiculo):  
    def __init__(self, marca, modelo):
        super().__init__(marca)  
        self.modelo = modelo

    def describir(self):
        return f"Coche: {self.marca} {self.modelo}"

# Uso
mi_coche = Coche("Toyota", "Corolla")
print(mi_coche.describir())  # Método heredado y extendido


