import random


def generar_laberinto(grafo, ancho, alto):
    visitado = [[False] * ancho for _ in range(alto)]

    def en_rango(x, y):
        return 0 <= x < alto and 0 <= y < ancho

    def dfs(x, y):
        visitado[x][y] = True
    
        direcciones = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        random.shuffle(direcciones)

        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if en_rango(nx, ny) and not visitado[nx][ny]:
                
                mx, my = x + dx // 2, y + dy // 2
                grafo.insertar_arista((x, y), (mx, my), 1)
                grafo.insertar_arista((mx, my), (nx, ny), 1)
                dfs(nx, ny)

    dfs(0, 0)

    x_final, y_final = alto - 1, ancho - 1
    visitado[x_final][y_final] = True 

    if x_final > 0:
        grafo.insertar_arista((x_final - 1, y_final), (x_final, y_final), 1)
        grafo.insertar_arista((x_final, y_final), (x_final - 1, y_final), 1)
    if y_final > 0:
        grafo.insertar_arista((x_final, y_final - 1), (x_final, y_final), 1)
        grafo.insertar_arista((x_final, y_final), (x_final, y_final - 1), 1)

    return grafo