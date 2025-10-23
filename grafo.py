
class ExcepcionAristaNoExiste(Exception):
    pass

class ExcepcionAristaYaExiste(Exception):
    pass


class Grafo:
    NRO_DE_VERTICE_INVALIDO = -1

    def __init__(self, vertices=None):
        self.listaDeVertices = []
        self.listasDeAdyacentes = []

        if vertices is not None:
            for vertice in vertices:
                self.insertarVertice(vertice)

    def getNroDelVertice(self, unVertice):
        for indice, verticeEnTurno in enumerate(self.listaDeVertices):
            if verticeEnTurno == unVertice:
                return indice
        return Grafo.NRO_DE_VERTICE_INVALIDO

    def validarVertice(self, vertice):
        if vertice not in self.listaDeVertices:
            raise ValueError(f"El {vertice} no esta en el grafo")

    def insertarVertice(self, vertice):
        if vertice in self.listaDeVertices:
            return
        self.listaDeVertices.append(vertice)
        self.listasDeAdyacentes.append([])

    def insertarArista(self, origen, destino):

        if self.existeArista(origen, destino):
            raise ExcepcionAristaYaExiste(f"La arista ({origen}, {destino}) ya existe.")

        posOrigen = self.getNroDelVertice(origen)
        posDestino = self.getNroDelVertice(destino)
        
        self.listasDeAdyacentes[posOrigen].append(posDestino)

    def eliminarArista(self, origen, destino):
        
        if not self.existeArista(origen, destino):
            raise ExcepcionAristaNoExiste(f"La arista ({origen}, {destino}) no existe.")

        posOrigen = self.getNroDelVertice(origen)
        posDestino = self.getNroDelVertice(destino)

        self.listasDeAdyacentes[posOrigen].remove(posDestino)

    def existeArista(self, origen, destino):
        self.validarVertice(origen)
        self.validarVertice(destino)
        posOrigen = self.getNroDelVertice(origen)
        posDestino = self.getNroDelVertice(destino)
        return posDestino in self.listasDeAdyacentes[posOrigen]

    def adyacentesDeVertice(self, vertice):
        self.validarVertice(vertice)
        posicion = self.getNroDelVertice(vertice)
        return [self.listaDeVertices[indice] for indice in self.listasDeAdyacentes[posicion]]
        #adyacentes = []  

        #for indice in self.listasDeAdyacentes[posicion]:
        #    vertice_adyacente = self.listaDeVertices[indice]
        #    adyacentes.append(vertice_adyacente)

        #return adyacentes
        
    def getVerticePorIndice(self, indice):
        if 0 <= indice < len(self.listaDeVertices):
            return self.listaDeVertices[indice]
        else:
            raise IndexError(f"Índice {indice} fuera de rango")
        
    def __str__(self):
        resultado = "Grafo:\n"
        for i, vertice in enumerate(self.listaDeVertices):
            adyacencias = self.adyacentesDeVertice(vertice)
            resultado += f"{vertice} -> {adyacencias}\n"
        return resultado

if __name__ == "__main__":
    grafo = Grafo([45,23,65,2])
    #grafo.insertarVertice(45)
    #grafo.insertarVertice(23)
    #grafo.insertarVertice(65)
    #grafo.insertarVertice(2)
    grafo.insertarArista(45,23)
    grafo.insertarArista(23,65)
    grafo.insertarArista(65,2)
    grafo.insertarArista(2,45)
    grafo.insertarArista(23,2)
    grafo.insertarArista(23,23)
    print(grafo)
    print(grafo.adyacentesDeVertice(23))
    print(grafo.existeArista(2,23))
