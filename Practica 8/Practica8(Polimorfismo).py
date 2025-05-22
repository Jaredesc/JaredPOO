class Criatura:
    def emitir_sonido(self):
        pass

class Canino(Criatura):
    def emitir_sonido(self):
        return "Guau guau"

class Felino(Criatura):
    def emitir_sonido(self):
        return "Miau miau"

def reproducir_sonido(creatura):
    print(creatura.emitir_sonido())

animal1 = Canino()
animal2 = Felino()

reproducir_sonido(animal1)
reproducir_sonido(animal2)

