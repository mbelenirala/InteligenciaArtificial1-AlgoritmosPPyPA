from Genlab import *
from PIL import Image, ImageDraw, ImageFont

#ACA ESTOY PROBANDO COMO MOSTRAR EL LABERINTO EN UNA IMAGEN, FIJATE SI TE GUSTA ASI 
# O SINO PONE OTRA IDEA PORQUE SOLO SE ME OCURRIO ESTA :c

def mostrar_matriz(matriz):
    size = (len(matriz[0])*40, len(matriz)*40)
    imagen = Image.new('RGB', size, color=(0, 0, 0))
    draw = ImageDraw.Draw(imagen)
    font_size = 32
    font = ImageFont.truetype("arial.ttf", font_size)
    cuadro_size = 40
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 'x':
                draw.text((j*cuadro_size, i*cuadro_size), 'x', font=font, fill=(255, 0, 0), stroke_width=1, stroke_fill=(255, 0, 0))
            elif matriz[i][j] == '0':
                draw.text((j*cuadro_size, i*cuadro_size), '0', font=font, fill=(0, 255, 0))
            elif matriz[i][j] == 'F':
                draw.text((j*cuadro_size, i*cuadro_size), 'F', font=font, fill=(0, 0, 255), stroke_width=2, stroke_fill=(0, 0, 255))
            elif matriz[i][j] == 'I':
                draw.text((j*cuadro_size, i*cuadro_size), 'I', font=font, fill=(0, 0, 255), stroke_width=2, stroke_fill=(0, 0, 255))
    # Muestra la imagen
    imagen.show()

matriz = generateMaze()
height = 10
width = 10
printMaze(matriz,height,width)
mostrar_matriz(matriz)
