#pgzero

celda = 50
anchura_en_cantidad_de_celdas = 5
altura_en_cantidad_de_celdas = 5
WIDTH = celda * anchura_en_cantidad_de_celdas
HEIGHT = celda * altura_en_cantidad_de_celdas
TITLE = "Mazmorras"
FPS = 30

my_map = [[0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 2, 1, 3, 1, 0], 
          [0, 1, 1, 2, 1, 1, 0], 
          [0, 3, 2, 1, 1, 3, 0], 
          [0, 1, 1, 1, 3, 1, 0], 
          [0, 1, 3, 1, 1, 2, 0], 
          [0, 0, 0, 0, 0, 0, 0]]


def map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            cell.left = cell.width*j
            cell.top = cell.height*i
            cell.draw()

def draw():
    map_draw()
    
