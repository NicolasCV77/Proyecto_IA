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