# Proyecto_IA

Para este proyecto se usan los algoritmos de BFS, DFS y A* con heurística implementada con distancia Manhattan dentro de un laberinto dado, el cual usa diferentes valores dentro de una matriz cuadrada de tamaño NxN para representar paredes, caminos, inicio y meta, los cuales se dividen de la siguiente forma.

- **0** → Camino donde se puede mover
- **1** → pared
- **2** → Nodo de inicio
- **3** → Nodo Final / Meta

### Descripción de los diferentes archivos dentro del proyecto

#### `main.py`
Archivo con el flujo principal del programa.<br>
Aquí se llaman las diferentes funciones que se tienen en otros archivos, los cuales permiten ver como diferentes algoritmos se comportan en un mismo problema.<br>
En este archivo reside la variable la cual contiene el `laberinto` a solucionar

#### `algoritmos.py`
Archivo con las implementaciones de los diferentes algoritmos.<br>
Aquí se tiene la lógica que rige a los algoritmos usados en el programa principal. Aquí se encuentran los algoritmos de `DFS`, `BFS` y `A*`, además de contener el calculo de la `Heuristica` para el algoritmo `A*` 

#### `grafo.py`
Archivo donde se almacenan funciones auxiliares. <br>
En este archivo se encuentran funciones que permiten hallar los puntos donde están tanto, el inicio y la meta del laberinto como la conversión de la matriz del laberinto a un grafo, de modo que permita a los algoritmos su fácil recorrido mediante este. 

#### `dibujar_laberinto.py`
En este archivo se encuentra una función que nos permite graficar el laberinto y guardar una imagen de este. Permitiendo la depuración y verificación de los diferentes algoritmos aquí presentados