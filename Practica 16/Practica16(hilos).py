import threading
from time import sleep
import asyncio

class hilo(threading.Thread):
    def __init__(self, nombre, intervalo):
        super().__init__()
        self.nombre = nombre
        self.intervalo = intervalo
    
    def run(self):
        print(f"El hilo {self.nombre} ha comenzado.")
        for i in range(5):
            print(f"El hilo {self.nombre} está en la iteración {i}.")
            sleep(self.intervalo)
        print(f"El hilo {self.nombre} ha terminado.")
async def tarea(nombre):
    print(f"El hilo {nombre} ha comenzado.")
    await asyncio.sleep(2)
    print(f"El hilo {nombre} ha terminado.")
async def main():
    await asyncio.gather(
        tarea("hilo1"),
        tarea("hilo2"),
        tarea("hilo3"))
asyncio.run(main())

hilo1 = hilo("hilo1", 2)
hilo2 = hilo("hilo2", 4)
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()