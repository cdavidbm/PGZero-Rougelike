#pgzero

celda = Actor("border")
celda1 = Actor("crack")
celda2 = Actor("bones")
celda3 = Actor("floor")
anchura_en_cantidad_de_celdas = 7
altura_en_cantidad_de_celdas = 7
WIDTH = celda.width * anchura_en_cantidad_de_celdas
HEIGHT = celda.height * altura_en_cantidad_de_celdas
TITLE = "Mazmorras"
FPS = 30

personaje = Actor("stand")
personaje.salud = 100
personaje.ataque = 5

mi_mapa = [[0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 2, 1, 3, 1, 0], 
          [0, 1, 1, 2, 1, 1, 0], 
          [0, 3, 2, 1, 1, 3, 0], 
          [0, 1, 1, 1, 3, 1, 0], 
          [0, 1, 3, 1, 1, 2, 0], 
          [0, 0, 0, 0, 0, 0, 0]]

def dibujar_mi_propio_mapa():
    for i in range(len(mi_mapa)):
        for j in range(len(mi_mapa[0])):
            if mi_mapa[i][j] == 0:
                celda.left = celda.width*j
                celda.top = celda.height*i
                celda.draw()
            elif mi_mapa[i][j] == 1:
                celda1.left = celda1.width*j
                celda1.top = celda1.height*i
                celda1.draw()
            elif mi_mapa[i][j] == 2:
                celda2.left = celda2.width*j
                celda2.top = celda2.height*i
                celda2.draw()
            elif mi_mapa[i][j] == 3:
                celda3.left = celda3.width*j
                celda3.top = celda3.height*i
                celda3.draw()

def draw():
    dibujar_mi_propio_mapa()
    personaje.draw()
    screen.draw.text(personaje.salud, center=(325, 10), color = 'white', fontsize = 16)
    screen.draw.text(personaje.ataque, center=(325, 25), color = 'white', fontsize = 16)

def on_key_down(key):
    if keyboard.right and personaje.x + celda.width < WIDTH - celda.width:
        personaje.x += celda.width





"""
for i in range(5):
    for j in range(5):
        print("el ciclo grande i:", i, "el subciclo j: ", j)
        
print("------------------")
print("tabla de multiplicar")
print("------------------")

for i in range(5):
    for j in range(5):
        print(i , "x", j, "=", i*j)
"""
