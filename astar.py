import heapq

class AStar:
    def __init__(self, grafo, inicio, fin):
        self.grafo = grafo
        self.inicio = inicio
        self.fin = fin

    def heuristica(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def encontrar_camino(self):
        lista_abierta = []
        heapq.heappush(lista_abierta, (0, self.inicio))

        procedencia = {}
        costo_real = {vertice: float("inf") for vertice in self.grafo.lista_de_vertices}
        costo_estimado = {vertice: float("inf") for vertice in self.grafo.lista_de_vertices}

        costo_real[self.inicio] = 0
        costo_estimado[self.inicio] = self.heuristica(self.inicio, self.fin)

        while lista_abierta:
            _, actual = heapq.heappop(lista_abierta)

            if actual == self.fin:
                camino = [actual]
                while actual in procedencia:
                    actual = procedencia[actual]
                    camino.append(actual)
                camino.reverse()
                return camino

            for vecino, peso in self.grafo.adyacentes_de_vertice(actual):
                costo_tentativo = costo_real[actual] + peso
                if costo_tentativo < costo_real[vecino]:
                    procedencia[vecino] = actual
                    costo_real[vecino] = costo_tentativo
                    costo_estimado[vecino] = costo_tentativo + self.heuristica(vecino, self.fin)
                    heapq.heappush(lista_abierta, (costo_estimado[vecino], vecino))

        return None