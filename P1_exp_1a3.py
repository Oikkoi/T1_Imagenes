from P1 import ColorSaturation
import numpy as np

ruta = "Test_Images/P4_IMG_2267_CFA.tif"

"""
Este código fue hecho para resolver la sección de Experimentación en el enunciado de la pregunta 1. 
Fue hecho pensando en hacer ejecuciones en serie para cada imagen y guardar su resultado. 

Las imágenes resultado de las modificaciones análogas (como indica el punto 3) serán guardados en P1_ResultadosExperimentos/,
la siguiente carpeta es el nombre de la imagen de las que están disponibles en Test_Images/

Lista_HSV_Neutra = [
    (0.0, 1.0),    # Rojo
    (0.083, 1.0),  # Naranja
    (0.166, 1.0),  # Amarillo
    (0.333, 1.0),  # Verde
    (0.5, 1.0),    # Cian
    (0.666, 1.0),  # Azul
    (0.833, 1.0),  # Magenta
]
Lista_LCH_Neutra = [
    (0, 1.0),          # Rojo
    (np.pi/4, 1.0),    # Naranja
    (np.pi/2, 1.0),    # Amarillo
    (np.pi, 1.0),      # Verde
    (5*np.pi/4, 1.0),  # Cian
    (3*np.pi/2, 1.0),  # Azul
    (7*np.pi/4, 1.0),  # Morado
]
"""

lista_HSV_aumentar = [
    (0.0, 1.0),    # Rojo
    (0.083, 2.0),  # Naranja
    (0.166, 1.0),  # Amarillo
    (0.333, 1.0),  # Verde
    (0.5, 8.0),    # Cian
    (0.666, 1.5),  # Azul
    (0.833, 2.0),  # Magenta
]

ColorSaturation("HSV", ruta, lista_HSV_aumentar, "HSV_aumentar.png")

lista_LCH_aumentar = [
    (0, 1.0),          # Rojo
    (np.pi/4, 2.0),    # Naranja
    (np.pi/2, 1.0),    # Amarillo
    (np.pi, 3.0),      # Verde
    (5*np.pi/4, 8.0),  # Cian
    (3*np.pi/2, 1.5),  # Azul
    (7*np.pi/4, 2.0),  # Morado / Violeta
]

ColorSaturation("LCH", ruta, lista_LCH_aumentar, "LCH_aumentar.png")

lista_HSV_disminuir = [
    (0.0, 0),      # Rojo
    (0.083, 1.0),  # Naranja
    (0.166, 0.5),  # Amarillo
    (0.333, 0.3),  # Verde
    (0.5, 1.0),    # Cian
    (0.666, 0),    # Azul
    (0.833, 1.0),  # Magenta
]

ColorSaturation("HSV", ruta, lista_HSV_disminuir, "HSV_disminuir.png")

lista_LCH_disminuir = [
    (0, 0),          # Rojo
    (np.pi/4, 1.0),    # Naranja
    (np.pi/2, 0.5),    # Amarillo
    (np.pi, 0.3),      # Verde
    (5*np.pi/4, 1.0),  # Cian
    (3*np.pi/2, 0),  # Azul
    (7*np.pi/4, 1.0),  # Morado / Violeta
]

ColorSaturation("LCH", ruta, lista_LCH_disminuir, "LCH_diminuir.png")

lista_HSV_mixta = [
    (0.0, 0),      # Rojo
    (0.083, 0.3),  # Naranja
    (0.166, 1.6),  # Amarillo
    (0.333, 2),    # Verde
    (0.5, 0.4),    # Cian
    (0.666, 3),    # Azul
    (0.833, 0),    # Magenta
]

ColorSaturation("HSV", ruta, lista_HSV_mixta, "HSV_mixto.png")

lista_LCH_mixta = [
    (0, 0),          # Rojo
    (np.pi/4, 0.3),    # Naranja
    (np.pi/2, 1.6),    # Amarillo
    (np.pi, 2),      # Verde
    (5*np.pi/4, 0.4),  # Cian
    (3*np.pi/2, 3),  # Azul
    (7*np.pi/4, 0),  # Morado / Violeta
]

ColorSaturation("LCH", ruta, lista_LCH_mixta, "LCH_mixto.png")
