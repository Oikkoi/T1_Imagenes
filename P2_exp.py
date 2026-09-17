from P2 import ecualizacion_local, convertir_a_gray, calcular_salto, extraer_segmentos, obtener_transformacion, calcular_peso_ponderado, mostrar_comparacion
from skimage import io, color, exposure
import matplotlib.pyplot as plt
import numpy as np


def mostrar_comparacion_variado(imagen_inicial, lista_imagenes, nombre_variable: str):
    imagen_1, imagen_2, imagen_3, imagen_4, imagen_5 = lista_imagenes
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    ax1, ax2, ax3, ax4, ax5, ax6 = axes.flatten()
    ax1.imshow(imagen_inicial, cmap='gray')
    ax1.set_title("Imagen Original")
    ax1.axis('off')
    ax2.imshow(imagen_1, cmap='gray')
    ax2.set_title(f"{nombre_variable}_1")
    ax2.axis('off')
    ax3.imshow(imagen_2, cmap='gray')
    ax3.set_title(f"{nombre_variable}_2")
    ax3.axis('off')
    ax4.imshow(imagen_3, cmap='gray')
    ax4.set_title(f"{nombre_variable}_3")
    ax4.axis("off")
    ax5.imshow(imagen_4, cmap='gray')
    ax5.set_title(f"{nombre_variable}_4")
    ax5.axis("off")
    ax6.imshow(imagen_5, cmap='gray')
    ax6.set_title(f"{nombre_variable}_5")
    ax6.axis("off")
    plt.tight_layout()
    plt.show()

# Exp 1: Demostrar la ecualización global:


def ec_global():
    ruta = "Test_Images/"
    imagen = "P2_IMG_2423.tif"
    file = ruta + imagen
    imagen_gray = convertir_a_gray(file)
    alto, ancho = imagen_gray.shape
    tamaño_segmento = max(alto, ancho)
    overlap = 0.5
    factor_limite = 40
    eq_global, resultado = ecualizacion_local(
        file, tamaño_segmento, overlap, factor_limite)
    io.imsave("Eq_global.tif", eq_global)
    io.imsave("Mi_eq_global.tif", resultado)


# ec_global()

"""Nota: En la visualización, la imagen hecha con CLAHE también se verá igual a la
ecualización global porque depende del tamaño del segmento que le demos como argumento"""


# Exp 2 (Overlap y Tamaño de región):


def varios_overlap(overlap_1, overlap_2, overlap_3, overlap_4, overlap_5):
    ruta = "Test_Images/"
    imagen = "P2_IMG_2423.tif"
    file = ruta + imagen
    tamaño_region = 128
    factor_limite = 55
    overlaps = (overlap_1, overlap_2, overlap_3, overlap_4, overlap_5)

    def ecualizacion_local_overlaps(file, tamaño_region, overlaps: tuple, factor_limite=None):
        imagen_gray = convertir_a_gray(file)
        if factor_limite == 0 or factor_limite == 0.0:
            factor_limite = None
        imagenes = []
        for overlap_deseado in overlaps:
            print(f"calculando {overlap_deseado}")
            lienzo_pesos = np.zeros(imagen_gray.shape)
            lienzo_segmentos = np.zeros(imagen_gray.shape)
            for segmento, (b_sup, b_inf, b_izq, b_der), (x, y) in extraer_segmentos(
                    imagen_gray, tamaño_region, overlap_deseado):
                print(f"calculando el segmento ({x}, {y})")
                alto, ancho = segmento.shape
                mascara_peso_ponderado = calcular_peso_ponderado(alto, ancho)
                cdf_normalizada = obtener_transformacion(
                    segmento, factor_limite)
                segmento_ecualizado = cdf_normalizada[segmento]
                segmento_ponderado = mascara_peso_ponderado * segmento_ecualizado
                lienzo_segmentos[b_sup:b_inf,
                                 b_izq:b_der] += segmento_ponderado
                lienzo_pesos[b_sup:b_inf,
                             b_izq:b_der] += mascara_peso_ponderado
            lienzo_pesos = np.maximum(lienzo_pesos, 1)
            imagen_final = np.round(
                (lienzo_segmentos / lienzo_pesos)).astype(np.uint8)
            imagenes.append(imagen_final)
            nombre_salida = f"Resultado_overlap_{overlap_deseado}.tif"
            io.imsave(nombre_salida, imagen_final)
        mostrar_comparacion_variado(imagen_gray, imagenes, "Overlap")

    ecualizacion_local_overlaps(file, tamaño_region, overlaps, factor_limite)


# varios_overlap(0.2, 0.4, 0.6, 0.8, 0.99)


def varios_tamaños(tamaño_1, tamaño_2, tamaño_3, tamaño_4, tamaño_5):
    ruta = "Test_Images/"
    imagen = "P2_IMG_2423.tif"
    file = ruta + imagen
    overlap = 0.8
    factor_limite = 55
    tamaños = (tamaño_1, tamaño_2, tamaño_3, tamaño_4, tamaño_5)

    def ecualizacion_local_tamaños(file, tamaños: tuple, overlap, factor_limite=None):
        imagen_gray = convertir_a_gray(file)
        if factor_limite == 0 or factor_limite == 0.0:
            factor_limite = None
        imagenes = []
        for tamaño_region in tamaños:
            print(f"calculando {tamaño_region}")
            lienzo_pesos = np.zeros(imagen_gray.shape)
            lienzo_segmentos = np.zeros(imagen_gray.shape)
            for segmento, (b_sup, b_inf, b_izq, b_der), (x, y) in extraer_segmentos(
                    imagen_gray, tamaño_region, overlap):
                print(f"calculando el segmento ({x}, {y})")
                alto, ancho = segmento.shape
                mascara_peso_ponderado = calcular_peso_ponderado(alto, ancho)
                cdf_normalizada = obtener_transformacion(
                    segmento, factor_limite)
                segmento_ecualizado = cdf_normalizada[segmento]
                segmento_ponderado = mascara_peso_ponderado * segmento_ecualizado
                lienzo_segmentos[b_sup:b_inf,
                                 b_izq:b_der] += segmento_ponderado
                lienzo_pesos[b_sup:b_inf,
                             b_izq:b_der] += mascara_peso_ponderado
            lienzo_pesos = np.maximum(lienzo_pesos, 1)
            imagen_final = np.round(
                (lienzo_segmentos / lienzo_pesos)).astype(np.uint8)
            imagenes.append(imagen_final)
            nombre_salida = f"Resultado_tamaño_{tamaño_region}.tif"
            io.imsave(nombre_salida, imagen_final)
        mostrar_comparacion_variado(imagen_gray, imagenes, "Tamaño")

    ecualizacion_local_tamaños(file, tamaños, overlap, factor_limite)

# varios_tamaños(32, 64, 128, 256, 512)


# Exp 3: Bins
def varios_bins(bins_1, bins_2, bins_3, bins_4, bins_5):
    ruta = "Test_Images/"
    imagen = "P2_IMG_2423.tif"
    file = ruta + imagen
    tamaño_region = 128
    factor_limite = 55
    overlap = 0.8
    bins = (bins_1, bins_2, bins_3, bins_4, bins_5)

    def ecualizacion_local_bins(file, tamaño_region, overlap, bins, factor_limite):
        imagen_gray = convertir_a_gray(file)
        if factor_limite == 0 or factor_limite == 0.0:
            factor_limite = None
        imagenes = []
        for bin_deseado in bins:
            print(f"calculando {bin_deseado}")
            lienzo_pesos = np.zeros(imagen_gray.shape)
            lienzo_segmentos = np.zeros(imagen_gray.shape)
            for segmento, (b_sup, b_inf, b_izq, b_der), (x, y) in extraer_segmentos(
                    imagen_gray, tamaño_region, overlap):
                print(f"calculando el segmento ({x}, {y})")
                alto, ancho = segmento.shape
                mascara_peso_ponderado = calcular_peso_ponderado(alto, ancho)
                cdf_normalizada = obtener_transformacion(
                    segmento, factor_limite, bin_deseado)
                indices_bins = np.clip(
                    (segmento / 256 * bin_deseado).astype(int), 0, bin_deseado - 1)
                segmento_ecualizado = cdf_normalizada[indices_bins]
                segmento_ponderado = mascara_peso_ponderado * segmento_ecualizado
                lienzo_segmentos[b_sup:b_inf,
                                 b_izq:b_der] += segmento_ponderado
                lienzo_pesos[b_sup:b_inf,
                             b_izq:b_der] += mascara_peso_ponderado
            lienzo_pesos = np.maximum(lienzo_pesos, 1)
            imagen_final = np.round(
                (lienzo_segmentos / lienzo_pesos)).astype(np.uint8)
            imagenes.append(imagen_final)
            nombre_salida = f"Resultado_bin_{bin_deseado}.tif"
            io.imsave(nombre_salida, imagen_final)
        mostrar_comparacion_variado(imagen_gray, imagenes, "Bin")
    ecualizacion_local_bins(file, tamaño_region, overlap, bins, factor_limite)


# varios_bins(1, 128, 256, 512, 1024)


# Exp 5: Varios Fcatores Limite
def varios_factor_limite(factor1, factor2, factor3, factor4, factor5):
    ruta = "Test_Images/"
    imagen = "P2_IMG_2423.tif"
    file = ruta + imagen
    tamaño_region = 128
    factores = (factor1, factor2, factor3, factor4, factor5)
    overlap = 0.8

    def ecualizacion_local_factores(file, tamaño, overlap, factores: tuple):
        imagen_gray = convertir_a_gray(file)
        imagenes = []
        for factor_limite in factores:
            if factor_limite == 0 or factor_limite == 0.0:
                factor_limite = None
            print(f"calculando {factor_limite}")
            lienzo_pesos = np.zeros(imagen_gray.shape)
            lienzo_segmentos = np.zeros(imagen_gray.shape)
            for segmento, (b_sup, b_inf, b_izq, b_der), (x, y) in extraer_segmentos(
                    imagen_gray, tamaño_region, overlap):
                print(f"calculando el segmento ({x}, {y})")
                alto, ancho = segmento.shape
                mascara_peso_ponderado = calcular_peso_ponderado(
                    alto, ancho)
                cdf_normalizada = obtener_transformacion(
                    segmento, factor_limite)
                segmento_ecualizado = cdf_normalizada[segmento]
                segmento_ponderado = mascara_peso_ponderado * segmento_ecualizado
                lienzo_segmentos[b_sup:b_inf,
                                 b_izq:b_der] += segmento_ponderado
                lienzo_pesos[b_sup:b_inf,
                             b_izq:b_der] += mascara_peso_ponderado
            lienzo_pesos = np.maximum(lienzo_pesos, 1)
            imagen_final = np.round(
                (lienzo_segmentos / lienzo_pesos)).astype(np.uint8)
            imagenes.append(imagen_final)
            nombre_salida = f"Resultado_factor_{factor_limite}.tif"
            io.imsave(nombre_salida, imagen_final)
        mostrar_comparacion_variado(imagen_gray, imagenes, "Factor_Limite")

    ecualizacion_local_factores(file, tamaño_region, overlap, factores)


# varios_factor_limite(1, 25, 50, 100, 200)


# Exp 6: Varias configuraciones:
def varias_config():
    def mostrar_comparacion_configs(imagenes, imagenes_clahe):
        imagen_1, imagen_2, imagen_3, imagen_4, imagen_5 = imagenes
        imagen_c1, imagen_c2, imagen_c3, imagen_c4, imagen_c5 = imagenes_clahe
        fig, axes = plt.subplots(2, 5, figsize=(18, 10))
        ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10 = axes.flatten()
        ax1.imshow(imagen_1, cmap='gray')
        ax1.set_title("Config 1")
        ax1.axis('off')
        ax2.imshow(imagen_2, cmap='gray')
        ax2.set_title("Config 2")
        ax2.axis('off')
        ax3.imshow(imagen_3, cmap='gray')
        ax3.set_title("Config 3")
        ax3.axis('off')
        ax4.imshow(imagen_4, cmap='gray')
        ax4.set_title("Config 4")
        ax4.axis("off")
        ax5.imshow(imagen_5, cmap='gray')
        ax5.set_title("Config 5")
        ax5.axis("off")
        ax6.imshow(imagen_c1, cmap='gray')
        ax6.set_title("Clahe 1")
        ax6.axis('off')
        ax7.imshow(imagen_c2, cmap='gray')
        ax7.set_title("Clahe 2")
        ax7.axis('off')
        ax8.imshow(imagen_c3, cmap='gray')
        ax8.set_title("Clahe 3")
        ax8.axis('off')
        ax9.imshow(imagen_c4, cmap='gray')
        ax9.set_title("Clahe 4")
        ax9.axis("off")
        ax10.imshow(imagen_c5, cmap='gray')
        ax10.set_title("Clahe 5")
        ax10.axis("off")
        plt.tight_layout()
        plt.show()

    configs = [{
        "tamaño": 16,
        "overlap": 0.2,
        "factor": 50
    }, {
        "tamaño": 64,
        "overlap": 0.8,
        "factor": 600
    }, {
        "tamaño": 128,
        "overlap": 0.5,
        "factor": 55
    }, {
        "tamaño": 128,
        "overlap": 0.5,
        "factor": None

    }, {
        "tamaño": 512,
        "overlap": 0.2,
        "factor": 100
    }]
    ruta = "Test_Images/"
    imagenes = ["im_bicipuerta.avif", "im_cocina.jpg"]
    file1 = ruta + "P2_IMG_2423.tif"
    for j, img in enumerate(imagenes):
        try:
            file = ruta + img
        except:
            raise FileNotFoundError("No existe el archivo")
        imagen_gray = convertir_a_gray(file)
        imagenes_clahe = []
        imagenes_listas = []
        for i, config in enumerate(configs):
            print(f"{"\n"*100}Realizando config {i+1}, imagen {j+1}")
            tamaño_region = config["tamaño"]
            overlap = config["overlap"]
            factor_limite = config["factor"]

            imagen_clahe = (exposure.equalize_adapthist(
                imagen_gray,
                kernel_size=(tamaño_region, tamaño_region),
                clip_limit=0.3
            ) * 255).astype(np.uint8)
            imagenes_clahe.append(imagen_clahe)

            if factor_limite == 0 or factor_limite == 0.0:
                factor_limite = None

            lienzo_pesos = np.zeros(imagen_gray.shape)
            lienzo_segmentos = np.zeros(imagen_gray.shape)

            for segmento, (b_sup, b_inf, b_izq, b_der), (x, y) in extraer_segmentos(
                    imagen_gray, tamaño_region, overlap):
                print(f"calculando el segmento ({x}, {y})")
                alto, ancho = segmento.shape
                mascara_peso_ponderado = calcular_peso_ponderado(
                    alto, ancho)
                cdf_normalizada = obtener_transformacion(
                    segmento, factor_limite)
                segmento_ecualizado = cdf_normalizada[segmento]
                segmento_ponderado = mascara_peso_ponderado * segmento_ecualizado
                lienzo_segmentos[b_sup:b_inf,
                                 b_izq:b_der] += segmento_ponderado
                lienzo_pesos[b_sup:b_inf,
                             b_izq:b_der] += mascara_peso_ponderado
            lienzo_pesos = np.maximum(lienzo_pesos, 1)
            imagen_final = np.round(
                (lienzo_segmentos / lienzo_pesos)).astype(np.uint8)
            imagenes_listas.append(imagen_final)
            nombre_salida = img.split(".")[0]
            io.imsave(f"{nombre_salida}_config{i}.tif", imagen_final)
            io.imsave(f"Clahe_{nombre_salida}_config{i}.tif", imagen_clahe)
        mostrar_comparacion_configs(imagenes_listas, imagenes_clahe)


# varias_config()


# Exp 7: Resultado Indeseable
def resultado_indeseable():
    ruta = "Test_Images/"
    file = ruta + "P2_IMG_2423.tif"

    tamaño_region = 128
    overlap = 0.5
    factor_limite = 55

    def mostrar_comparacion_indeseada(imagen_inicial, lista_imagenes):
        imagen_1, imagen_2, imagen_3 = lista_imagenes
        fig, axes = plt.subplots(2, 2, figsize=(18, 10))
        ax1, ax2, ax3, ax4 = axes.flatten()
        ax1.imshow(imagen_inicial, cmap='gray')
        ax1.set_title("Imagen Original")
        ax1.axis('off')
        ax2.imshow(imagen_1, cmap='gray')
        ax2.set_title("Imagen sin Factor Limitante")
        ax2.axis('off')
        ax3.imshow(imagen_2, cmap='gray')
        ax3.set_title("Imagen con Factor Limitante")
        ax3.axis('off')
        ax4.imshow(imagen_3, cmap='gray')
        ax4.set_title("Imagen CLAHE")
        ax4.axis("off")
        plt.tight_layout()
        plt.show()

    def ecualizacion_local_indeseada(file, tamaño_region, overlap, factor_limite=None):
        imagen_gray = convertir_a_gray(file)
        lienzo_pesos = np.zeros(imagen_gray.shape)
        lienzo_segmentos = np.zeros(imagen_gray.shape)
        if factor_limite == 0 or factor_limite == 0.0:
            factor_limite = None
        for segmento, (b_sup, b_inf, b_izq, b_der), (x, y) in extraer_segmentos(
                imagen_gray, tamaño_region, overlap):
            alto, ancho = segmento.shape
            mascara_peso_ponderado = calcular_peso_ponderado(alto, ancho)
            cdf_normalizada = obtener_transformacion(
                segmento, factor_limite)
            segmento_ecualizado = cdf_normalizada[segmento]
            segmento_ponderado = mascara_peso_ponderado * segmento_ecualizado
            lienzo_segmentos[b_sup:b_inf, b_izq:b_der] += segmento_ponderado
            lienzo_pesos[b_sup:b_inf, b_izq:b_der] += mascara_peso_ponderado
        lienzo_pesos = np.maximum(lienzo_pesos, 1)
        imagen_final = np.round(
            (lienzo_segmentos / lienzo_pesos)).astype(np.uint8)
        return imagen_final

    imagen_original = convertir_a_gray(file)
    io.imsave("Imagen_OG.tif", imagen_original)

    imagen_indeseada = ecualizacion_local_indeseada(
        file, tamaño_region, overlap)
    io.imsave("Imagen_indeseada.tif", imagen_indeseada)
    imagen_clahe = (exposure.equalize_adapthist(
        imagen_original,
        kernel_size=(tamaño_region, tamaño_region),
        clip_limit=0.3
    ) * 255).astype(np.uint8)
    io.imsave("Imagen_CLAHE.tif", imagen_clahe)
    imagen_deseada = ecualizacion_local_indeseada(
        file, tamaño_region, overlap, factor_limite)
    io.imsave("Imagen_con_limite.tif", imagen_deseada)
    mostrar_comparacion_indeseada(
        imagen_original, [imagen_indeseada, imagen_deseada, imagen_clahe])


# resultado_indeseable()


# Exp8: Experimento Personal

"""Decidí ver qué pasa si comparo una imagen RGB aplicando el mismo 
algoritmo que diseñé a sus tres canales de forma independiente, versus aplicarlo al canal 
V de HSV"""


def experimento_personal():
    ruta = "Test_Images/"
    imagen = "im_bicipuerta.avif"
    file = ruta + imagen
    imagen_original = io.imread(file)

    tamaño_region = 128
    overlap = 0.8
    factor = 55

    def algoritmo(matriz, tamaño, overlap, factor):
        lienzo_pesos = np.zeros(matriz.shape)
        lienzo_segmentos = np.zeros(matriz.shape)
        for segmento, (b_sup, b_inf, b_izq, b_der), (x, y) in extraer_segmentos(matriz, tamaño, overlap):
            alto, ancho = segmento.shape
            mascara = calcular_peso_ponderado(alto, ancho)
            cdf = obtener_transformacion(segmento, factor)
            segmento_ponderado = mascara * cdf[segmento]
            lienzo_segmentos[b_sup:b_inf, b_izq:b_der] += segmento_ponderado
            lienzo_pesos[b_sup:b_inf, b_izq:b_der] += mascara
        lienzo_pesos = np.maximum(lienzo_pesos, 1)
        return np.round(lienzo_segmentos/lienzo_pesos).astype(np.uint8)
    img_rgb_eq = np.zeros(imagen_original.shape)
    for i in range(3):
        img_rgb_eq[:, :, i] = algoritmo(
            imagen_original[:, :, i], tamaño_region, overlap, factor)
    img_hsv = color.rgb2hsv(imagen_original)
    canal_v = (img_hsv[:, :, 2] * 255).astype(np.uint8)
    canal_v_eq = algoritmo(canal_v, tamaño_region, overlap, factor)
    img_hsv[:, :, 2] = canal_v_eq / 255.0
    img_hsv_resultado = (color.hsv2rgb(img_hsv) * 255).astype(np.uint8)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    ax1.imshow(imagen_original)
    ax1.set_title("Original RGB")
    io.imsave("Orignal_RGB.tif", imagen_original)
    ax1.axis('off')
    ax2.imshow(img_rgb_eq)
    ax2.set_title("Canales RGB separados")
    io.imsave("RGB_Transformado.tif", img_rgb_eq)
    ax2.axis('off')
    ax3.imshow(img_hsv_resultado)
    ax3.set_title("Solo Value")
    io.imsave("HSV_Transformado.tif", img_hsv_resultado)
    ax3.axis('off')
    plt.tight_layout()
    plt.show()


experimento_personal()
