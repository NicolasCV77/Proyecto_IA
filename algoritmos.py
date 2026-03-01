# algoritmos.py

import heapq
from collections import deque 

# =========================
# DFS
# =========================
def dfs(grafo, inicio, meta): 
    """Implementación del algoritmo DFS

    Args:
        grafo (dict): Grafo representado como un diccionario de adyacencia
        inicio (tuple): Punto de inicio en el grafo
        meta (tuple): Punto de meta en el grafo

    Returns:
        list: Camino desde inicio hasta meta, o None si no hay solución
    """
    pila = [(inicio, [inicio])]
    visitados = set()

    # DFS: LIFO (Last In, First Out) usando una pila.
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
    """Implementación del algoritmo BFS

    Args:
        grafo (dict): Grafo representado como un diccionario de adyacencia
        inicio (tuple): Punto de inicio en el grafo
        meta (tuple): Punto de meta en el grafo

    Returns:
        list: Camino desde inicio hasta meta, o None si no hay solución
    """
    cola = deque([(inicio, [inicio])])
    visitados = set()

    # BFS: FIFO (First In, First Out) usando una cola.
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
    """Función que calcula el valor de la heurística Manhattan entre dos puntos

    Args:
        nodo (tuple): Coordenadas del nodo actual
        meta (tuple): Coordenadas del nodo meta

    Returns:
        int: Valor de la heurística Manhattan entre los dos puntos
    """
    return abs(nodo[0] - meta[0]) + abs(nodo[1] - meta[1])


# =========================
# A* (original, paso a paso)
# ========================= 
def a_estrella(grafo, inicio, meta):
    """Implementación del algoritmo A* original (paso a paso)

    Args:
        grafo (dict): Grafo representado como un diccionario de adyacencia
        inicio (tuple): Punto de inicio en el grafo
        meta (tuple): Punto de meta en el grafo

    Returns:
        tuple: (camino, nodos_expandidos) donde camino es la lista de celdas
                y nodos_expandidos es el contador de nodos sacados de la cola
    """ 
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))
    vino_de = {inicio: None}
    costo_g = {inicio: 0}
    nodos_expandidos = 0

    # A*: Prioridad basada en f(n) = g(n) + h(n), donde g(n) es el costo acumulado
    # desde el inicio hasta el nodo n, y h(n) es la heurística (distancia Manhattan) desde n hasta la meta.
    while cola_prioridad:
        _, actual = heapq.heappop(cola_prioridad)
        nodos_expandidos += 1

        if actual == meta:
            break

        for vecino, peso in grafo[actual]:
            nuevo_costo = costo_g[actual] + peso

            if vecino not in costo_g or nuevo_costo < costo_g[vecino]:
                costo_g[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(vecino, meta)
                heapq.heappush(cola_prioridad, (prioridad, vecino))
                vino_de[vecino] = actual

    # Reconstruir camino
    camino = []
    nodo = meta

    while nodo is not None:
        camino.append(nodo)
        nodo = vino_de.get(nodo)

    camino.reverse()

    if camino and camino[0] == inicio:
        return camino, nodos_expandidos
    else:
        return None, nodos_expandidos


# =========================
# MACRO-GRAFO: Identificación de Nodos de Decisión
# =========================
def identificar_nodos_decision(grafo, inicio, meta):
    """Identifica los nodos de decisión en el laberinto.

    Un nodo de decisión es cualquier nodo cuyo grado (número de vecinos)
    sea diferente de 2. Esto incluye:
        - El inicio y la meta (siempre son nodos de decisión)
        - Bifurcaciones (grado 3 o 4)
        - Callejones sin salida (grado 1)

    Args:
        grafo (dict): Grafo original del laberinto
        inicio (tuple): Coordenada del punto de inicio
        meta (tuple): Coordenada del punto de meta

    Returns:
        set: Conjunto de coordenadas que son nodos de decisión
    """
    nodos_decision = set()

    for nodo, vecinos in grafo.items():
        grado = len(vecinos)
        # Es nodo de decisión si su grado es diferente de 2
        # o si es inicio/meta (siempre deben incluirse).
        if grado != 2 or nodo == inicio or nodo == meta:
            nodos_decision.add(nodo)

    return nodos_decision


# =========================
# MACRO-GRAFO: Exploración de Corredores
# =========================
def explorar_corredor(grafo, origen, primer_paso, nodos_decision):
    """Parte de un nodo de decisión y recorre el corredor hasta encontrar
    el siguiente nodo de decisión, registrando todos los pasos intermedios.

    Args:
        grafo (dict): Grafo original del laberinto
        origen (tuple): Nodo de decisión desde el que inicia el corredor
        primer_paso (tuple): Primer vecino en la dirección del corredor
        nodos_decision (set): Conjunto de nodos de decisión

    Returns:
        tuple: (nodo_destino, costo, pasos_intermedios) donde:
            - nodo_destino es el siguiente nodo de decisión encontrado
            - costo es la longitud (número de pasos) del corredor
            - pasos_intermedios es la lista ordenada de celdas del corredor (sin incluir origen, incluyendo nodo_destino)
    """
    pasos = [primer_paso]
    anterior = origen
    actual = primer_paso
    costo = 1

    # Avanzar por el corredor mientras no lleguemos a un nodo de decisión.
    while actual not in nodos_decision:
        # Buscar el único vecino que no sea el anterior (el pasillo continúa).
        siguiente = None
        for vecino, _ in grafo[actual]:
            if vecino != anterior:
                siguiente = vecino
                break

        if siguiente is None:
            # Callejón sin salida sin ser nodo de decisión (no debería ocurrir).
            break

        anterior = actual
        actual = siguiente
        pasos.append(actual)
        costo += 1

    return actual, costo, pasos


# =========================
# MACRO-GRAFO: Construcción
# =========================
def construir_macro_grafo(grafo, inicio, meta):
    """Construye el macro-grafo donde los nodos son los nodos de decisión
    y las aristas representan corredores completos con su longitud como peso.

    Args:
        grafo (dict): Grafo original del laberinto
        inicio (tuple): Coordenada del punto de inicio
        meta (tuple): Coordenada del punto de meta

    Returns:
        tuple: (macro_grafo, nodos_decision, corredores) donde:
                - macro_grafo es un dict {nodo: [(vecino, peso), ...]}
                - nodos_decision es el conjunto de nodos de decisión
                - corredores es un dict {(origen, destino): [pasos]} con los
                pasos intermedios de cada corredor (para reconstruir la ruta)
    """
    nodos_decision = identificar_nodos_decision(grafo, inicio, meta)

    # macro_grafo: nodo de decisión → lista de (nodo_destino, costo).
    macro_grafo = {nd: [] for nd in nodos_decision}

    # corredores: (origen, destino) → lista de celdas intermedias (sin origen, con destino).
    corredores = {}

    for nd in nodos_decision:
        for primer_paso, _ in grafo[nd]:
            # Explorar el corredor que sale hacia primer_paso.
            destino, costo, pasos = explorar_corredor(grafo, nd, primer_paso, nodos_decision)

            # Agregar la macro-arista si no existe ya (evitar duplicados).
            ya_existe = any(v == destino for v, _ in macro_grafo[nd])
            if not ya_existe:
                macro_grafo[nd].append((destino, costo))
                # Guardar los pasos del corredor en ambas direcciones.
                corredores[(nd, destino)] = pasos
                corredores[(destino, nd)] = list(reversed([nd] + pasos[:-1]))

    return macro_grafo, nodos_decision, corredores


# =========================
# A* sobre el MACRO-GRAFO
# =========================
def a_estrella_macro(macro_grafo, inicio, meta):
    """Implementación de A* que opera sobre el macro-grafo, saltando entre
    nodos de decisión en lugar de avanzar celda a celda.

    El costo g(n) acumula los pesos de las macro-aristas (longitudes de corredores).
    La heurística sigue siendo la distancia Manhattan al nodo meta.

    Args:
        macro_grafo (dict): Macro-grafo {nodo_decision: [(vecino, peso), ...]}
        inicio (tuple): Coordenada del punto de inicio
        meta (tuple): Coordenada del punto de meta

    Returns:
        tuple: (ruta_compacta, nodos_expandidos) donde:
                - ruta_compacta es la lista de nodos de decisión desde inicio hasta meta
                - nodos_expandidos es el contador de nodos sacados de la cola
    """
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))

    vino_de = {inicio: None}
    costo_g = {inicio: 0}
    nodos_expandidos = 0

    while cola_prioridad:
        _, actual = heapq.heappop(cola_prioridad)
        nodos_expandidos += 1

        if actual == meta:
            break

        # Explorar macro-vecinos (siguiente nodo de decisión al final de cada corredor).
        for macro_vecino, peso in macro_grafo.get(actual, []):
            nuevo_costo = costo_g[actual] + peso

            if macro_vecino not in costo_g or nuevo_costo < costo_g[macro_vecino]:
                costo_g[macro_vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(macro_vecino, meta)
                heapq.heappush(cola_prioridad, (prioridad, macro_vecino))
                vino_de[macro_vecino] = actual

    # Reconstruir ruta compacta (solo nodos de decisión).
    ruta_compacta = []
    nodo = meta

    while nodo is not None:
        ruta_compacta.append(nodo)
        nodo = vino_de.get(nodo)

    ruta_compacta.reverse()

    if ruta_compacta and ruta_compacta[0] == inicio:
        return ruta_compacta, nodos_expandidos
    else:
        return None, nodos_expandidos


# =========================
# Reconstrucción de la Ruta Completa
# =========================
def reconstruir_ruta_completa(ruta_compacta, corredores):
    """Expande la ruta compacta (nodos de decisión) a la ruta completa,
    incluyendo todos los pasos intermedios a través de los corredores.

    Args:
        ruta_compacta (list): Secuencia de nodos de decisión desde inicio hasta meta
        corredores (dict): Diccionario {(origen, destino): [pasos_intermedios]} generado por construir_macro_grafo

    Returns:
        list: Ruta completa celda a celda desde inicio hasta meta
    """
    if ruta_compacta is None or len(ruta_compacta) == 0:
        return None

    # La ruta completa comienza con el primer nodo de decisión (inicio).
    ruta_completa = [ruta_compacta[0]]

    for i in range(len(ruta_compacta) - 1):
        origen = ruta_compacta[i]
        destino = ruta_compacta[i + 1]

        # Agregar los pasos del corredor entre origen y destino
        # (los pasos ya no incluyen el origen, pero sí el destino).
        pasos = corredores.get((origen, destino), [destino])
        ruta_completa.extend(pasos)

    return ruta_completa
