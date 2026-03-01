# main.py

from grafo import encontrar_puntos, matriz_a_grafo
from algoritmos import (
    dfs, bfs,
    a_estrella,
    construir_macro_grafo,
    a_estrella_macro,
    reconstruir_ruta_completa
)
from dibujar_laberinto import dibujar_laberinto, dibujar_recorrido


# Función para imprimir los resultados de cada algoritmo de manera clara.
def imprimir_resultado(nombre, camino, nodos_expandidos=None):
    """Función que imprime el recorrido que ha tomado el algoritmo

    Args:
        nombre (str): Nombre del algoritmo
        camino (List): Camino encontrado por el algoritmo
        nodos_expandidos (int, optional): Número de nodos expandidos (solo A*)
    """
    print("\n" + "=" * 40)
    print(nombre)
    print("=" * 40)
    if camino:
        print("Ruta encontrada:")
        print(camino)
        print("Longitud:", len(camino))
        if nodos_expandidos is not None:
            print("Nodos expandidos:", nodos_expandidos)
    else:
        print("No se encontró solución.")
        if nodos_expandidos is not None:
            print("Nodos expandidos:", nodos_expandidos)


# Función principal: ejecuta todos los algoritmos y muestra comparativa.
def main():
    """Función principal donde se indica el laberinto a solucionar y se llama a las
    funciones para encontrar el camino, las dimensiones del laberinto y dibujar el laberinto.
    """
    # El laberinto se representa como una matriz de NxN, donde:
    # 0: camino libre.
    # 1: pared.
    # 2: punto de inicio.
    # 3: punto de meta.

    # Cargar el laberinto desde el archivo laberinto.txt
    laberinto = []
    with open("laberinto.txt", "r") as f:
        for linea in f:
            fila = [int(x) for x in linea.strip().split(",")]
            laberinto.append(fila)

    # Tamaño del laberinto (debe ser cuadrado).
    N = len(laberinto)

    # Encontrar los puntos de inicio y meta en el laberinto.
    inicio, meta = encontrar_puntos(laberinto, N)

    # Convertir la matriz del laberinto a un grafo para facilitar la búsqueda de caminos.
    grafo = matriz_a_grafo(laberinto, N)

    # Imprimir los puntos de inicio y meta encontrados.
    print("Inicio:", inicio)
    print("Meta:  ", meta)

    # Dibujar el laberinto vacío para facilitar la visualización.
    dibujar_laberinto(laberinto, N)

    # ─ Algoritmos originales ─

    # DFS.
    camino_dfs = dfs(grafo, inicio, meta)
    imprimir_resultado("DFS", camino_dfs)
    dibujar_recorrido(laberinto, N, camino_dfs, "DFS")

    # BFS.
    camino_bfs = bfs(grafo, inicio, meta)
    imprimir_resultado("BFS", camino_bfs)
    dibujar_recorrido(laberinto, N, camino_bfs, "BFS")

    # A* original (paso a paso).
    camino_astar, expandidos_astar = a_estrella(grafo, inicio, meta)
    imprimir_resultado("A* (original, paso a paso)", camino_astar, expandidos_astar)
    dibujar_recorrido(laberinto, N, camino_astar, "A_estrella")

    # ─ A* sobre el Macro-Grafo ─

    # 1. Construir el macro-grafo con nodos de decisión.
    macro_grafo, nodos_decision, corredores = construir_macro_grafo(grafo, inicio, meta)

    print("\n" + "=" * 40)
    print("MACRO-GRAFO")
    print("=" * 40)
    print(f"Nodos de decisión identificados ({len(nodos_decision)}):")
    for nd in sorted(nodos_decision):
        vecinos_macro = [(v, c) for v, c in macro_grafo[nd]]
        print(f"  {nd}  →  {vecinos_macro}")

    # 2. Ejecutar A* sobre el macro-grafo.
    ruta_compacta, expandidos_macro = a_estrella_macro(macro_grafo, inicio, meta)

    print("\nRuta compacta (solo nodos de decisión):")
    print(ruta_compacta)
    if ruta_compacta:
        print("Nodos de decisión en la ruta:", len(ruta_compacta))

    # 3. Reconstruir la ruta completa (celda a celda) y graficar.
    ruta_completa = reconstruir_ruta_completa(ruta_compacta, corredores)
    imprimir_resultado("A* Macro (ruta completa reconstruida)", ruta_completa, expandidos_macro)
    dibujar_recorrido(laberinto, N, ruta_completa, "A_estrella_macro")

    # ─ Análisis Comparativo ─
    print("\n" + "=" * 40)
    print("ANÁLISIS COMPARATIVO")
    print("=" * 40)
    if camino_astar and ruta_completa:
        print(f"{'Métrica':<35} {'A* Original':>12} {'A* Macro':>12}")
        print("-" * 61)
        print(f"{'Nodos expandidos (cola prioridad)':<35} {expandidos_astar:>12} {expandidos_macro:>12}")
        print(f"{'Longitud de la ruta (pasos)':<35} {len(camino_astar):>12} {len(ruta_completa):>12}")
        print(f"{'Nodos de decisión en la ruta':<35} {'—':>12} {len(ruta_compacta):>12}")
        reduccion = (1 - expandidos_macro / expandidos_astar) * 100
        print(f"\nReducción de nodos expandidos: {reduccion:.1f}%")


if __name__ == "__main__":
    main()
