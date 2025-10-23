from marcados import ControlMarcados
from collections import deque

class BFS:
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

        cola = deque()  
        nro_vertice = self.grafo.getNroDelVertice(vertice_en_turno)
        cola.append(nro_vertice)
        self.control_marcados.marcar_vertice(nro_vertice)

        while cola:
            nro_actual = cola.popleft() 
            vertice_actual = self.grafo.getVerticePorIndice(nro_actual)
            self.recorrido.append(vertice_actual)

            adyacentes = self.grafo.adyacentesDeVertice(vertice_actual)
            for adyacente in adyacentes:
                nro_adyacente = self.grafo.getNroDelVertice(adyacente)
                if not self.control_marcados.esta_marcado_el_vertice(nro_adyacente):
                    cola.append(nro_adyacente)
                    self.control_marcados.marcar_vertice(nro_adyacente)
    
    
