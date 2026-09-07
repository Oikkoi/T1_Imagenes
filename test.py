import numpy as np
import matplotlib.pyplot as plt
from skimage import io

imagen = io.imread("test_image.png")
print("Imagen cargada")
img_plot = plt.imshow(imagen)
print("Se supone que muestra")
plt.show()
