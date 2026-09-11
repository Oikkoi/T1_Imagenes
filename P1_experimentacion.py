from P1 import ColorSaturation
import numpy as np

"""
Comenzaré con el modo HSV. La primera configuración utilizada corresponde al archivo 
'resultado_HSV_aumentar.png", la segunda a 'resultado_HSV_disminuir.png" y la tercera a 
'resultado_HSV_mixto.png'. Más abajo se encuentran las líneas. El código fue pensado para ir comentando
las líneas que no corresponden al experimento.
Como referencia, en HSV:
Rojo = 0.0 = 1.0
Naranja = 0.083
Amarillo = 0.166
Verde = 0.333
Cyan-Verde = 0.416
Cyan = 0.500
Azul = 0.666
Morado = 0.750
Fucsia = 0.833
"""
# Lista RGB sin modificar para HSV:
# [(0, 1), (0.083, 1), (0.166, 1), (0.333, 1), (0.416, 1), (0.5, 1), (0.666, 1), (0.75, 1), (0.833, 1)]

lista_HSV_aumentar = [(0, 1), (0.083, 2), (0.166, 1), (0.333, 7),
                      (0.416, 1), (0.5, 3), (0.666, 67), (0.75, 10), (0.833, 1)]
"""
ColorSaturation(mode="HSV", file="test_image.jpg",
                lista_pares=lista_HSV_aumentar)
"""
lista_HSV_disminuir = [(0, 0), (0.083, 0.2), (0.166, 0.4), (0.333, 0.6),
                       (0.416, 0.8), (0.5, 1), (0.666, 0.8), (0.75, 0.6), (0.833, 0.4)]
"""
ColorSaturation(mode="HSV", file="test_image.jpg",
                lista_pares=lista_HSV_disminuir)
"""

lista_HSV_mixta = [(0, 0), (0.083, 0.5), (0.166, 3), (0.333, 1),
                   (0.416, 0), (0.5, 0), (0.666, 7), (0.75, 0.3), (0.833, 0.1)]
"""
ColorSaturation(mode="HSV", file="test_image.jpg",
                lista_pares=lista_HSV_mixta)
"""

"""
Traté de más o menos tomar los colores de la lista anterior en LCH viendo una imagen, así que me disculpo de antemano si no funciona.
"""
# Lista LCH sin modificar:
# [(0, 1), (np.pi/6, 1), (2*np.pi/6, 1), (3*np.pi/6, 1), (4*np.pi/6, 1), (5*np.pi/6, 1), (6*np.pi/6, 1), (7*np.pi/6, 1), (8*np.pi/6, 1), (9*np.pi/6, 1), (10*np.pi/6, 1), (11*np.pi/6, 1), (12*np.pi/6, 1)]
lista_LCH_aumentar = [(0, 1), (np.pi/6, 2), (2*np.pi/6, 1), (3*np.pi/6, 1), (4*np.pi/6, 1), (5*np.pi/6, 4),
                      (6*np.pi/6, 1), (7*np.pi/6, 1), (8*np.pi/6, 8), (9*np.pi/6, 4), (10*np.pi/6, 1), (11*np.pi/6, 1)]
# ColorSaturation("LCH", "test_image.jpg", lista_LCH_aumentar)

lista_LCH_disminuir = [(0, 0.3), (np.pi/6, 1), (2*np.pi/6, 0.5), (3*np.pi/6, 1), (4*np.pi/6, 0.6), (5*np.pi/6, 0.88),
                       (6*np.pi/6, 1), (7*np.pi/6, 1), (8*np.pi/6, 0.5), (9*np.pi/6, 1), (10*np.pi/6, 1), (11*np.pi/6, 0.67)]
# ColorSaturation("LCH", "test_image.jpg", lista_LCH_disminuir)

lista_LCH_mixta = [(0, 0.3), (np.pi/6, 1), (2*np.pi/6, 1), (3*np.pi/6, 0.1), (4*np.pi/6, 1), (5*np.pi/6, 2), (6*np.pi/6, 1),
                   (7*np.pi/6, 1), (8*np.pi/6, 1), (9*np.pi/6, 1), (10*np.pi/6, 1), (11*np.pi/6, 1), (12*np.pi/6, 5000)]
ColorSaturation("LCH", "test_image.jpg", lista_LCH_mixta)
