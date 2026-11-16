from collections import deque


def camino_mas_corto(grafo, inicio, fin):
    """Camino con la menor cantidad de aristas entre 'inicio' y 'fin'.

    Ignora los pesos de las aristas (solo cuenta "saltos"); usa BFS.
    Devuelve la lista de vértices del camino, o None si no hay camino.
    """
    if not grafo.existe_vertice(inicio) or not grafo.existe_vertice(fin):
        raise ValueError("El vértice de inicio o de fin no existe en el grafo.")

    if inicio == fin:
        return [inicio]

    procedencia = {inicio: None}
    cola = deque([inicio])

    while cola:
        actual = cola.popleft()

        for vecino, _peso in grafo.adyacentes_de_vertice(actual):
            if vecino not in procedencia:
                procedencia[vecino] = actual

                if vecino == fin:
                    camino = [vecino]
                    while procedencia[camino[-1]] is not None:
                        camino.append(procedencia[camino[-1]])
                    camino.reverse()
                    return camino

                cola.append(vecino)

    return None
