# P1 (`P1.py`):
**Para hacer esta pregunta, fueron utilizadas las librerías `numpy`, `matplotlib` y `skimage`.**

Se definieron las siguientes funciones:
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


# P2 (`P2.py`):
**Para hacer esta pregunta, fueron utilizadas las librerías `numpy`, `matplotlib` y `skimage`.**

Para su ejecución, se definieron las siguientes funciones:
1. *convertir_a_gray*: Recibe como argumento el directorio relativo a `P2.py` que contiene la imagen a probar. Utiliza la función `imread` del módulo `io` de `skimage` para conseguir el tensor de la imagen, y según su longitud (es decir, el tipo de imagen), retorna una imagen en formato GreyScale, tras convertir la imagen original con el módulo `color` de `skimage` y las funciones `rgb2gray` o `rgba2gray`. Si la imagen original ya estaba en GrayScale, la retorna directamente. Se asume que se entregará una imagen en RGB en caso de que el tensor tenga longitud 3. En cualquier otro caso de longitud, la función levanta un **ValueError**

2. *calcular_salto*: Recibe como argumento el tamaño de región deseado como valor entero y el overlap deseado como float entre 0 y 1. Si el overlap es mayor o igual a 1, levanta un **ValueError*, ya que el overlap representa el valor porcentual (ej: 25% = 0.25) entre los segmentos para el algoritmo CLAHE. Calcula la cantidad total de pixeles que se superpondrán entre cada recorte, y luego calcula la diferencia entre el tamaño deseado de la región y el recorte para determinar el salto. Retorna el valor calculado, redondeado.

3. *extraer_segmentos*: Recibe como argumentos la imagen (ya leída), el tamaño de región deseado y el overlap deseado. Comienza llamando a *calcular_salto* y guarda dicha variable. Se consiguen las dimensiones de la imagen usando el atributo `.shape` de los tensores de `numpy`, luego utiliza dos bucles `for` anidados uno dentro del otro. El de fuera itera sobre y, el otro sobre x, ambos entre los respectivos valores máximos `y_max` y `x_max`. La función retorna un generador que contiene todos los segmentos de la imagen original usando slicing simple, una tupla que contiene los valores de los bordes de dicho segmento y una tupla con las coordenadas de la esquina superior izquierda x, y.

4. *obtener_transformacion*: Recibe como argumento el segmento y el factor límite. Utiliza la función `histogram` de `numpy`, declarando 256 *bins*, en un rango entre 0 y 256 cada uno. Luego, si es que el factor límite está definido, se calcula el valor promedio del segmento, se escala por el factor límite y se corta el histograma por dicho valor usando `clip` de `numpy`. Si el factor límite no está definido, se deja el histograma normal. Se calcula la diferencia entre el histograma normal y el cortado (es decir, si no hay factor límite esta diferencia es cero), se define el exceso con `sum` de `numpy` y sumando este exceso (repartido entre los 256 bins) al histograma cortado se calcula la CDF (función de distribución acumulada) con la función `cumsum` de `numpy`. Finalmente, se normaliza usando la función `round` de `numpy` en la cdf multiplicada por 255 y dividida entre su valor máximo.

5. *calcular_peso_ponderado*: recibe como argumentos el alto y ancho del segmento, creando una matriz de pesos en función de la distancia (por eso se llama ponderado); utiliza las funciones `minimum` para comparar ambos arreglos hechos con `arange` y quedarse con el menor elemento en ambos arreglos para cada posición. Luego se usa `outer` para calcular el producto exterior y formar una matriz con dichos valores. Todas las funciones anteriores son de `numpy` Al centro quedan valores mayores y a los bordes solo ceros; es por eso que en la definición previa al producto exterior se suma 1 a ambos vectores. Retorna la máscara de pesos hecha con el producto exterior.

6. *mostrar_comparacion*: Recibe como argumento la imagen inicial, la final y el tamaño de la región. Utiliza el módulo `exposure` de `skimage` para hacer las imágenes con ecualización global y CLAHE y luego utiliza `MatPlotLib` para mostrar la comparación entre las 4.

7. *ecualizacion_local*: Recibe como argumento el la ruta de la imagen, el tamaño de la región, el overlap_deseado y puede recibir el factor límite (que viene definido por defecto como *None*). Llama a la función *convertir_a_gray* para convertir la imagen original en GrayScale, luego crea dos lienzos vacíos con `np.zeros` (del mismo tamaño que la imagen orginal con el atributo `.shape`). Luego revisa si es que factor límite vale 0 para asignarlo como *None*. Después inicia un bucle for que itera en todos los segmentos, tupla de bordes y esquinas (x, y) en *extraer_segmentos*. Define el alto y ancho de cada segmento con el atributo `.shape` y llama a la función *calcular_peso_ponderado*. Después llama a la función *obtener_transformacion* para obtener la CDF normalizada, la cual se usa como un diccionario para tener el segmento ecualizado. Seguidamente se pondera dicho segmento con la máscara de peso ponderado. Se suma al lienzo de segmentos el segmento que se acaba de ponderar, y al lienzo de pesos se suma la máscara de peso ponderado. Finalmente, pasa la línea de seguridad que se asegura de que todos los valores del lienzo de pesos sean al menos 1 (con `np.maximum`) y se define la imagen final como la división (redondeada con `np.round`) entre el lienzo de segmentos y el lienzo de pesos. Luego se llama a *mostrar_comparacion* para mostrar los resultados. 

## Uso de `P2.py`:
Se puede ejecutar el archivo directamente. 

Al final del archivo (desde la línea 113) se encuentran los parámetros modificables del archivo, siendo estos `ruta`, `nombre_imagen`, `tamaño_segmento`, `overlap` y `factor_limite`. 

`ruta` es el string con la dirección (relativa a ``P2.py`) que lleva a la carpeta que contenga las imágenes de prueba. Debe ir en formato string, y se debe cambiar / por \ según corresponda. Ejemplo: `Test_Images/` o `Test_Images\`

`nombre_imagen` es un string con el nombre del archivo con su respectiva extensión. Ejemplo: `"P2_IMG_2423.tif"`

`tamaño_segmento` es un int con el tamaño deseado de cada región. Por ejemplo: `128`, `64`, `100000`, etc.

`overlap` es el float que corresponde al valor porcentual deseado para la superposición entre segmentos. Por ejemplo, `25%` de superposición deseada corresponde a `0.25`

`factor_limite` es un float con el factor de escalamiento que se usará para cortar el histograma, si es que se define y es distinto de 0.


# P3 (`P3.py`):
**Para hacer esta parte, se utilizaron las librerías `numpy`, `matplotlib.pyplot` y `skimage`.**

Se definieron las funciones:
1. *convertir_a_rgb*: recibe la dirección de la imagen y el tipo de imagen como argumento. Luego retorna la imagen como `ubyte8` (del módulo `skimage`). Soporta RGB, HSV, HSL, HSI y GrayScale. Para hacerlo, utiliza `io.imread()` de `skimage` para convertir la dirección en el tensor de imagen, y `color` y las funciones de conversión:
    - `color.hsv2rgb`
    - `color.hsl2rgb`
    - `color.hsi2rgb`
    - `color.gray2rgb`
    - `color.rgba2rgb`

2. *generar_lienzo_salida*: Recibe el factor del escalamiento **s** y la imagen original (RGB). Utiliza el método `.shape` en la imagen original para extraer el alto y ancho de la imagen. Luego, usa la función `np.ceil` de esas dimensiones escaladas por **s**, ambas redondeadas por la función `int()` Retorna un tensor de ceros con `np.zeros` de las mismas dimensiones a las escaladas y los tres canales de color. También la tupla de dimensiones de la imagen.

3. *mapeo_inverso*: Recibe la tupla de coordenadas actuales (en el lienzo reescalado) y el factor de escalamiento s. Calcula las posiciones en el lienzo original al dividir por s, retorna el par de coordenadas calculadas.

4. *calcular_nuevas_coordenadas*: recibe el tamaño máximo de la imagen original, el factor de escalamiento s, las coordenadas actuales (en el nuevo lienzo) y el modo de uso. Llama a *mapeo_inverso* para obtener el par x, y de coordenadas actuales (en la imagen original). Si el modo es `"vecino"`, el par de pixeles que se deben usar solamente es el mínimo (convertido en entero) entre x redondeado y x máximo de la imagen original. Es análogo para y. Si el modo es `"bilineal"`, se obtienen los cuatro pixeles posibles x0, y0, x1, y1 (donde x0 es el píxel de la izquierda a (x, y) e y0 es el píxel de arriba; y x1 = x0+1 e y1 = y0+1). Se calcula la distancia entre x y x0 e y e y0 (llamados diferenciales dx, dy) y los pesos son, matemáticamente, (1-dx), dx y análogo para y. Se retornan las tuplas de pesos y la tupla con los cuatro pixeles.

5. *reescalamiento*: recibe el factor de escalamiento s, la dirección relativa a la imagen, el tipo de imagen y el modo de interpolación. Primero, revisa que el modo de interpolación sea válido ("bilineal", "vecino") o variaciones de mayúsculas. Luego se consigue el tensor de la imagen con *convertir_a_rgb* y sus tamaños máximos con el atributo `.shape` de nuevo. Se extrae el lienzo vacío (tamaño escalado) junto a sus dimensiones con *generar_lienzo_salida* Después, se entra a dos bucles for. Se itera en y, luego en x en el rango de las dimensiones máximas del nuevo lienzo. Se desempaqueta la salida de *calcular_nuevas_coordenadas* según el modo:
    - Bilineal: se extraen las tuplas de peso w_x y w_y, junto a los cuatro pixeles posibles. Para cada combinación de los pares x0, y0, x1, y1 se calcula el color de cada pixel llamando a la imagen original y finalmente, sumando. Este valor es luego asignado en el lienzo vacío para las coordenadas x, y sobre las que se itera.
    - Vecino: Se extrae los pixeles promediados x_p, y_p y se asigna el mismo color de la imagne en x_p, y_p al lienzo en x, y
- Finalmente, se retorna el lienzo vacío usando `.astype(np.uint8)` y la imagen original

## Uso de `P3.py`

A partir de la línea 100 empieza el ejecutable en `P3.py`. Para modificarlo, se espera la modificación de las siguientes variables:

- `ruta`: Corregir `\` por `/` según el sistema operativo. También, renombrar la ruta **relativa a P3.py** según donde estén las imágenes para probar.

- `imagen`: Cambiar el string asignado por el nombre (con su extensión) de la imagen.

- `s`: el factor de escalamiento.

- `tipo_imagen`: Un string con el tipo de imagen, están soportados los soportados por *convertir_a_gray()*

- `modo_interpolacion` = se espera `"vecino"` o `"bilineal"`