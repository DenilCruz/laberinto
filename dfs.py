def recorrido_dfs(grafo, inicio):
    """Recorre el grafo en profundidad (DFS) a partir de 'inicio'.

    Devuelve la lista de vértices en el orden en que fueron visitados.
    """
    if not grafo.existe_vertice(inicio):
        raise ValueError(f"El vértice {inicio} no existe en el grafo.")

    visitados = set()
    pila = [inicio]
    orden_de_visita = []

    while pila:
        actual = pila.pop()
        if actual in visitados:
            continue

        visitados.add(actual)
        orden_de_visita.append(actual)

        vecinos = [vecino for vecino, _peso in grafo.adyacentes_de_vertice(actual)]
        for vecino in reversed(vecinos):
            if vecino not in visitados:
                pila.append(vecino)

    return orden_de_visita
