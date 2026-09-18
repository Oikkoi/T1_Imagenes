from P3 import reescalamiento, comparar_original_escalado
import matplotlib.pyplot as plt
from skimage import io

# Exp 1: Varios valores de S


def varios_s(valores_S: tuple):
    ruta = "Test_Images/"
    imagen = "P3_IMG_2387_crop.tif"
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

def varios_test():
    ruta = "Test_Images/"
    imagenes = ("im_bicipuerta.avif, P3_IMG_2387_crop.tif", "im_cocina.jpg")
    varios_s = (0.3, 1.5)
    tipo_imagen = "rgb"
    modos = ("vecino", "bilineal")
    for modo in modos:
        for imagen in imagenes:
            imagenes_procesadas = []
            for s in varios_s:
                file = ruta + imagen
                imagen_escalada, imagen_original = reescalamiento(
                    s, file, tipo_imagen, modo)
                io.imsave(
                    f"{modo}_{imagen.split(".")[0]}_escalada_por_{s}.tif", imagen_escalada)
                io.imsave(
                    f"{modo}_{imagen.split(".")[0]}_original.tif", imagen_original)
                imagenes_procesadas.append(imagen_escalada)
            imagen_1, imagen_2, imagen_3, imagen_4, imagen_5, imagen_6 = imagenes_procesadas
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
