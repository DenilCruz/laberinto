import random
from grafo_pesado import GrafoPesado

class ConjuntoDisjunto:
    """Estructura de Unión y Búsqueda (Union-Find)."""
    def __init__(self, elementos):
        self.padre = {e: e for e in elementos}
        self.rango = {e: 0 for e in elementos}

    def encontrar(self, elemento):
        if self.padre[elemento] != elemento:
            self.padre[elemento] = self.encontrar(self.padre[elemento])
        return self.padre[elemento]

    def unir(self, a, b):
        raiz_a = self.encontrar(a)
        raiz_b = self.encontrar(b)
        if raiz_a == raiz_b:
            return False
        if self.rango[raiz_a] < self.rango[raiz_b]:
            self.padre[raiz_a] = raiz_b
        elif self.rango[raiz_a] > self.rango[raiz_b]:
            self.padre[raiz_b] = raiz_a
        else:
            self.padre[raiz_b] = raiz_a
            self.rango[raiz_a] += 1
        return True

def generar_laberinto_kruskal(grafo, ancho, alto):
    """Genera un laberinto usando el algoritmo de Kruskal (versión simple)."""
    
    # Limpiar el grafo existente
    for i in range(len(grafo.listas_de_adyacentes)):
        grafo.listas_de_adyacentes[i] = []
    
    # Crear todas las celdas (puntos en grid 2D)
    for x in range(alto):
        for y in range(ancho):
            if not grafo.existe_vertice((x, y)):
                grafo.insertar_vertice((x, y))
    
    # Lista de todas las posibles paredes horizontales y verticales
    paredes = []
    
    # Paredes horizontales (entre filas)
    for x in range(alto - 1):
        for y in range(ancho):
            paredes.append(((x, y), (x + 1, y), random.random()))
    
    # Paredes verticales (entre columnas)
    for x in range(alto):
        for y in range(ancho - 1):
            paredes.append(((x, y), (x, y + 1), random.random()))
    
    # Mezclar paredes
    random.shuffle(paredes)
    
    # Aplicar Kruskal
    vertices = [(i, j) for i in range(alto) for j in range(ancho)]
    conjunto = ConjuntoDisjunto(vertices)
    
    for v1, v2, peso in paredes:
        if conjunto.unir(v1, v2):
            grafo.insertar_arista(v1, v2, peso)
    
    return grafo