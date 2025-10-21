#pgzero

celda = 50
anchura_en_cantidad_de_celdas = 5
altura_en_cantidad_de_celdas = 5
WIDTH = celda * anchura_en_cantidad_de_celdas
HEIGHT = celda * altura_en_cantidad_de_celdas
TITLE = "Mazmorras"
FPS = 30

mi_mapa = [[0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 2, 1, 3, 1, 0], 
          [0, 1, 1, 2, 1, 1, 0], 
          [0, 3, 2, 1, 1, 3, 0], 
          [0, 1, 1, 1, 3, 1, 0], 
          [0, 1, 3, 1, 1, 2, 0], 
          [0, 0, 0, 0, 0, 0, 0]]

def dibujar_mi_propio_mapa():
    for i in range(len(mi_mapa)):
        for j in range(len(dibujar_mi_propio_mapa[0])):
            celda.left = celda.width*j
            celda.top = celda.height*i
            celda.draw()

def draw():
    dibujar_mi_propio_mapa()

