# P1 (`P1.py`):
**Para hacer esta pregunta, fueron utilizadas las librerías `numpy`, `matplotlib` y `skimage`.**

Para definidas las siguientes funciones:
1. *formar_intervalos*: Recibe como argumento una lista de tuplas, en formato `(h_i, m_i)` y retorna los arrays de los *hue* y los pesos *m* ordenados. (Es decir, la posición i en ambos array corresponde al par ordenado `h_i`, `m_i`). Para hacerlo, utiliza la función `numpy.array()` para convertir las listas unzipped en arrays. Retorna dichos arrays.
2. *Interpolacion_HSV*: Recibe como argumento la matriz de hue de la imagen HSV y ambos arrays obtenidos en la función *formar_intervalos*. Retorna la matriz de pesos post interpolación. Para hacerlo, utiliza la función `numpy.interp()`, en particular utilizando el parámetro *period* para no tener problemas con las discontinuidades. Retorna la matriz de pesos.
3. *gm_S*: Recibe la imagen HSV y la matriz de pesos obtenida en la función *Interpolacion_HSV*. Utiliza la función `numpy.clip()` para limitar los valores del producto S*M (píxel a píxel) a 1, ya que la saturación en la librería `skimage` viene normalizada. Retorna la nueva matriz de saturación.
4. *ColorSaturationHSV*: Recibe el nombre del archivo en *str* y la lista de pares ordenados (`h_i`, `m_i`). Usando el módulo `io` de `skimage` (en particular, la función `imread`) se obtiene el tensor de la imagen; luego usando el módulo `color` se usa la función `rgb2hsv` para convertir dicho tensor a HSV. Luego llama a las funciones anteriores para obtener los parámetros requeridos, luego sobrescribe la matriz de Hue obtenida en *gm_S* en la imagen HSV, la convierte en rgb otra vez usando la función `hsv2rgb` del módulo `color` de `skimage`. Finalmente retorna el tensor de la nueva imagen RGB.
5. *Interpolacion_LCH*: Recibe como argumento la máscara de croma y los arrays de hue y pesos. De manera similar a *Interpolacion_HSV*, usa la función `numpy.interp` para determinar la matriz de pesos según el croma. Utiliza un período de 2π en lugar de 1. Retorna la matriz de pesos.
6. *gm_C*: Recibe como argumentos la matriz de Croma y la matriz de pesos. De manera similar a *gm_S*, aplica la transformación C*M  y utiliza la función `numpy.clip` para asegurarse de que no den valores de saturación negativos. Retorna la nueva matriz de Croma.
7. *ColorSaturationLCH*: Recibe el nombre del archivo y la lista de tuplas `(h_i, m_i)`. Actúa de forma análoga a *ColorSaturationHSV*, pero para las funciones definidas para el espacio LCH. Utiliza las funciones:
    - `imread()` del módulo `io` para obtener el tensor de la imagen RGB.
    - `rgb2lab` del módulo `color` para obtener el tensor de la imagen del espacio LAB.
    - `lab2lch` para obtener el tensor de la imagen del espacio LCH.
    - `lch2lab` para convertir la imagen LCH modificada a LAB.
    - `lab2rgb` para convertir la imagen modificada a RGB.
8. *ColorSaturation*: Recibe el modo (que es solicitado como input en la consola), el nombre del archivo y la lista de pares ordenados como argumento. Utiliza una condicional para determinar en qué modo se está llamando la función y llamar a *ColorSaturationHSV* o *ColorSaturationLCH* respectivamente. Utiliza `matplotlib` para mostrar y guardar la imagen bajo el nombre `resultado.png` en la carpeta donde se esté ejecutando `P1.py`. también muestra la imagen en una nueva ventana.

## Uso de `P1.py`:
Se puede ejecutar el archivo directamente. 

Al final del archivo (desde la línea 82) se encuentran los parámetros modificables del archivo, siendo estos `mode`, `imagen` y `lista_pares`. 

`mode` es la única variable que se pedirá como input al ejecutar el código. **Debe** ser una variación (de mayúsculas o minúsculas) de `HSV` o `LCH`. Ejemplo: `HsV` llamará a la transformación por HSV, `lCH` llamará a la transformación por LCH, mientras que `hola` levantará un error indicado que el menú llamado es inválido.

`imagen` debe ser un string con el nombre del archivo con su extensión, por ejemplo: `"test_image.png"`.

`lista_pares` es todos los puntos arbitrarios de control. Es **necesario** que sea una lista y que dicha lista contenga tuplas de formato `(h_i, m_i)`. Ejemplo: `[(0, 0.5), (0.333, 0), (0.666, 2)]` 

###### Enlace al repo: [Enlace](https://github.com/Oikkoi/T1_Imagenes.git)