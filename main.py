# Clasificacion de huevos logica difusa
# Sientanse con la libertad de restructurar y modularizar los procesos. Estamos en fase de construcción (planeación)


# *** Entrada *** #
# Tenemos que definir como vamos a aceptar y modelar los datos de entrada.
# Para el modelado podemos crear un objeto Egg, con los atributos que vamos a considerar de este
# Como es simiulacion, podemos generar aleatoriamente (dentro de un rango) valores de los atributos
# para cada instancia de huevo. Esto puede ser en el constructor
# A partir de ahí cada huevo tendría su método de fuzzificación donde cada atributo iría a la función
# de membresía triangular o trapezoidal.

class Casillero:
    def __init__(self, matriz_huevos,cantidad_plumas):
        self.matriz_huevos = matriz_huevos #idealmente, que siempre sean 60 (es un arraylist de
                                            #objetos tipo Huevo)
        self.cantidad_plumas = cantidad_plumas #cantidad de plumas dentro de la caja (en unidades)

class Huevo:
    def __init__(self,area_mancha,grosor_fisura,
                 presencia_derrames,
                 interior_limpio,ancho,alto,profundidad,densidad_relativa,area_moteado,
                 distancia_camara_interna,matriz_colores,matriz_alturas):
        self.area_mancha = area_mancha #el área total de las manchas superficiales (en milímetros)
        self.grosor_fisura = grosor_fisura #el grosor de la fisura externa más ancha (en micrómetros)
        self.presencia_derrames = presencia_derrames #presencia de derrames (booleano)
        self.interior_limpio = interior_limpio #interior sin microbios ni inclusiones (booleano)
        self.ancho = ancho #ancho del huevo (en cm)
        self.alto = alto #alto del huevo (en cm)
        self.profundidad = profundidad #profundidad del huevo (en cm)
        self.densidad_relativa = densidad_relativa #densidad relatva (un flotante adimensional entre 1 y 1.15, aprox.)
        self.area_moteado = area_moteado #área de la superficie que está moteada (un flotante, en cm²)
        self.distancia_camara_interna = distancia_camara_interna #distancia de cámara interna (en milímetros)
        self.matriz_colores = matriz_colores #dividiendo la superficie en pixeles de colores, 
                                            #los colores de cada pixel en RGB
        self.matriz_alturas = matriz_alturas #dividiendo la superficie en irregularidades, 
                                            #las coordenadas en el eje y


def funcion_triangular(a,m,b,x): #a (inicio de la función), mitad (pico máximo), b (fin del intervalo) y x(valor en el que está la característica)
    if(x<=a): return 0
    if(a<x and x<=m):return (x-a)/(m-a)
    if(m<x and x<=b):return (b-x)/(b-m)
    if(x>b): return 0

def funcion_trapezoidal(a,b,c,d,x): #a (inicio de la función), b (inicio del pico máximo), c (fin del pico máximo), d (fin de la función) y x (valor en el que está la característica)
    if(x<=a): return 0
    if(a<x and x<=b):return (x-a)/(b-a)
    if(b<x and x<=c):return 1
    if(c<x and x<=d):return (d-x)/(b-c)
    if(x>d): return 0
        



# *** Base de conocimiento *** #
# Después entra en una de las clasificaciones de cada característica
# ej. 0.3 de pequeño, 0. 7 de mediano, 0.5 de grande. (Aquí podríamos hacer varias cosas quedarnos con el más significativo,
# promediar, o calcular con todas **termina siendo m^n  donde n son las categorias/reglas y n las características del huevo**)
# Y esta es la parte intermedia o dónde consultamos nuestra base de conocimiento




# *** Salida *** #
# Defuzzificación, depende como hayamos elegido en el paso anterior continuamos aquí. El objetivo es clasificar en 3 clases,
# A, B y C, dónde es A para consumo immediato, B procesamiento y C deshechos.
