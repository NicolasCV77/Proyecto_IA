# grafo.py

def encontrar_puntos(laberinto, N):
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