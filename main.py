from sistema_reparto import Pedido, ListaEnlazadaPedidos, ColaPedidosEnlazada, ColaPedidosArreglo, ArbolBusquedaPedidos, Grafo

lista_pedidos = ListaEnlazadaPedidos()
arbol_pedidos = ArbolBusquedaPedidos()
grafo_zonas = Grafo()
cola_atencion = ColaPedidosEnlazada()  # cambiar por ColaPedidosArreglo() para la otra version

def registrar_pedido(id_pedido, cliente, zona, plato):
    pedido = Pedido(id_pedido, cliente, zona, plato)
    lista_pedidos.insertar(pedido)
    arbol_pedidos.insertar(pedido)
    cola_atencion.encolar(pedido)
    print(f"Registrado: {pedido}")

def cargar_datos_iniciales():
    registrar_pedido(101, "Ana", "Centro", "Bandeja paisa")
    registrar_pedido(102, "Luis", "Barrio Norte", "Ajiaco")
    registrar_pedido(103, "Marta", "Vereda Alta", "Sancocho")
    registrar_pedido(104, "Pedro", "Barrio Sur", "Empanadas")
    registrar_pedido(105, "Sofia", "Centro", "Arepas")
    grafo_zonas.agregar_conexion("Centro", "Barrio Norte")
    grafo_zonas.agregar_conexion("Centro", "Barrio Sur")
    grafo_zonas.agregar_conexion("Barrio Norte", "Vereda Alta")
    grafo_zonas.agregar_conexion("Barrio Sur", "Urbanizacion El Roble")

def demostracion():
    print("\nCaso normal: registrar y atender un pedido")
    registrar_pedido(106, "Carlos", "Vereda Alta", "Tamal")
    print("Atendido:", cola_atencion.atender())
    print("\nCaso limite: buscar clave que no existe ->", arbol_pedidos.buscar(999))
    arbol_pedidos.insertar(Pedido(101, "Otro", "Centro", "Otro plato"))
    print("Caso limite: clave repetida, sigue igual ->", arbol_pedidos.buscar(101))
    lp = ListaEnlazadaPedidos()
    lp.insertar(Pedido(1, "Unico", "Centro", "Test"))
    lp.eliminar(1)
    print("Caso limite: lista vacia tras eliminar su unico elemento ->", lp.esta_vacia())
    cp = ColaPedidosEnlazada()
    print("Caso limite: atender con cola vacia ->", cp.atender())
    ca = ColaPedidosArreglo(capacidad=2)
    ca.encolar(Pedido(1, "A", "Centro", "X"))
    ca.encolar(Pedido(2, "B", "Centro", "Y"))
    print("Caso limite: encolar con cola llena ->", ca.encolar(Pedido(3, "C", "Centro", "Z")))
    print("\nListado ordenado por id (inorden):")
    for p in arbol_pedidos.inorden(): print(p)
    print("\nGrafo - vecinos y grado de Centro:", grafo_zonas.vecinos("Centro"), grafo_zonas.grado("Centro"))
    print("Centro y Vereda Alta conectados directo:", grafo_zonas.conectados_directamente("Centro", "Vereda Alta"))

def menu():
    print("\n1.Registrar 2.Buscar 3.Eliminar 4.Listar 5.Listar ordenado 6.Atender 7.Vecinos 8.Conexion 9.Demo 10.Salir")

def main():
    cargar_datos_iniciales()
    opcion = 0
    while opcion != 10:
        menu()
        opcion = int(input("Opcion: "))
        if opcion == 1: registrar_pedido(int(input("Id: ")), input("Cliente: "), input("Zona: "), input("Plato: "))
        elif opcion == 2: print(arbol_pedidos.buscar(int(input("Id: "))))
        elif opcion == 3: print("Eliminado" if lista_pedidos.eliminar(int(input("Id: "))) else "No existe")
        elif opcion == 4:
            for p in lista_pedidos.recorrer(): print(p)
        elif opcion == 5:
            for p in arbol_pedidos.inorden(): print(p)
        elif opcion == 6: print(cola_atencion.atender())
        elif opcion == 7:
            z = input("Zona: ")
            print("Vecinos:", grafo_zonas.vecinos(z), "Grado:", grafo_zonas.grado(z))
        elif opcion == 8: print(grafo_zonas.conectados_directamente(input("Zona 1: "), input("Zona 2: ")))
        elif opcion == 9: demostracion()

if __name__ == "__main__":
    main()
