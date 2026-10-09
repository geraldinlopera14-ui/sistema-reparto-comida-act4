[README 4.md](https://github.com/user-attachments/files/33012908/README.4.md)
# Sistema de Reparto de Comida a Domicilio

## 1. Nombre del sistema
Sistema de Reparto de Comida a Domicilio

## 2. Descripción no técnica del caso
Un negocio de comida preparada reparte pedidos a domicilio en el pueblo. Necesita anotar cada pedido, atenderlos en el orden en que llegaron, poder buscar uno rápido si el cliente pregunta, y saber qué zonas del pueblo están conectadas por las rutas de reparto para organizar mejor los recorridos.

## 3. Clases y estructura de cada componente

| Componente | Clases | Estructura |
|---|---|---|
| A - Registro y proceso | Pedido, NodoLista, ListaEnlazadaPedidos, NodoCola, ColaPedidosEnlazada | Lista enlazada simple + cola |
| B - Índice de búsqueda | NodoArbol, ArbolBusquedaPedidos | Árbol binario de búsqueda |
| C - Relaciones | Grafo | Grafo con listas de adyacencia |
| D - Un contrato, dos implementaciones | ColaPedidosEnlazada, ColaPedidosArreglo | Misma cola, una con nodos y otra con arreglo |

## 4. Por qué se eligió cada estructura
- Lista enlazada simple: solo hacía falta agregar pedidos, recorrerlos y buscarlos o borrarlos. No se necesitaba ir hacia atrás ni volver al inicio, así que no tenía sentido complicarla con una doble o una circular.
- Cola: los pedidos se atienden en el orden en que llegan, el primero que pide es el primero en recibir su comida.
- Árbol binario: permite encontrar un pedido por su número sin tener que revisarlos todos uno por uno, y de paso entrega la lista ya ordenada.
- Grafo: hay pocas zonas y pocas conexiones entre ellas, así que no tenía sentido guardar todas las combinaciones posibles, solo las que existen de verdad.

## 5. Comparación: cola con arreglo vs. cola con lista enlazada
Las dos hacen lo mismo (encolar y atender), pero de forma distinta por dentro. La de arreglo tiene un límite fijo de 20 pedidos esperando; si se llena, no deja agregar más. La de lista enlazada no tiene ese límite, va creciendo según haga falta. La de arreglo conviene cuando ya se sabe más o menos cuántos pedidos van a esperar; la de lista enlazada conviene cuando no se sabe.

## 6. Experimento: altura del árbol según el orden de los datos

| Cantidad de datos | Altura si se insertan en desorden | Altura si se insertan ya ordenados |
|---|---|---|
| 5 | 3 | 4 |
| 10 | 5 | 9 |
| 15 | 5 | 14 |

Cuando los datos entran ya ordenados, cada número nuevo es siempre más grande que los anteriores, entonces siempre se acomoda del mismo lado y el árbol termina pareciendo una fila torcida en vez de un árbol parejo. Por eso buscar algo ahí puede tardar hasta 14 pasos en vez de 5.

## 7. Dibujo de las rotaciones AVL
<img width="1536" height="2048" alt="image" src="https://github.com/user-attachments/assets/6b330b27-0ccf-4069-8c1e-18d718291337" />


## 8. Cómo ejecutar el programa
```bash
python main.py
python experimento_arbol.py
```

## 9. Pruebas que se hicieron (opción 9 del menú)
- Registrar y atender un pedido normal.
- Buscar un pedido que no existe.
- Intentar registrar un pedido con un número repetido.
- Eliminar el único pedido de una lista y dejarla vacía.
- Atender cuando no hay nadie en la fila.
- Llenar por completo la fila de arreglo e intentar agregar uno más.

## 10. Qué le falta al sistema
La fila con arreglo tiene un cupo fijo de 20 pedidos. Si se cierra el programa, se pierde todo lo registrado porque no queda guardado en ningún lado. El árbol tampoco se acomoda solo, así que si llegan muchos pedidos con números seguidos, buscar se vuelve más lento. Se podría mejorar guardando los pedidos en un archivo, y usando un árbol que se autobalancee.

## 11. Enlace al video
https://canva.link/w70mzocds2upzwv
