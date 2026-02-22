# algoritmos.py

import heapq
from collections import deque


# =========================
# DFS
# =========================

def dfs(grafo, inicio, meta):
    pila = [(inicio, [inicio])]
    visitados = set()
    
    while pila:
        nodo, camino = pila.pop()
        
        if nodo == meta:
            return camino
        
        if nodo not in visitados:
            visitados.add(nodo)
            
            for vecino, _ in grafo[nodo]:
                if vecino not in visitados:
                    pila.append((vecino, camino + [vecino]))
    
    return None


# =========================
# BFS
# =========================

def bfs(grafo, inicio, meta):
    cola = deque([(inicio, [inicio])])
    visitados = set()
    
    while cola:
        nodo, camino = cola.popleft()
        
        if nodo == meta:
            return camino
        
        if nodo not in visitados:
            visitados.add(nodo)
            
            for vecino, _ in grafo[nodo]:
                if vecino not in visitados:
                    cola.append((vecino, camino + [vecino]))
    
    return None


# =========================
# Heurística Manhattan
# =========================

def heuristica(nodo, meta):
    return abs(nodo[0] - meta[0]) + abs(nodo[1] - meta[1])


# =========================
# A*
# =========================

def a_estrella(grafo, inicio, meta):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))
    
    vino_de = {}
    costo_g = {}
    
    vino_de[inicio] = None
    costo_g[inicio] = 0
    
    while cola_prioridad:
        _, actual = heapq.heappop(cola_prioridad)
        
        if actual == meta:
            break
        
        for vecino, peso in grafo[actual]:
            nuevo_costo = costo_g[actual] + peso
            
            if vecino not in costo_g or nuevo_costo < costo_g[vecino]:
                costo_g[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(vecino, meta)
                heapq.heappush(cola_prioridad, (prioridad, vecino))
                vino_de[vecino] = actual
    
    # reconstruir camino
    camino = []
    nodo = meta
    
    while nodo is not None:
        camino.append(nodo)
        nodo = vino_de.get(nodo)
    
    camino.reverse()
    
    if camino and camino[0] == inicio:
        return camino
    else:
        return None