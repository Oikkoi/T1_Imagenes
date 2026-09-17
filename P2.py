import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from skimage import exposure  # Para las imágenes comparativas


def convertir_a_gray(dir_file: str):
    imagen = io.imread(dir_file)
    if len(imagen.shape) == 2:
        return imagen
    elif len(imagen.shape) == 3:
        return (color.rgb2gray(imagen) * 255).astype(np.uint8)
    elif len(imagen.shape) == 4:
        return (color.rgba2gray(imagen) * 255).astype(np.uint8)
    else:
        raise ValueError("La imagen no está en formato GrayScale, RGB, o RGBA")


def calcular_salto(tamaño_region: int, overlap_deseado: float):
    if overlap_deseado >= 1 or overlap_deseado < 0:
        raise ValueError(
            "Se espera que el overlap deseado sea un valor entre 0 y 1")
    overlap_pixeles = tamaño_region * overlap_deseado
    salto = int(tamaño_region - overlap_pixeles)
    if salto == 0:
        salto = 1
    return salto


def extraer_segmentos(imagen, tamaño_region: int, overlap_deseado: float):
    salto = calcular_salto(tamaño_region, overlap_deseado)
    y_max, x_max = imagen.shape
    for y in range(0, y_max, salto):
        for x in range(0, x_max, salto):
            b_sup = y
            b_inf = min(y + tamaño_region, y_max)
            b_izq = x
            b_der = min(x + tamaño_region, x_max)
            segmento = imagen[b_sup:b_inf, b_izq:b_der]
            yield segmento, (b_sup, b_inf, b_izq, b_der), (x, y)


def obtener_transformacion(segmento, factor_limite: float, num_bins=256):
    histograma, bordes = np.histogram(segmento, bins=num_bins, range=(0, 256))
    if factor_limite is not None:
        alto, ancho = segmento.shape
        promedio = (alto * ancho) / num_bins
        limite_real = int(promedio * factor_limite)
        histograma_cortado = np.clip(histograma, 0, limite_real)
    else:
        histograma_cortado = histograma
    diferencia = histograma - histograma_cortado
    exceso = np.sum(diferencia)
    histograma_redistribuido = histograma_cortado + (exceso / num_bins)
    cdf = np.cumsum(histograma_redistribuido)
    if cdf.max() > 0:
        cdf_normalizada = np.round(cdf * 255 / cdf.max()).astype(np.uint8)
    else:
        cdf_normalizada = np.zeros_like(cdf, dtype=np.uint8)
    return cdf_normalizada


def calcular_peso_ponderado(alto, ancho):
    techo_y = np.minimum(np.arange(alto), (alto - 1) - np.arange(alto)) + 1
    techo_x = np.minimum(np.arange(ancho), (ancho - 1) - np.arange(ancho)) + 1
    mascara_pesos = np.outer(techo_y, techo_x)
    return mascara_pesos


def mostrar_comparacion(imagen_inicial, imagen_final, tamaño_region):
    # Imagen global es la que se obtiene con la ecualización hecha por skimage
    imagen_eq_global = (exposure.equalize_hist(
        imagen_inicial) * 255).astype(np.uint8)
    imagen_clahe = (exposure.equalize_adapthist(
        imagen_inicial,
        kernel_size=(tamaño_region, tamaño_region),
        clip_limit=0.3
    ) * 255).astype(np.uint8)

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(15, 5))
    ax1.imshow(imagen_inicial, cmap='gray')
    ax1.set_title("Imagen Original")
    ax1.axis('off')
    ax2.imshow(imagen_final, cmap='gray')
    ax2.set_title("Resultado")
    ax2.axis('off')
    ax3.imshow(imagen_eq_global, cmap='gray')
    ax3.set_title("Ecualización global por Skimage")
    ax3.axis('off')
    ax4.imshow(imagen_clahe, cmap='gray')
    ax4.set_title("Ecualización CLAHE por Skimage")
    ax4.axis("off")
    plt.tight_layout()
    plt.show()
    return imagen_eq_global, imagen_final


def ecualizacion_local(file, tamaño_region, overlap_deseado, factor_limite=None):
    imagen_gray = convertir_a_gray(file)
    lienzo_pesos = np.zeros(imagen_gray.shape)
    lienzo_segmentos = np.zeros(imagen_gray.shape)
    if factor_limite == 0 or factor_limite == 0.0:
        factor_limite = None
    for segmento, (b_sup, b_inf, b_izq, b_der), (x, y) in extraer_segmentos(
            imagen_gray, tamaño_region, overlap_deseado):
        alto, ancho = segmento.shape
        mascara_peso_ponderado = calcular_peso_ponderado(alto, ancho)
        cdf_normalizada = obtener_transformacion(
            segmento, factor_limite)
        segmento_ecualizado = cdf_normalizada[segmento]
        segmento_ponderado = mascara_peso_ponderado * segmento_ecualizado
        lienzo_segmentos[b_sup:b_inf, b_izq:b_der] += segmento_ponderado
        lienzo_pesos[b_sup:b_inf, b_izq:b_der] += mascara_peso_ponderado
    lienzo_pesos = np.maximum(lienzo_pesos, 1)
    imagen_final = np.round((lienzo_segmentos / lienzo_pesos)).astype(np.uint8)
    return mostrar_comparacion(imagen_gray, imagen_final, tamaño_region)


if __name__ == "__main__":
    ruta = "Test_Images/"
    nombre_imagen = "P2_IMG_2423.tif"
    file = ruta + nombre_imagen

    tamaño_segmento = 128
    overlap = 0.8
    factor_limite = 55
    ecualizacion_local(file, tamaño_segmento, overlap, factor_limite)
