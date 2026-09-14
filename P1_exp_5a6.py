from P1 import ColorSaturation
import numpy as np


# Experimento 5
"""
ColorSaturation("LCH", "Test_Images/im_espectro_color.jpg",
                [(np.pi, 67)], "experimento_5.png", True)
"""

# Experimento 6
ListaHSV = [
    (0.0, 0),         # Rojo
    (0.09, 0),        # Naranja
    (0.18, 0),        # Amarillo
    (0.27, 0),        # Verde lima
    (0.36, 0),        # Verde
    (0.45, 0),        # Cian verdoso
    (0.54, 0),        # Cian
    (0.629, 0),
    (0.63, 1),        # Azul claro
    (0.631, 0),
    (0.72, 0),        # Azul
    (0.81, 0),        # Violeta
    (0.90, 0),        # Rosa
]

ColorSaturation("HSV", "Test_Images/im_espectro_color.jpg",
                ListaHSV, "exp_6.png", True)
