# main.py

from grafo import encontrar_puntos, matriz_a_grafo
from algoritmos import dfs, bfs, a_estrella


def imprimir_resultado(nombre, camino):
    print("\n" + nombre)
    if camino:
        print("Ruta encontrada:")
        print(camino)
        print("Longitud:", len(camino))
    else:
        print("No se encontró solución.")


def main():

    laberinto = [
        [2,1,1,1,0,0,1,1,1,1],
        [0,0,0,1,1,1,0,0,1,0],
        [1,1,0,0,0,1,0,1,1,1],
        [0,1,1,1,0,1,0,1,0,1],
        [1,1,0,1,0,1,0,0,1,1],
        [0,0,0,1,0,3,1,0,1,0],
        [1,1,1,1,1,0,1,0,1,1],
        [1,0,0,0,0,1,1,1,0,1],
        [1,1,1,1,1,1,0,1,0,1],
        [1,0,1,0,1,0,1,1,1,1]
    ]

    N = len(laberinto)

    inicio, meta = encontrar_puntos(laberinto, N)
    grafo = matriz_a_grafo(laberinto, N)

    print("Inicio:", inicio)
    print("Meta:", meta)

    imprimir_resultado("DFS", dfs(grafo, inicio, meta))
    imprimir_resultado("BFS", bfs(grafo, inicio, meta))
    imprimir_resultado("A*", a_estrella(grafo, inicio, meta))


if __name__ == "__main__":
    main()