# grafo.py

def encontrar_puntos(laberinto, N):
    """Función que encuentra los puntos de inicio y meta en el laberinto

    Args:
        laberinto (List): Matriz que representa el laberinto
        N (int): Tamaño del laberinto (debe ser cuadrado)

    Returns:
        tuple tuple: Regresa los puntos donde está el inicio y la meta en el laberinto
    """
    inicio = None
    meta = None

    for i in range(N):
        for j in range(N):
            if laberinto[i][j] == 2:
                inicio = (i, j)
            if laberinto[i][j] == 3:
                meta = (i, j)
                
    return inicio, meta


def matriz_a_grafo(laberinto, N):
    """Función que toma la lista del laberinto y la convierte en un grafo representado como un diccionario de adyacencia

    Args:
        laberinto (List): Matriz que representa el laberinto
        N (int): Tamaño del laberinto (debe ser cuadrado)

    Returns:
        dict: Grafo representado como un diccionario de adyacencia
    """
    grafo = {}
    
    for i in range(N):
        for j in range(N):
            if laberinto[i][j] != 1:  # no es pared
                vecinos = []
                
                movimientos = [(-1,0),(1,0),(0,-1),(0,1)]
                
                for dx, dy in movimientos:
                    nx = i + dx
                    ny = j + dy
                    
                    if 0 <= nx < N and 0 <= ny < N:
                        if laberinto[nx][ny] != 1:
                            vecinos.append(((nx, ny), 1))
                
                grafo[(i, j)] = vecinos
                
    return grafo