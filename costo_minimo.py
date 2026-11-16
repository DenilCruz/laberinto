import heapq


def costo_minimo(grafo, inicio, fin):
    """Camino de menor costo total entre 'inicio' y 'fin' (algoritmo de Dijkstra).

    Tiene en cuenta el peso de cada arista. Devuelve una tupla
    (camino, costo_total); si no hay camino, devuelve (None, float("inf")).
    """
    if not grafo.existe_vertice(inicio) or not grafo.existe_vertice(fin):
        raise ValueError("El vértice de inicio o de fin no existe en el grafo.")

    costos = {vertice: float("inf") for vertice in grafo.lista_de_vertices}
    costos[inicio] = 0
    procedencia = {}
    visitados = set()

    cola_de_prioridad = [(0, inicio)]

    while cola_de_prioridad:
        costo_actual, actual = heapq.heappop(cola_de_prioridad)

        if actual in visitados:
            continue
        visitados.add(actual)

        if actual == fin:
            break

        for vecino, peso in grafo.adyacentes_de_vertice(actual):
            nuevo_costo = costo_actual + peso
            if nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                procedencia[vecino] = actual
                heapq.heappush(cola_de_prioridad, (nuevo_costo, vecino))

    if costos[fin] == float("inf"):
        return None, float("inf")

    camino = [fin]
    while camino[-1] != inicio:
        camino.append(procedencia[camino[-1]])
    camino.reverse()

    return camino, costos[fin]
