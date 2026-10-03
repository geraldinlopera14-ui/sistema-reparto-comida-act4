class Pedido:
    def __init__(self, id_pedido, cliente, zona, plato):
        self.__id = id_pedido
        self.__cliente = cliente
        self.__zona = zona
        self.__plato = plato
        self.__estado = "pendiente"
    def get_id(self): return self.__id
    def get_cliente(self): return self.__cliente
    def get_zona(self): return self.__zona
    def get_plato(self): return self.__plato
    def get_estado(self): return self.__estado
    def marcar_entregado(self): self.__estado = "entregado"
    def __str__(self): return f"#{self.__id} {self.__cliente} | {self.__zona} | {self.__plato} | {self.__estado}"


class NodoLista:
    def __init__(self, pedido):
        self.pedido = pedido
        self.siguiente = None

class ListaEnlazadaPedidos:  # simple: solo se recorre hacia adelante, no hace falta doble ni circular
    def __init__(self): self.cabeza = None
    def insertar(self, pedido):
        nuevo = NodoLista(pedido)
        if not self.cabeza: self.cabeza = nuevo; return
        actual = self.cabeza
        while actual.siguiente: actual = actual.siguiente
        actual.siguiente = nuevo
    def buscar(self, id_pedido):
        actual = self.cabeza
        while actual:
            if actual.pedido.get_id() == id_pedido: return actual.pedido
            actual = actual.siguiente
        return None
    def eliminar(self, id_pedido):
        actual, anterior = self.cabeza, None
        while actual:
            if actual.pedido.get_id() == id_pedido:
                if anterior: anterior.siguiente = actual.siguiente
                else: self.cabeza = actual.siguiente
                return True
            anterior, actual = actual, actual.siguiente
        return False
    def recorrer(self):
        r, actual = [], self.cabeza
        while actual: r.append(actual.pedido); actual = actual.siguiente
        return r
    def esta_vacia(self): return self.cabeza is None


class NodoCola:
    def __init__(self, pedido):
        self.pedido = pedido
        self.siguiente = None

class ColaPedidosEnlazada:
    def __init__(self): self.frente = self.final = None; self.cantidad = 0
    def encolar(self, pedido):
        nodo = NodoCola(pedido)
        if not self.frente: self.frente = self.final = nodo
        else: self.final.siguiente = nodo; self.final = nodo
        self.cantidad += 1
        return True
    def atender(self):
        if not self.frente: return None
        pedido = self.frente.pedido
        self.frente = self.frente.siguiente
        if not self.frente: self.final = None
        self.cantidad -= 1
        return pedido
    def esta_vacia(self): return self.frente is None
    def tamano(self): return self.cantidad


class ColaPedidosArreglo:  # mismo contrato que la de arriba, pero con arreglo fijo circular
    def __init__(self, capacidad=20):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.frente = self.final = self.cantidad = 0
    def encolar(self, pedido):
        if self.cantidad == self.capacidad: return False
        self.datos[self.final] = pedido
        self.final = (self.final + 1) % self.capacidad
        self.cantidad += 1
        return True
    def atender(self):
        if self.cantidad == 0: return None
        pedido = self.datos[self.frente]
        self.frente = (self.frente + 1) % self.capacidad
        self.cantidad -= 1
        return pedido
    def esta_vacia(self): return self.cantidad == 0
    def tamano(self): return self.cantidad


class NodoArbol:
    def __init__(self, pedido):
        self.pedido = pedido
        self.izquierdo = self.derecho = None

class ArbolBusquedaPedidos:
    def __init__(self): self.raiz = None
    def insertar(self, pedido): self.raiz = self._insertar(self.raiz, pedido)
    def _insertar(self, nodo, pedido):
        if not nodo: return NodoArbol(pedido)
        if pedido.get_id() < nodo.pedido.get_id(): nodo.izquierdo = self._insertar(nodo.izquierdo, pedido)
        elif pedido.get_id() > nodo.pedido.get_id(): nodo.derecho = self._insertar(nodo.derecho, pedido)
        return nodo
    def buscar(self, id_pedido): return self._buscar(self.raiz, id_pedido)
    def _buscar(self, nodo, id_pedido):
        if not nodo: return None
        if id_pedido == nodo.pedido.get_id(): return nodo.pedido
        if id_pedido < nodo.pedido.get_id(): return self._buscar(nodo.izquierdo, id_pedido)
        return self._buscar(nodo.derecho, id_pedido)
    def preorden(self): r = []; self._preorden(self.raiz, r); return r
    def _preorden(self, nodo, r):
        if nodo: r.append(nodo.pedido); self._preorden(nodo.izquierdo, r); self._preorden(nodo.derecho, r)
    def inorden(self): r = []; self._inorden(self.raiz, r); return r
    def _inorden(self, nodo, r):
        if nodo: self._inorden(nodo.izquierdo, r); r.append(nodo.pedido); self._inorden(nodo.derecho, r)
    def postorden(self): r = []; self._postorden(self.raiz, r); return r
    def _postorden(self, nodo, r):
        if nodo: self._postorden(nodo.izquierdo, r); self._postorden(nodo.derecho, r); r.append(nodo.pedido)
    def altura(self): return self._altura(self.raiz)
    def _altura(self, nodo):
        if not nodo: return -1
        return 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))


class Grafo:  # relacion no jerarquica: zonas conectadas por rutas de reparto
    def __init__(self): self.adyacencia = {}
    def agregar_zona(self, zona):
        if zona not in self.adyacencia: self.adyacencia[zona] = []
    def agregar_conexion(self, zona1, zona2):
        self.agregar_zona(zona1); self.agregar_zona(zona2)
        if zona2 not in self.adyacencia[zona1]: self.adyacencia[zona1].append(zona2)
        if zona1 not in self.adyacencia[zona2]: self.adyacencia[zona2].append(zona1)
    def vecinos(self, zona): return self.adyacencia.get(zona, [])
    def grado(self, zona): return len(self.adyacencia.get(zona, []))
    def conectados_directamente(self, zona1, zona2): return zona2 in self.adyacencia.get(zona1, [])
