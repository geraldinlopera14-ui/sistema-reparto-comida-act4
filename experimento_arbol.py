import random
from sistema_reparto import Pedido, ArbolBusquedaPedidos

claves = list(range(101, 116))  # 15 claves
random.seed(7)
desordenadas = claves.copy()
random.shuffle(desordenadas)
ordenadas = sorted(claves)

arbol_d = ArbolBusquedaPedidos()
arbol_o = ArbolBusquedaPedidos()

print(f"{'Cantidad':<10}{'Altura desordenado':<22}{'Altura ordenado'}")
for i in range(len(claves)):
    arbol_d.insertar(Pedido(desordenadas[i], "Cliente", "Zona", "Plato"))
    arbol_o.insertar(Pedido(ordenadas[i], "Cliente", "Zona", "Plato"))
    print(f"{i+1:<10}{arbol_d.altura():<22}{arbol_o.altura()}")
