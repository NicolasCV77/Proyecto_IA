# main.py

from grafo import encontrar_puntos, matriz_a_grafo
from algoritmos import dfs, bfs, a_estrella
from dibujar_laberinto import dibujar_laberinto

def imprimir_resultado(nombre, camino):
    """Función que imprime el recorrido que ha tomado el algoritmo para llegar al resultado final

    Args:
        nombre (str): Nombre del algoritmo
        camino (List): Camino encontrado por el algoritmo
    """
    print("\n" + nombre)
    if camino:
        print("Ruta encontrada:")
        print(camino)
        print("Longitud:", len(camino))
    else:
        print("No se encontró solución.")


def main():
    """Función principal donde se indica el laberinto a solucionar y se llama a las funciones para encontrar el camino, las dimensiones del laberinto y dibujar el laberinto, 
    """

    # El laberinto se representa como una matriz de 10x10, donde:
    # 0: camino libre
    # 1: pared
    # 2: punto de inicio
    # 3: punto de meta
    laberinto = [
        [2,0,0,0,0,0,1,1,1,1],
        [0,1,1,1,1,0,0,0,1,0],
        [0,1,0,0,0,1,0,1,1,1],
        [0,1,0,1,0,1,0,1,0,1],
        [0,1,0,1,0,1,0,0,1,1],
        [0,0,0,1,0,0,0,0,1,0],
        [1,1,1,1,1,3,1,0,1,1],
        [1,0,0,0,0,1,1,1,0,1],
        [1,1,1,1,1,1,0,1,0,1],
        [1,0,1,0,1,0,1,1,1,1]
    ]

    # Tamaño del laberinto (Debe de ser cuadrado)
    N = len(laberinto)

    # Encontrar los puntos de inicio y meta en el laberinto
    inicio, meta = encontrar_puntos(laberinto, N)

    # Convertir la matriz del laberinto a un grafo para facilitar la búsqueda de caminos
    grafo = matriz_a_grafo(laberinto, N)

    # Imprimir los puntos de inicio y meta encontrados
    print("Inicio:", inicio)
    print("Meta:", meta)

    # Dibujar el laberinto para facilitar la visualización 
    dibujar_laberinto(laberinto, N)

    # Ejecutar los algoritmos de búsqueda y mostrar los resultados
    imprimir_resultado("DFS", dfs(grafo, inicio, meta))
    imprimir_resultado("BFS", bfs(grafo, inicio, meta))
    imprimir_resultado("A*", a_estrella(grafo, inicio, meta))


if __name__ == "__main__":
    main()