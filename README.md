# Proyecto_IA

Para este proyecto se usan los algoritmos de BFS, DFS y A* con heurística implementada con distancia Manhattan dentro de un laberinto dado, el cual usa diferentes valores dentro de una matriz cuadrada de tamaño NxN para representar paredes, caminos, inicio y meta, los cuales se dividen de la siguiente forma.

- **0** → Camino donde se puede mover
- **1** → Pared
- **2** → Nodo de inicio
- **3** → Nodo Final / Meta

---
## Modificación: A* sobre Macro-Grafo
Como optimización al proyecto original, se implementó una técnica de **abstracción del espacio de estados** que permite al agente saltar entre intersecciones (nodos de decisión) en lugar de avanzar celda a celda. Esto reduce significativamente el número de nodos expandidos en laberintos con pasillos largos.

Un **nodo de decisión** es cualquier celda cuyo grado (número de vecinos) sea diferente de 2, lo que incluye:
- El nodo de inicio y el nodo meta
- Bifurcaciones (grado 3 o 4)
- Callejones sin salida (grado 1)

El **macro-grafo** resultante conecta únicamente estos nodos de decisión, donde el peso de cada arista es la longitud del corredor que los une. El A* opera sobre este grafo reducido y luego reconstruye el camino completo celda a celda para su visualización.

---

## Descripción de los archivos

#### `main.py`
Archivo con el flujo principal del programa. Aquí se llaman las diferentes funciones que se tienen en otros archivos, los cuales permiten ver cómo los diferentes algoritmos se comportan en un mismo problema.

Carga el laberinto desde `laberinto.txt`, ejecuta los 4 algoritmos (DFS, BFS, A* original y A* Macro), genera las imágenes de cada recorrido y muestra al final un análisis comparativo entre A* original y A* Macro.

#### `algoritmos.py`
Archivo con las implementaciones de los diferentes algoritmos. Contiene:
- `dfs` — Búsqueda en profundidad
- `bfs` — Búsqueda en anchura
- `heuristica` — Distancia Manhattan entre dos puntos
- `a_estrella` — A* original, avanzando celda a celda
- `identificar_nodos_decision` — Detecta los nodos de decisión del grafo
- `explorar_corredor` — Recorre un pasillo hasta encontrar el siguiente nodo de decisión
- `construir_macro_grafo` — Construye el grafo reducido de nodos de decisión
- `a_estrella_macro` — A* que opera sobre el macro-grafo
- `reconstruir_ruta_completa` — Expande la ruta compacta a la ruta celda a celda

#### `grafo.py`
Archivo con funciones auxiliares para procesar el laberinto:
- `encontrar_puntos` — Localiza las coordenadas del inicio (`2`) y la meta (`3`)
- `matriz_a_grafo` — Convierte la matriz del laberinto en un diccionario de adyacencia para facilitar la búsqueda

#### `dibujar_laberinto.py`
Archivo con las funciones de visualización:
- `dibujar_laberinto` — Genera una imagen del laberinto vacío (`laberinto.png`)
- `dibujar_recorrido` — Genera una imagen del laberinto con el camino encontrado marcado en amarillo y flechas de dirección. Guarda una imagen por algoritmo con el nombre `recorrido_<algoritmo>.png`

#### `laberinto.txt`
Archivo de texto con la matriz del laberinto. Cada fila es una línea y los valores están separados por comas. El laberinto debe ser cuadrado (NxN).

---

## Imágenes generadas

Al ejecutar `main.py` se generan las siguientes imágenes en el directorio del proyecto:

| Archivo | Descripción |
|---|---|
| `laberinto.png` | El laberinto sin recorridos |
| `recorrido_dfs.png` | Camino encontrado por DFS |
| `recorrido_bfs.png` | Camino encontrado por BFS |
| `recorrido_a_estrella.png` | Camino encontrado por A* original |
| `recorrido_a_estrella_macro.png` | Camino encontrado por A* Macro |

---

## Cómo ejecutar

```bash
python main.py
```

Asegúrate de tener el archivo `laberinto.txt` en el mismo directorio antes de ejecutar.
