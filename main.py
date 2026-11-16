"""
Demostración de un grafo ponderado normal (sin laberinto, sin pygame).
Todo se explica por consola: construcción del grafo y los distintos
algoritmos sobre él (BFS, DFS, camino más corto y costo mínimo).
"""

from grafo_pesado import GrafoPesado
from bfs import recorrido_bfs
from dfs import recorrido_dfs
from camino_mas_corto import camino_mas_corto
from costo_minimo import costo_minimo


def construir_grafo_de_ciudades():
    ciudades = ["Lima", "Arequipa", "Cusco", "Trujillo", "Piura", "Ica"]
    grafo = GrafoPesado(ciudades)

    # (origen, destino, costo/distancia)
    rutas = [
        ("Lima", "Trujillo", 7),
        ("Lima", "Ica", 3),
        ("Lima", "Arequipa", 10),
        ("Ica", "Arequipa", 6),
        ("Arequipa", "Cusco", 5),
        ("Trujillo", "Piura", 4),
        ("Cusco", "Piura", 20),
    ]
    for origen, destino, costo in rutas:
        grafo.insertar_arista(origen, destino, costo)

    return grafo


def explicar_grafo(grafo):
    print("=" * 60)
    print("GRAFO PONDERADO")
    print("=" * 60)
    print(grafo)

    print(f"Cantidad de vertices: {grafo.cantidad_de_vertices()}")
    print(f"Cantidad de aristas:  {grafo.cantidad_de_aristas()}")
    print()

    print("Adyacencias de cada vertice (vecino, peso):")
    for vertice in grafo.lista_de_vertices:
        print(f"  {vertice}: {grafo.adyacentes_de_vertice(vertice)}")
    print()


def explicar_bfs(grafo, inicio):
    print("=" * 60)
    print(f"BFS (recorrido en anchura) desde {inicio}")
    print("=" * 60)
    orden = recorrido_bfs(grafo, inicio)
    print("  " + " -> ".join(orden))
    print()


def explicar_dfs(grafo, inicio):
    print("=" * 60)
    print(f"DFS (recorrido en profundidad) desde {inicio}")
    print("=" * 60)
    orden = recorrido_dfs(grafo, inicio)
    print("  " + " -> ".join(orden))
    print()


def explicar_camino_mas_corto(grafo, inicio, fin):
    print("=" * 60)
    print(f"CAMINO MAS CORTO (menos saltos, sin pesos): {inicio} -> {fin}")
    print("=" * 60)
    camino = camino_mas_corto(grafo, inicio, fin)
    if camino is None:
        print(f"No existe un camino entre {inicio} y {fin}.")
    else:
        print("  " + " -> ".join(camino))
        print(f"  Cantidad de saltos: {len(camino) - 1}")
    print()


def explicar_costo_minimo(grafo, inicio, fin):
    print("=" * 60)
    print(f"COSTO MINIMO (Dijkstra, con pesos): {inicio} -> {fin}")
    print("=" * 60)
    camino, costo_total = costo_minimo(grafo, inicio, fin)
    if camino is None:
        print(f"No existe un camino entre {inicio} y {fin}.")
    else:
        print("  " + " -> ".join(camino))
        print(f"  Costo total: {costo_total}")
    print()


def main():
    grafo = construir_grafo_de_ciudades()

    explicar_grafo(grafo)
    explicar_bfs(grafo, "Lima")
    explicar_dfs(grafo, "Lima")
    explicar_camino_mas_corto(grafo, "Lima", "Piura")
    explicar_costo_minimo(grafo, "Lima", "Piura")


if __name__ == "__main__":
    main()
