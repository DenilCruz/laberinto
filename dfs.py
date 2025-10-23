from marcados import ControlMarcados

class DFS:
    def __init__(self, grafo, vertice_de_partida):

        self.grafo = grafo
        self.vertice_de_partida = vertice_de_partida
        self.control_marcados = ControlMarcados(len(grafo.listaDeVertices))
        self.recorrido = []

    def ejecutar_desde_inicio(self):
        self.control_marcados.desmarcar_todos_los_vertices()
        self.recorrido = []
        self.ejecutar_recorrido(self.vertice_de_partida)
        return self.recorrido
      
    def ejecutar_recorrido(self, vertice_en_turno):

        self.grafo.validarVertice(vertice_en_turno)

        nro_vertice = self.grafo.getNroDelVertice(vertice_en_turno)
        self.control_marcados.marcar_vertice(nro_vertice)
        self.recorrido.append(vertice_en_turno)

        adyacentes = self.grafo.adyacentesDeVertice(vertice_en_turno)

        for adyacente in adyacentes:
            nro_adyacente = self.grafo.getNroDelVertice(adyacente)
            if not self.control_marcados.esta_marcado_el_vertice(nro_adyacente):
                self.ejecutar_recorrido(adyacente)
