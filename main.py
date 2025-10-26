import pygame
import random
import sys
from grafo import Grafo
from bfs import BFS
from dfs import DFS
from astar import AStar


ANCHO, ALTO = 25,25
TAM_CELDA = 25
FPS = 60

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (60, 60, 60)
AMARILLO = (255, 255, 0)

pygame.init()
pantalla = pygame.display.set_mode((ANCHO * TAM_CELDA, ALTO * TAM_CELDA))
pygame.display.set_caption("Laberinto con Grafo, DFS y BFS")
clock = pygame.time.Clock()

def generar_grafo_laberinto(ancho, alto):
    g = Grafo()
    for i in range(alto):
        for j in range(ancho):
            g.insertarVertice((i, j))
    return g

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
                grafo.insertarArista((x, y), (mx, my))
                grafo.insertarArista((mx, my), (nx, ny))
                dfs(nx, ny)

    dfs(0, 0)

    x_final, y_final = ALTO - 1, ANCHO - 1
    visitado[x_final][y_final] = True 

    if x_final > 0:
        grafo.insertarArista((x_final - 1, y_final), (x_final, y_final))
        grafo.insertarArista((x_final, y_final), (x_final - 1, y_final))
    if y_final > 0:
        grafo.insertarArista((x_final, y_final - 1), (x_final, y_final))
        grafo.insertarArista((x_final, y_final), (x_final, y_final - 1))

    return grafo

def dibujar_laberinto(grafo, camino=None):
    pantalla.fill(NEGRO)
    for (x, y) in grafo.listaDeVertices:

        color = BLANCO if grafo.adyacentesDeVertice((x, y)) else GRIS
        pygame.draw.rect(pantalla, color, (y * TAM_CELDA, x * TAM_CELDA, TAM_CELDA, TAM_CELDA))

    if camino:
        for (x, y) in camino:
            pygame.draw.rect(pantalla, AMARILLO, (y * TAM_CELDA, x * TAM_CELDA, TAM_CELDA, TAM_CELDA))

    pygame.display.flip()

def main():
    grafo = generar_grafo_laberinto(ANCHO, ALTO)
    grafo = generar_laberinto(grafo, ANCHO, ALTO)
    inicio, fin = (0, 0), (ALTO - 1, ANCHO - 1)

    dibujar_laberinto(grafo)
    pygame.display.flip()

    pygame.time.wait(1000)
    
    # Resolver con A*
    a_star = AStar(grafo, inicio, fin)
    camino_final = a_star.encontrar_camino()

    if camino_final:
        dibujar_laberinto(grafo, camino=camino_final)
    else:
        print("⚠ No se encontró camino al final")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    grafo = generar_grafo_laberinto(ANCHO, ALTO)  # <- crear nuevo grafo
                    grafo = generar_laberinto(grafo, ANCHO, ALTO)
                    inicio, fin = (0, 0), (ALTO - 1, ANCHO - 1)
                    dibujar_laberinto(grafo)
                    a_star = AStar(grafo, inicio, fin)
                    camino_final = a_star.encontrar_camino()

                    if camino_final:
                        dibujar_laberinto(grafo, camino=camino_final)
                    else:
                        print("⚠ No se encontró camino al final")
        clock.tick(FPS)

if __name__ == "__main__":
    main()
