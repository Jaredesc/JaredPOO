import json
import requests
class GestorJson:
    def __init__(self,arch):
        self.arch = arch
    
    def leerJson (self):
        try:
            with open(self.arch, "r") as f:
                return json.load(f)
        
        except FileNotFoundError:

            print("El archivo no existe")
            return None
        except json.JSONDecodeError:
            print(f"El archivo no es json")
            return {}
        
    def escribirJson(self, data):
        with open(self.arch, "w") as f:
            json.dump(data, f, indent=4)

    def modificarJson(self, llave, valor):
        with open(self.arch, "r") as f:
            data = self.leerJson()
            data[llave] = valor
            self.escribirJson(data)
    def obtenerPokemon(self, pokemon):
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
            response = requests.get(url)
            response.raise_for_status()
            datos = response.json()
            self.escribirJson(datos)
            print(f"Datos de {pokemon} guardados en {self.arch}")
        except requests.exceptions.HTTPError:
            print(f"El enlace no existe")
            return None
        except requests.exceptions.RequestException as e:
            print(F"No se pudo realizar la petición")

gjson = GestorJson("pokemon.json")
gjson.obtenerPokemon("pikachu")
pokemonInfo = gjson.leerJson()
habilidades = pokemonInfo["abilities"]
print("Habilidades:")
for habilidad in habilidades:
    print(habilidad["ability"]["name"])