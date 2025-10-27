from adyacente_con_peso import AdyacenteConPeso


class ExcepcionAristaYaExiste(Exception):
    pass


class ExcepcionAristaNoExiste(Exception):
    pass


class GrafoPesado:
    NRO_DE_VERTICES_INVALIDOS = -1

    def __init__(self, vertices=None):
        self.lista_de_vertices = []
        self.listas_de_adyacentes = []
        if vertices:
            for v in vertices:
                self.insertar_vertice(v)

    # ------------------------
    # Métodos de vértices
    # ------------------------
    def insertar_vertice(self, vertice):
        if vertice in self.lista_de_vertices:
            return
        self.lista_de_vertices.append(vertice)
        self.listas_de_adyacentes.append([])

    def existe_vertice(self, vertice):
        return vertice in self.lista_de_vertices

    def indice_de_vertice(self, vertice):
        try:
            return self.lista_de_vertices.index(vertice)
        except ValueError:
            return self.NRO_DE_VERTICES_INVALIDOS

    # ------------------------
    # Métodos de aristas
    # ------------------------
    def insertar_arista(self, vertice1, vertice2, peso=1.0):
        if not self.existe_vertice(vertice1) or not self.existe_vertice(vertice2):
            raise ValueError("Uno o ambos vértices no existen.")

        pos_vertice1 = self.indice_de_vertice(vertice1)
        pos_vertice2 = self.indice_de_vertice(vertice2)

        adyacentes_de_vertice1 = self.listas_de_adyacentes[pos_vertice1]
        adyacentes_de_vertice2 = self.listas_de_adyacentes[pos_vertice2]

        ady1 = AdyacenteConPeso(pos_vertice2, peso)
        ady2 = AdyacenteConPeso(pos_vertice1, peso)

        if ady1 in adyacentes_de_vertice1:
            #raise ExcepcionAristaYaExiste("La arista ya existe.")
            pass

        adyacentes_de_vertice1.append(ady1)
        adyacentes_de_vertice2.append(ady2)

    def existe_arista(self, vertice1, vertice2):
        pos1 = self.indice_de_vertice(vertice1)
        pos2 = self.indice_de_vertice(vertice2)
        if pos1 == -1 or pos2 == -1:
            return False
        return AdyacenteConPeso(pos2) in self.listas_de_adyacentes[pos1]

    def eliminar_arista(self, vertice1, vertice2):
        if not self.existe_arista(vertice1, vertice2):
            raise ExcepcionAristaNoExiste("La arista no existe.")

        pos1 = self.indice_de_vertice(vertice1)
        pos2 = self.indice_de_vertice(vertice2)

        self.listas_de_adyacentes[pos1] = [
            ady for ady in self.listas_de_adyacentes[pos1] if ady.indice_vertice != pos2
        ]
        self.listas_de_adyacentes[pos2] = [
            ady for ady in self.listas_de_adyacentes[pos2] if ady.indice_vertice != pos1
        ]

    # ------------------------
    # Métodos de información
    # ------------------------
    def cantidad_de_vertices(self):
        return len(self.lista_de_vertices)

    def cantidad_de_aristas(self):
        total = sum(len(lista) for lista in self.listas_de_adyacentes)
        return total // 2  # porque es no dirigido

    def adyacentes_de_vertice(self, vertice):
        pos = self.indice_de_vertice(vertice)
        if pos == -1:
            raise ValueError("El vértice no existe.")
        return [
            (self.lista_de_vertices[ady.indice_vertice], ady.peso)
            for ady in self.listas_de_adyacentes[pos]
        ]

    def __str__(self):
        resultado = "Grafo Pesado:\n"
        for i, vertice in enumerate(self.lista_de_vertices):
            ady = [
                f"({self.lista_de_vertices[a.indice_vertice]}, peso={a.peso})"
                for a in self.listas_de_adyacentes[i]
            ]
            resultado += f"{vertice} -> {ady}\n"
        return resultado

'''from grafo_pesado import GrafoPesado

g = GrafoPesado(["A", "B", "C"])
g.insertar_arista("A", "B", 3)
g.insertar_arista("A", "C", 1.5)

print(g)
print("Adyacentes de A:", g.adyacentes_de_vertice("A"))
'''