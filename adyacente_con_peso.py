class AdyacenteConPeso:
    def __init__(self, vertice, peso=0.0):
        self.indice_vertice = vertice
        self.peso = peso

    def get_indice_vertice(self):
        return self.indice_vertice

    def set_indice_vertice(self, vertice):
        self.indice_vertice = vertice

    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso

    def __lt__(self, otro):
        return self.indice_vertice < otro.indice_vertice

    def __eq__(self, otro):
        if not isinstance(otro, AdyacenteConPeso):
            return False
        return self.indice_vertice == otro.indice_vertice

    def __repr__(self):
        return f"({self.indice_vertice}, peso={self.peso})"
