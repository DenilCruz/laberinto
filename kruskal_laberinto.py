import random

class ConjuntoDisjunto:
    def __init__(self, elementos):
        self.padre = {e: e for e in elementos}
        self.rango = {e: 0 for e in elementos}

    def encontrar_raiz(self, e):
        if self.padre[e] != e:
            self.padre[e] = self.encontrar_raiz(self.padre[e])
        return self.padre[e]

    def unir(self, a, b):
        ra = self.encontrar_raiz(a)
        rb = self.encontrar_raiz(b)
        if ra == rb:
            return False
        if self.rango[ra] < self.rango[rb]:
            self.padre[ra] = rb
        elif self.rango[ra] > self.rango[rb]:
            self.padre[rb] = ra
        else:
            self.padre[rb] = ra
            self.rango[ra] += 1
        return True


def generar_laberinto_kruskal(grafo, ancho, alto):

    celdas = [(x, y) for x in range(0, alto, 2) for y in range(0, ancho, 2)]
    paredes = []


    for x, y in celdas:
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < alto and 0 <= ny < ancho:
                paredes.append(((x, y), (nx, ny)))

    random.shuffle(paredes)
    conjunto = ConjuntoDisjunto(celdas)

    for (x, y), (nx, ny) in paredes:
        if conjunto.unir((x, y), (nx, ny)):
            mx, my = (x + nx) // 2, (y + ny) // 2 
            grafo.insertar_arista((x, y), (mx, my), 1)
            grafo.insertar_arista((mx, my), (nx, ny), 1)

    return grafo
