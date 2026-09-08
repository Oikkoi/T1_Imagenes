import numpy as np
import matplotlib.pyplot as plt
from skimage import io

m = 1


def gm_S(S, mm=m):
    """Me decidí por usar la transformación S' = S*m"""
    return np.clip(S * mm, 0, 1)


def aplicar_gm(imagen):
    img_hsv = color.rgb2hsv(imagen)
    """Se puede aislar según índice, H es 0, S es 1 y V es 2"""
    img_hsv[:, :, 1] = gm_S(img_hsv[:, :, 1], m)
    return img_hsv


def visualizar(imagen_hsv):
    img_rgb = color.hsv2rgb(img_hsv)
    """plt solo recibe rgb, si pongo plot de img_hsv sale una imagen verde"""
    plt.imshow(img_rgb)
    plt.show()
    return
