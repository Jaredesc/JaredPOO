import numpy as np

data_np = np.array([1, 2, 3, "4", 5])
data_list = [1, "texto", False, 2.5, 9]

tuple_np = tuple(data_np)
tuple_list = tuple(data_list)

set_np = set(data_np)
set_list = set(data_list)

registro = {
    "nombre": "Carlos",
    "edad": 29,
    "activo": False,
    "saldo": 100.5,
    "edad": 31
}

print(tuple_np)
print(tuple_list)
print(set_np)
print(set_list)
print(registro)

data_list.append(100)
data_list.insert(2, 88)
data_list.extend(["extra", 77])
data_list.remove("texto")
print(data_list)

data_list.pop(3)
print(data_list)

info = {"a": "uno", "b": "dos", "c": "tres"}
print(info)

info = dict(a="uno", b="dos", c="tres")
print(info)
print(info["a"])
print(info.get("a"))
print(info.get("z"))

info["a"] = "modificado"
info["nuevo"] = "valor"
print(info)

del info["nuevo"]
print(info)

removido = info.pop("a")
print(removido)

print("b" in info)
print(info.values())
print(info.items())
print(info.keys())

info.update({"a": "uno de nuevo"})
print(info)

info.clear()
print(info)

conj1 = {1, 2, 3}
conj2 = {3, 4, 5}

print("Unión:", conj1 | conj2)
print("Intersección:", conj1 & conj2)
print("Diferencia A-B:", conj1 - conj2)
print("Diferencia B-A:", conj2 - conj1)
print("Diferencia simétrica:", conj1 ^ conj2)

grupo_a = {1, 2, 3}
grupo_b = {1, 2, 3, 4}
grupo_vacio = {}

print(type(grupo_vacio))
print("Es subconjunto:", grupo_a.issubset(grupo_b))
print("Es superconjunto:", grupo_b.issuperset(grupo_a))

grupo_a = {10, 20}
grupo_b = {30, 40}
print("Son disjuntos:", grupo_a.isdisjoint(grupo_b))

copia = grupo_a.copy()
print("Copia:", copia)

print("Tamaño:", len(grupo_a))
grupo_a.clear()
print("Vacio:", grupo_a)

conj_test = {5, 10, 15, 20, 25}
print("Original:", conj_test)

conj_test.add(30)
conj_test.add(10)
print("Con añadido:", conj_test)

conj_test.discard(15)
conj_test.discard(100)

try:
    conj_test.remove(999)
except KeyError:
    print("Elemento 999 no está en el conjunto.")

print("Contiene 10:", 10 in conj_test)
print("Contiene 50:", 50 in conj_test)
