from enum import Enum

class Semana(Enum):
    LUNES = "Lunes"
    MARTES = "Martes"
    MIERCOLES = "Miércoles"
    JUEVES = "Jueves"
    VIERNES = "Viernes"
    SABADO = "Sábado"
    DOMINGO = "Domingo"

def es_dia_valido(nombre_dia):
    try:
        if type(nombre_dia) is not str:
            raise TypeError("Solo se permite texto como entrada.")

        dia_formateado = nombre_dia.capitalize()
        dias_validos = [d.value for d in Semana]

        if dia_formateado in dias_validos:
            print(f"Confirmado: {dia_formateado}")
        else:
            raise ValueError("Día no reconocido dentro de la semana.")
    
    except (TypeError, ValueError) as error:
        print(f"Error detectado: {error}")
    
    finally:
        print("Proceso finalizado.")

es_dia_valido("lunes")
es_dia_valido("Domingo")
es_dia_valido("invierno")
es_dia_valido(456)
