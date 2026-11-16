from collections import deque


def recorrido_bfs(grafo, inicio):
    """Recorre el grafo en anchura (BFS) a partir de 'inicio'.

    Devuelve la lista de vértices en el orden en que fueron visitados.
    """
    if not grafo.existe_vertice(inicio):
        raise ValueError(f"El vértice {inicio} no existe en el grafo.")

    visitados = {inicio}
    cola = deque([inicio])
    orden_de_visita = []

    while cola:
        actual = cola.popleft()
        orden_de_visita.append(actual)

        for vecino, _peso in grafo.adyacentes_de_vertice(actual):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)

    return orden_de_visita
