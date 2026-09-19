from P3 import reescalamiento, comparar_original_escalado
import matplotlib.pyplot as plt
from skimage import io
import gc
import time

# Exp 1: Varios valores de S


def varios_s(valores_S: tuple, imagen="P3_IMG_2387_crop.tif"):
    ruta = "Test_Images/"
    file = ruta + imagen
    tipo_imagen = "RGB"
    modo_interpolacion = "bilineal"
    imagenes_procesadas = []
    for s in valores_S:
        if (type(s) != type(0.1)) and (type(s) != type(1)):
            raise ValueError(
                "Se espera que el arugmento de varios_s() sea una tupla con floats o int")
        imagen_escalada, imagen_original = reescalamiento(
            s, file, tipo_imagen, modo_interpolacion)
        io.imsave(
            f"{modo_interpolacion}_{imagen.split(".")[0]}_escalada_por_{s}.tif", imagen_escalada)
        io.imsave(
            f"{modo_interpolacion}_{imagen.split(".")[0]}_original.tif", imagen_original)
        imagenes_procesadas.append(imagen_escalada)
    s1, s2, s3, s4, s5 = valores_S
    imagen_1, imagen_2, imagen_3, imagen_4, imagen_5 = imagenes_procesadas
    fig, axes = plt.subplots(2, 3, figsize=(50, 30))
    ax1, ax2, ax3, ax4, ax5, ax6 = axes.flatten()
    ax1.imshow(imagen_original)
    ax1.set_title("Imagen Original")
    ax1.axis('off')
    ax2.imshow(imagen_1)
    ax2.set_title(f"Escalado por {s1}")
    ax2.axis('off')
    ax3.imshow(imagen_2)
    ax3.set_title(f"Escalado por {s2}")
    ax3.axis('off')
    ax4.imshow(imagen_3)
    ax4.set_title(f"Escalado por {s3}")
    ax4.axis("off")
    ax5.imshow(imagen_4)
    ax5.set_title(f"Escalado por {s4}")
    ax5.axis("off")
    ax6.imshow(imagen_5)
    ax6.set_title(f"Escalado por {s5}")
    ax6.axis("off")
    plt.tight_layout()
    plt.show()

# varios_s((0.1, 0.5, 0.7, 1.5, 2))

# Exp 2: Comparar vecino y bilineal


def varios_test(imagenes: tuple, varios_s=(0.3, 1.5), tipo_imagen="rgb"):
    ruta = "Test_Images/"
    modos = ("vecino", "bilineal")
    for imagen in imagenes:
        print(f"{"\n" * 100} TRABAJANDO IMAGEN {imagen}")
        file = ruta + imagen
        for s in varios_s:
            print(f"{"\n" * 100} TRABAJANDO s {s}")
            for modo in modos:
                imagen_escalada, imagen_original = reescalamiento(
                    s, file, tipo_imagen, modo)
                del imagen_original
                io.imsave(
                    f"{imagen.split(".")[0]}_{modo}_{s}.tif", imagen_escalada)
                del imagen_escalada
                gc.collect()

# varios_test(("im_bicipuerta.avif", "P3_IMG_2387_crop.tif", "im_cocina.jpg"))

# Exp 3: Dos imágenes

# varios_test(("im_ciudad.jpg", "im_venecia.avif"))

# Exp 4: Explorar reducción y ampliación


def explorar_s(imagenes: tuple, s: tuple):
    varios_test(imagenes, s)


# explorar_s(("im_ciudad.jpg", "hola.png"), (2, 1))

# Exp 5: Reducción y ampliación:

def perder_info(imagen: str):
    ruta = "Test_Images/"
    file = ruta + imagen
    tipo_imagen = "rgb"
    modos = ("vecino", "bilineal")
    s_min, s_max = 0.5, 2
    for modo in modos:
        print(f"{"\n" * 100} Calculando modo {modo}")
        imagen_deescalada, imagen_original = reescalamiento(
            s_min, file, tipo_imagen, modo)
        nombre_imagen_deescalada = f"{imagen}_escalada_por_{s_min}_modo_{modo}.tif"
        io.imsave(nombre_imagen_deescalada, imagen_deescalada)
        imagen_reescalada, imagen_orignal = reescalamiento(
            s_max, nombre_imagen_deescalada, tipo_imagen, modo)
        io.imsave(f"{imagen}_reescalada_por_{s_min}_y_{s_max}_modo_{modo}.tif",
                  imagen_reescalada)

# perder_info("im_venecia.avif")

# Exp 6: Escalados suvesivos vs 1 escalado


def escalados_sucesisvos(tupla_s: tuple, imagen: str):
    ruta = "Test_Images/"
    file_og = ruta + imagen
    tipo_imagen = "rgb"
    modos = ("vecino", "bilineal")
    s_max = 1
    for s in tupla_s:
        s_max *= s
    for modo in modos:
        s_acumulado = 1
        file = file_og
        for s in tupla_s:
            s_acumulado *= s
            print(s_max, s, s_acumulado)
            time.sleep(2)
            imagen_parcial, _ = reescalamiento(s, file, tipo_imagen, modo)
            file = f"{imagen.split(".")[0]}_parcial_{s_acumulado}_{modo}.tif"
            io.imsave(file, imagen_parcial)
            del imagen_parcial
            gc.collect()
        imagen_directa, _ = reescalamiento(
            s_max, file_og, tipo_imagen, modo)
        io.imsave(
            f"{imagen.split(".")[0]}_directo_{s_max}_{modo}.tif", imagen_directa)
        del imagen_directa
        gc.collect()

# escalados_sucesisvos((1.2, 1.3, 1.5), "im_venecia.avif")


# Exp 7: Perdida de estructuras finas
def perdida(imagen: str):
    ruta = "Test_Images/"
    file = ruta + imagen
    for s in (0.1, 0.2, 0.5, 0.8):
        img_name = imagen.split(".")[0]
        modos = ("bilineal", "vecino")
        for modo in modos:
            imagen_perdida, _ = reescalamiento(
                0.1, file, "rgb", modo)
            nombre = f"{img_name}_deescalado_{s}_{modo}.tif"
            io.imsave(nombre, imagen_perdida)
            del imagen_perdida
            gc.collect()


"""
for imagen in ("im_venecia.avif", "im_cocina.jpg", "im_ciudad.jpg"):
    perdida(imagen)
"""

# Exp 8:
# varios_test(("im_ciudad_ruido.png", "raiseerror"), 0.3, 0.5, 1.5, 1.7), "rgba")
