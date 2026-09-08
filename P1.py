import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color


def formar_intervalos(lista_tuplas):
    """El formato requerido para la función es una lista que
    contiene tuplas con los pares ordenados (h, m)"""
    puntos = sorted(lista_tuplas, key=lambda tupla: tupla[0])
    h_tupla, m_tupla = zip(*puntos)
    h_array = np.array(h_tupla)
    m_array = np.array(m_tupla)
    m_array = np.clip(m_array, a_min=0, a_max=None)
    return h_array, m_array


def interpolacion(x, h_array, m_array):
    # Gracias a la periodicidad de la función, no problemas de continuidad en 0 y 1 (ambos son rojo)
    return np.interp(x, h_array, m_array, period=1)


def gm_S(S, matriz_multiplicar):
    # En np, S*m si ambos son arrays del mismo tamaño es una multiplicación píxel a píxel
    return np.clip(S * matriz_multiplicar, 0, 1)


def ColorSaturationHSV(file: str, lista_tuplas):
    h_array, m_array = formar_intervalos(lista_tuplas)

    # Definimos los tensores de RGB Y HSV
    imagen_rgb = io.imread(file)
    imagen_hsv = color.rgb2hsv(imagen_rgb)

    # definimos el hue y la saturacion:
    hue = imagen_hsv[:, :, 0]
    saturacion = imagen_hsv[:, :, 1]

    interpolada = interpolacion(hue, h_array, m_array)
    nuevo_S = gm_S(saturacion, interpolada)
    imagen_hsv[:, :, 1] = nuevo_S
    imagen_rgb = color.hsv2rgb(imagen_hsv)
    return imagen_rgb
