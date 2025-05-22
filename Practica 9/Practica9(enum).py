from enum import Enum
class consecutivo(Enum):
    Lunes=1
    Martes=2
    miercoles=3

print(consecutivo.Lunes)
print(consecutivo.Lunes.value)
print(type(consecutivo.Lunes))
print(type(consecutivo.Lunes.value))