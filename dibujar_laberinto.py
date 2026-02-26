#dibujar_laberinto.py

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


def dibujar_laberinto(matriz, n):
    laberinto = np.array(matriz)

    # Colores: 0=camino(blanco), 1=pared(negro), 2=inicio(verde), 3=meta(rojo)
    colores = ListedColormap([
        "#FFFFFF",  # 0 - camino (blanco)
        "#2C3E50",  # 1 - pared (azul oscuro/negro)
        "#27AE60",  # 2 - inicio (verde)
        "#E74C3C"   # 3 - meta (rojo)
    ])

    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Dibujar el laberinto
    ax.imshow(laberinto, cmap=colores, vmin=0, vmax=3)
    
    # Dibujar líneas de cuadrícula para formar celdas
    for i in range(n + 1):
        ax.axhline(i - 0.5, color='black', linewidth=2)
        ax.axvline(i - 0.5, color='black', linewidth=2)
    
    # Configurar ejes
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(range(n))
    ax.set_yticklabels(range(n))
    
    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(n - 0.5, -0.5)
    
    plt.title("Laberinto", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig("laberinto.png", dpi=150, bbox_inches='tight')
    plt.close()


def dibujar_recorrido(matriz, n, camino, nombre_algoritmo):
    """Dibuja el laberinto con el recorrido del algoritmo marcado

    Args:
        matriz (List): Matriz que representa el laberinto
        n (int): Tamaño del laberinto
        camino (List): Lista de coordenadas del recorrido
        nombre_algoritmo (str): Nombre del algoritmo para el título y archivo
    """
    if camino is None:
        return
    
    laberinto = np.array(matriz, dtype=float)
    
    # Colores: 0=camino(blanco), 1=pared(negro), 2=inicio(verde), 3=meta(rojo), 4=recorrido(amarillo)
    colores = ListedColormap([
        "#FFFFFF",  # 0 - camino (blanco)
        "#2C3E50",  # 1 - pared (azul oscuro/negro)
        "#27AE60",  # 2 - inicio (verde)
        "#E74C3C",  # 3 - meta (rojo)
        "#F1C40F"   # 4 - recorrido (amarillo)
    ])
    
    # Marcar el recorrido en el laberinto (excepto inicio y meta)
    for coord in camino:
        i, j = coord
        if laberinto[i][j] == 0:  # Solo marcar celdas de camino libre
            laberinto[i][j] = 4

    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Dibujar el laberinto con el recorrido
    ax.imshow(laberinto, cmap=colores, vmin=0, vmax=4)
    
    # Dibujar líneas de cuadrícula para formar celdas
    for i in range(n + 1):
        ax.axhline(i - 0.5, color='black', linewidth=2)
        ax.axvline(i - 0.5, color='black', linewidth=2)
    
    # Dibujar flechas para mostrar la dirección del recorrido
    for idx in range(len(camino) - 1):
        y1, x1 = camino[idx]
        y2, x2 = camino[idx + 1]
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='#E67E22', lw=2))
    
    # Configurar ejes
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(range(n))
    ax.set_yticklabels(range(n))
    
    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(n - 0.5, -0.5)
    
    plt.title(f"Recorrido {nombre_algoritmo}", fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    # Guardar con nombre basado en el algoritmo
    nombre_archivo = f"recorrido_{nombre_algoritmo.lower()}.png"
    plt.savefig(nombre_archivo, dpi=150, bbox_inches='tight')
    plt.close()