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


def Interpolacion_HSV(x, h_array, m_array):
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

    interpolada = Interpolacion_HSV(hue, h_array, m_array)
    nuevo_S = gm_S(saturacion, interpolada)
    imagen_hsv[:, :, 1] = nuevo_S
    imagen_rgb = color.hsv2rgb(imagen_hsv)
    return imagen_rgb


def Interpolacion_LCH(x, h_array, m_array):
    return np.interp(x, h_array, m_array, period=2*np.pi)


def gm_C(C, matriz_multiplicar):
    return np.clip(C*matriz_multiplicar, a_min=0, a_max=None)


def ColorSaturationLCH(file: str, lista_tuplas):
    h_array, m_array = formar_intervalos(lista_tuplas)

    # Definimos los tensores de RGB Y HSV
    imagen_rgb = io.imread(file)
    imagen_cie = color.rgb2lab(imagen_rgb)
    imagen_lch = color.lab2lch(imagen_cie)

    hue = imagen_lch[:, :, 2]
    croma = imagen_lch[:, :, 1]

    interpolada = Interpolacion_LCH(hue, h_array, m_array)
    nuevo_C = gm_C(croma, interpolada)
    imagen_lch[:, :, 1] = nuevo_C
    imagen_lab = color.lch2lab(imagen_lch)
    imagen_rgb = color.lab2rgb(imagen_lab)
    return imagen_rgb


def ColorSaturation(mode: str, file: str, lista_pares):
    if mode == "HS":
        imagen_rgb = ColorSaturationHSV(file, lista_pares)
    else:
        imagen_rgb = ColorSaturationLCH(file, lista_pares)
    plt.imshow(imagen_rgb)
    plt.imsave("resultado.png", imagen_rgb)
    plt.show()


if __name__ == "__main__":
    mode = "LCH"  # HS para HSV, cualquier otra cosa para LCH
    imagen = "test_image2.jpg"
    lista_pares = [(0, 1), (np.pi/2, 1), (np.pi, 1), (3*np.pi/4, 1)]
    ColorSaturation(mode, imagen, lista_pares)
