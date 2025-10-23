class ControlMarcados:
    def __init__(self, nro_de_vertices):
        self.lista_de_marcados = [False for _ in range(nro_de_vertices)]

    def esta_marcado_el_vertice(self, nro_del_vertice):
        return self.lista_de_marcados[nro_del_vertice]

    def marcar_vertice(self, nro_del_vertice):
        self.lista_de_marcados[nro_del_vertice] = True

    def desmarcar_vertice(self, nro_del_vertice):
        self.lista_de_marcados[nro_del_vertice] = False

    def desmarcar_todos_los_vertices(self):
        self.lista_de_marcados = [False for _ in self.lista_de_marcados]

    def estan_todos_los_vertices_marcados(self):
        return all(self.lista_de_marcados)
