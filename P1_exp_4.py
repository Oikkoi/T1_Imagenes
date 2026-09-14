from P1 import ColorSaturation
import numpy as np

ruta = "Test_Images/im_espectro_color.jpg"

"""
Para la experimentación propuesta en el apartado 4, 
vamos a usar distintas longitudes de escalamientos mixtos para HSV y LCH

En la experimentación anterior usé las siguientes listas:
Lista_HSV_Neutra = [
    (0.0, 1.0),    # Rojo
    (0.083, 1.0),  # Naranja
    (0.166, 1.0),  # Amarillo
    (0.333, 1.0),  # Verde
    (0.5, 1.0),    # Cian
    (0.666, 1.0),  # Azul
    (0.833, 1.0),  # Magenta
]

 Lista_LCH_Neutra = [
    (0, 1.0),          # Rojo
    (np.pi/4, 1.0),    # Naranja
    (np.pi/2, 1.0),    # Amarillo
    (np.pi, 1.0),      # Verde
    (5*np.pi/4, 1.0),  # Cian
    (3*np.pi/2, 1.0),  # Azul
    (7*np.pi/4, 1.0),  # Morado
]
Porque estimé que esos 7 colores eran más que suficientes para utilizar todo el espectro. 
En esta experimentación usaré listas bien distribuidas de 2, 3, 5, 7 (la ya usada antes) y 11 elementos
"""

Lista2_LCH = [
    (0, 0.5),          # Rojo
    (np.pi, 1.5),      # Verde
]
Lista2_HSV = [
    (0.0, 0.5),        # Rojo
    (0.5, 1.5),        # Cian
]
Lista3_LCH = [
    (0, 2.0),          # Rojo
    (2*np.pi/3, 0.3),  # Amarillo verdoso
    (4*np.pi/3, 1.2),  # Cyan-Azul
]
Lista3_HSV = [
    (0.0, 2.0),        # Rojo
    (0.333, 0.3),      # Verde
    (0.666, 1.2),      # Azul
]
Lista5_LCH = [
    (0, 0.0),          # Rojo
    (2*np.pi/5, 1.2),  # Naranja
    (4*np.pi/5, 0.5),  # Verde amarillento
    (6*np.pi/5, 2.0),  # Cian
    (8*np.pi/5, 0.8),  # Morado-Violeta
]
Lista5_HSV = [
    (0.0, 0.0),        # Rojo
    (0.2, 1.2),        # Amarillo verdoso
    (0.4, 0.5),        # Verde-cian
    (0.6, 2.0),        # Azul
    (0.8, 0.8),        # Magenta
]
Lista7_LCH = [
    (0, 1.0),          # Rojo
    (np.pi/4, 1.5),    # Naranja
    (np.pi/2, 0),    # Amarillo
    (np.pi, 3.0),      # Verde
    (5*np.pi/4, 0.0),  # Cian
    (3*np.pi/2, 4.1),  # Azul
    (7*np.pi/4, 3.0),  # Morado
]
Lista7_HSV = [
    (0.0, 1.0),    # Rojo
    (0.083, 1.5),  # Naranja
    (0.166, 0),  # Amarillo
    (0.333, 3.0),  # Verde
    (0.5, 0.0),    # Cian
    (0.666, 4.1),  # Azul
    (0.833, 3.0),  # Magenta
]
Lista11_LCH = [
    (0, 1.5),           # Rojo
    (2*np.pi/11, 0.8),  # Naranja rojizo
    (4*np.pi/11, 1.2),  # Amarillo
    (6*np.pi/11, 0.5),  # Amarillo verdoso
    (8*np.pi/11, 0.0),  # Verde
    (10*np.pi/11, 2.0),  # Verde azulado
    (12*np.pi/11, 1.0),  # Cian
    (14*np.pi/11, 0.7),  # Azul claro
    (16*np.pi/11, 1.8),  # Azul
    (18*np.pi/11, 0.3),  # Morado
    (20*np.pi/11, 1.1),  # Rosa
]
Lista11_HSV = [
    (0.0, 1.5),         # Rojo
    (0.09, 0.8),        # Naranja
    (0.18, 1.2),        # Amarillo
    (0.27, 0.5),        # Verde lima
    (0.36, 0.0),        # Verde
    (0.45, 2.0),        # Cian verdoso
    (0.54, 1.0),        # Cian
    (0.63, 0.7),        # Azul claro
    (0.72, 1.8),        # Azul
    (0.81, 0.3),        # Violeta
    (0.90, 1.1),        # Rosa
]

diccionario_listas = {
    "Lista2_HSV": Lista2_HSV,
    "Lista2_LCH": Lista2_LCH,
    "Lista3_HSV": Lista3_HSV,
    "Lista3_LCH": Lista3_LCH,
    "Lista5_HSV": Lista5_HSV,
    "Lista5_LCH": Lista5_LCH,
    "Lista7_HSV": Lista7_HSV,
    "Lista7_LCH": Lista7_LCH,
    "Lista11_HSV": Lista11_HSV,
    "Lista11_LCH": Lista11_LCH
}

for nombre_lista, valores_lista in diccionario_listas.items():
    if "HSV" in nombre_lista:
        mode = "HSV"
    elif "LCH" in nombre_lista:
        mode = "LCH"
    nombre_archivo = f"{nombre_lista.strip("Lista")}_puntos.png"
    ColorSaturation(mode, ruta, valores_lista, nombre_archivo)
    print(f"Procesada y guardada: {nombre_archivo}")
