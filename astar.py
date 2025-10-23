import heapq

class AStar:
    def __init__(self, grafo, inicio, fin):
        self.grafo = grafo
        self.inicio = inicio
        self.fin = fin

    def heuristica(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def encontrar_camino(self):
        abiertos = []
        heapq.heappush(abiertos, (0, self.inicio))

        came_from = {}
        g_score = {v: float("inf") for v in self.grafo.listaDeVertices}
        f_score = {v: float("inf") for v in self.grafo.listaDeVertices}

        g_score[self.inicio] = 0
        f_score[self.inicio] = self.heuristica(self.inicio, self.fin)

        while abiertos:
            _, actual = heapq.heappop(abiertos)

            if actual == self.fin:
                # Reconstruir camino óptimo
                camino = [actual]
                while actual in came_from:
                    actual = came_from[actual]
                    camino.append(actual)
                camino.reverse()
                return camino

            for vecino in self.grafo.adyacentesDeVertice(actual):
                tentative_g = g_score[actual] + 1  # Cada paso cuesta 1
                if tentative_g < g_score[vecino]:
                    came_from[vecino] = actual
                    g_score[vecino] = tentative_g
                    f_score[vecino] = tentative_g + self.heuristica(vecino, self.fin)
                    heapq.heappush(abiertos, (f_score[vecino], vecino))

        return None  # No hay camino
