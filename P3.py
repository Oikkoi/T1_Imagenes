import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color


def convertir_a_rgb(file: str, tipo: str):  # Cubre RGB, HSV, HSL, HSI y GrayScale
    # Ya que no puedo determinar el tipo de espacio de color de la imagen, lo pido como argumento
    imagen_og = io.imread(file)
    tipo = tipo.upper()
    if tipo == "RGB":
        imagen_rgb = imagen_og
    elif tipo == "HSV":
        imagen_rgb = color.hsv2rgb(imagen_og)
    elif tipo == "HSL":
        imagen_rgb = color.hsl2rgb(imagen_og)
    elif tipo == "HSI":
        imagen_rgb = color.hsi2rgb(imagen_og)
    elif tipo == "GRAYSCALE":
        imagen_rgb = color.gray2rgb(imagen_og)
    else:
        raise ValueError(
            "El tipo de imagen no es RGB, HSV, HSL, HSI ni GrayScale")
    return imagen_rgb


def generar_lienzo_salida(s: float, imagen_original):
    alto_og, ancho_og, _ = imagen_original.shape
    y_max, x_max = (int(np.ceil(alto_og*s)), int(np.ceil(ancho_og*s)))
    return np.zeros((y_max, x_max, 3)), (x_max, y_max)


def mapeo_inverso(coords: tuple, s: float):
    i, j = coords
    x = i / s
    y = j / s
    return (x, y)


def calcular_nuevas_coordenadas(coords_max: tuple, s: float, coords: tuple, modo: str):
    x, y = mapeo_inverso(coords, s)
    x_max, y_max = coords_max
    if modo == "vecino":
        x_p = min(int(np.round(x)), x_max)
        y_p = min(int(np.round(y)), y_max)
        return (x_p, y_p)
    elif modo == "bilineal":
        x0 = int(np.floor(x))
        y0 = int(np.floor(y))
        y1 = min(y0 + 1, y_max)
        x1 = min(x0 + 1, x_max)
        dy = y - y0
        dx = x - x0
        pesos_y = ((1-dy), dy)
        pesos_x = ((1-dx), dx)
        return pesos_x, pesos_y, (y0, x0, x1, y1)


def reescalamiento(s: float, file: str, tipo_imagen: str, modo_interpolacion: str):
    modo_interpolacion = modo_interpolacion.lower()
    opciones_validas = ("bilineal", "vecino")
    if modo_interpolacion not in opciones_validas:
        raise ValueError(
            "Opción de interpolación no válida. Reintentar con 'Bilineal' o 'Vecino'")
    imagen_rgb = convertir_a_rgb(file, tipo_imagen)
    y_max, x_max, _ = imagen_rgb.shape
    lienzo_vacio, (nuevo_ancho, nuevo_alto) = generar_lienzo_salida(
        s, imagen_rgb)
    for y in range(nuevo_alto):
        for x in range(nuevo_ancho):
            print(f"Trabajando pixel {(x, y)}")
            args = calcular_nuevas_coordenadas(
                (x_max-1, y_max-1), s, (x, y), modo_interpolacion)
            if modo_interpolacion == "bilineal":
                w_x, w_y, (y0, x0, x1, y1) = args
                p00 = imagen_rgb[y0, x0] * w_y[0] * w_x[0]
                p01 = imagen_rgb[y0, x1] * w_y[0] * w_x[1]
                p10 = imagen_rgb[y1, x0] * w_y[1] * w_x[0]
                p11 = imagen_rgb[y1, x1] * w_y[1] * w_x[1]
                color_final = p00 + p01 + p10 + p11
                lienzo_vacio[y, x] = color_final
            else:
                x_p, y_p = args
                lienzo_vacio[y, x] = imagen_rgb[y_p, x_p]
    return lienzo_vacio.astype(np.uint8), imagen_rgb


def comparar_original_escalado(imagen_original, imagen_escalada):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(50, 30))
    ax1.imshow(imagen_original)
    ax1.set_title("Imagen Original")
    ax1.axis('off')
    ax2.imshow(imagen_escalada)
    ax2.set_title("Resultado")
    ax2.axis('off')
    plt.show()


if __name__ == "__main__":
    ruta = "Test_Images/"
    imagen = "P3_IMG_2387_crop.tif"
    file = ruta + imagen
    s = 0.5
    tipo_imagen = "RGB"
    modo_interpolacion = "vecino"
    imagen_escalada, imagen_original = reescalamiento(
        s, file, tipo_imagen, modo_interpolacion)
    io.imsave(
        f"{modo_interpolacion}_{imagen.split(".")[0]}_escalada_por_{s}.tif", imagen_escalada)
    io.imsave(
        f"{modo_interpolacion}_{imagen.split(".")[0]}_original.tif", imagen_original)
    comparar_original_escalado(imagen_original, imagen_escalada)
