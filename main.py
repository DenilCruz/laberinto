import pygame
import random
import sys
from grafo_pesado import GrafoPesado
from bfs import BFS
from astar import AStar
from kruskal_laberinto import generar_laberinto_kruskal
from dfs_laberinto import generar_laberinto

ANCHO, ALTO = 25, 25
TAM_CELDA = 25
FPS = 60

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (60, 60, 60)
AMARILLO = (255, 255, 0)

pygame.init()
pantalla = pygame.display.set_mode((ANCHO * TAM_CELDA, ALTO * TAM_CELDA))
pygame.display.set_caption("Laberinto con Grafo Pesado, DFS y BFS")
clock = pygame.time.Clock()

def generar_grafo_pesado_laberinto(ancho, alto):
    grafo = GrafoPesado()
    for i in range(alto):
        for j in range(ancho):
            grafo.insertar_vertice((i, j))
    return grafo

def dibujar_laberinto_pesado(grafo, camino=None):
    pantalla.fill(NEGRO)
    for (x, y) in grafo.lista_de_vertices:
        # Verificar si el vértice tiene adyacentes (caminos disponibles)
        color = BLANCO if grafo.adyacentes_de_vertice((x, y)) else GRIS
        pygame.draw.rect(pantalla, color, (y * TAM_CELDA, x * TAM_CELDA, TAM_CELDA, TAM_CELDA))

    if camino:
        for (x, y) in camino:
            pygame.draw.rect(pantalla, AMARILLO, (y * TAM_CELDA, x * TAM_CELDA, TAM_CELDA, TAM_CELDA))

    pygame.display.flip()

def main():
        
    grafo = generar_grafo_pesado_laberinto(ANCHO, ALTO)
    #grafo = generar_laberinto(grafo, ANCHO, ALTO)
    grafo = generar_laberinto_kruskal(grafo, ANCHO, ALTO)
    
    
    inicio, fin = (0, 0), (ALTO - 1, ANCHO - 1)

    dibujar_laberinto_pesado(grafo)
    pygame.display.flip()

    pygame.time.wait(1000)
    
    # Resolver con A*
    a_star = AStar(grafo, inicio, fin)
    camino_final = a_star.encontrar_camino()

    if camino_final:
        dibujar_laberinto_pesado(grafo, camino=camino_final)
    else:
        print("⚠ No se encontró camino al final")
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # Regenerar laberinto con grafo pesado
                    grafo = generar_grafo_pesado_laberinto(ANCHO, ALTO) 
                    grafo = generar_laberinto(grafo, ANCHO, ALTO)
                    dibujar_laberinto_pesado(grafo)
                    a_star = AStar(grafo, inicio, fin)
                    camino_final = a_star.encontrar_camino()

                    pygame.display.set_caption("Laberinto con Grafo Pesado DFS")

                    if camino_final:
                        dibujar_laberinto_pesado(grafo, camino=camino_final)
                    else:
                        print("⚠ No se encontró camino al final")

                elif event.key == pygame.K_2:
                    grafo = generar_grafo_pesado_laberinto(ANCHO, ALTO) 
                    grafo = generar_laberinto_kruskal(grafo, ANCHO, ALTO)
                    dibujar_laberinto_pesado(grafo)
                    a_star = AStar(grafo, inicio, fin)
                    camino_final = a_star.encontrar_camino()
                    
                    pygame.display.set_caption("Laberinto con Grafo Pesado Kruskal")

                    if camino_final:
                        dibujar_laberinto_pesado(grafo, camino=camino_final)
                    else:
                        print("⚠ No se encontró camino al final")

        clock.tick(FPS)

if __name__ == "__main__":
    main()