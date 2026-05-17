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
    def __init__(self, matriz_huevos, cantidad_plumas):
        self.matriz_huevos = (
            matriz_huevos  # idealmente, que siempre sean 60 (es un arraylist de
        )
        # objetos tipo Huevo)
        self.cantidad_plumas = (
            cantidad_plumas  # cantidad de plumas dentro de la caja (en unidades)
        )


class Huevo:
    def __init__(
        self,
        area_mancha,
        grosor_fisura,
        presencia_derrames,
        interior_limpio,
        ancho,
        alto,
        profundidad,
        densidad_relativa,
        area_moteado,
        distancia_camara_interna,
        matriz_colores,
        matriz_alturas,
    ):
        self.area_mancha = (
            area_mancha  # el área total de las manchas superficiales (en milímetros)
        )
        self.grosor_fisura = (
            grosor_fisura  # el grosor de la fisura externa más ancha (en micrómetros)
        )
        self.presencia_derrames = presencia_derrames  # presencia de derrames (booleano)
        self.interior_limpio = (
            interior_limpio  # interior sin microbios ni inclusiones (booleano)
        )
        self.ancho = ancho  # ancho del huevo (en cm)
        self.alto = alto  # alto del huevo (en cm)
        self.profundidad = profundidad  # profundidad del huevo (en cm)
        self.densidad_relativa = densidad_relativa  # densidad relatva (un flotante adimensional entre 1 y 1.15, aprox.)
        self.area_moteado = (
            area_moteado  # área de la superficie que está moteada (un flotante, en cm²)
        )
        self.distancia_camara_interna = (
            distancia_camara_interna  # distancia de cámara interna (en milímetros)
        )
        self.matriz_colores = (
            matriz_colores  # dividiendo la superficie en pixeles de colores,
        )
        # los colores de cada pixel en RGB
        self.matriz_alturas = (
            matriz_alturas  # dividiendo la superficie en irregularidades,
        )
        # las coordenadas en el eje y


def funcion_gamma(a, m, x):
    """
    Función de membresía Gamma (creciente).
    a: inicio de la función (pertenencia 0).
    m: punto donde alcanza la pertenencia 1.
    x: valor de la característica.
    """
    if x <= a:
        return 0
    if x > a and x < m:
        return (x - a) / (m - a)
    return 1


def funcion_L(a, m, x):  # es la inversa de Gamma
    """
    Función de membresía L (decreciente).
    a: punto donde empieza a caer desde 1.
    m: punto donde llega a 0.
    x: valor de la característica.
    """
    if x <= a:
        return 1
    if x > a and x < m:
        return (m - x) / (m - a)
    return 0


def funcion_triangular(
    a, m, b, x
):  # a (inicio de la función), mitad (pico máximo), b (fin del intervalo) y x(valor en el que está la característica)
    """
    Función de membresía triangular.
    a: inicio del intervalo.
    m: pico máximo (pertenencia 1).
    b: fin del intervalo.
    x: valor de la característica.
    """
    # if(x<=a): return 0
    if a < x and x <= m:
        return (x - a) / (m - a)
    if m < x and x <= b:
        return (b - x) / (b - m)
    return 0


def funcion_trapezoidal(
    a, b, c, d, x
):  # a (inicio de la función), b (inicio del pico máximo), c (fin del pico máximo), d (fin de la función) y x (valor en el que está la característica)
    """
    Función de membresía trapezoidal.
    a: inicio de la rampa ascendente.
    b: inicio de la meseta (pertenencia 1).
    c: fin de la meseta.
    d: fin de la rampa descendente.
    x: valor de la característica.
    """
    # if(x<=a): return 0
    if a < x and x <= b:
        return (x - a) / (b - a)
    if b < x and x <= c:
        return 1
    if c < x and x <= d:
        return (d - x) / (d - c) # Corregido b-c por d-c para consistencia matemática
    return 0


# --- Funciones de Pertenencia de Salida (Escala 0 a 10) ---
def membresia_salida_C(x):
    """Clase C (Desecho): Centrada en 2."""
    return funcion_triangular(0, 2, 4, x)

def membresia_salida_B(x):
    """Clase B (Procesar): Centrada en 5."""
    return funcion_triangular(3, 5, 7, x)

def membresia_salida_A(x):
    """Clase A (Consumo): Centrada en 8."""
    return funcion_triangular(6, 8, 10, x)


def calcular_centroide(activacion_A, activacion_B, activacion_C):
    """
    Calcula el centroide de la figura agregada de las 3 clases (Mamdani).
    activacion_A, activacion_B, activacion_C: niveles de activación de cada clase (0 a 1).
    """
    suma_productos = 0.0
    suma_alturas = 0.0
    
    paso = 0.1
    x = 0.0
    while x <= 10.0:
        # Recorte de las funciones de salida (Mínimo)
        mu_A = min(membresia_salida_A(x), activacion_A)
        mu_B = min(membresia_salida_B(x), activacion_B)
        mu_C = min(membresia_salida_C(x), activacion_C)
        
        # Agregación de las áreas (Máximo)
        mu_total = max(mu_A, mu_B, mu_C)
        
        if mu_total > 0:
            suma_productos += x * mu_total
            suma_alturas += mu_total
        x += paso
        
    if suma_alturas == 0:
        return 5.0  # Valor neutral por defecto
        
    return suma_productos / suma_alturas


# *** Base de conocimiento *** #
# Después entra en una de las clasificaciones de cada característica
# ej. 0.3 de pequeño, 0. 7 de mediano, 0.5 de grande. (Aquí podríamos hacer varias cosas quedarnos con el más significativo,
# promediar, o calcular con todas **termina siendo m^n  donde n son las categorias/reglas y n las características del huevo**)
# Y esta es la parte intermedia o dónde consultamos nuestra base de conocimiento

rangos_L = {
    "suciedad_area": [0.5, 0.6],  # a partir de 0.5 cm², está sucio
    "suciedad_proporcional": [
        0.125,
        0.25,
    ],  # a partir de 1/8, está sucio (si el huevo es muy pequeño, 1/8 podrá ser menor que 0.5 cm² y, por lo tanto, estará sucio antes de los 0.5 cm²)
    "fisura": [0.05, 0.1],  # a partir de un grosor de 0.1 mm es una fisura grande
    "rugosidad": [
        0.1,
        0.6,
    ],  # después de los 6 micrómetros ya es una rugosidad considerable
}

rangos_triangulares = {"solidos_en_yema": [55, 70, 85], "excentricidad": []}

rangos_trapezoidales = {
    "excentricidad": [0, 72, 76, 100],
    "densidad_relativa": [1.035, 1.070, 1.085, 1.120],
    "excentricidad": [65, 72, 76, 83],
    "grosor": [0.341, 367],
}


# *** Salida *** #
# Defuzzificación, depende como hayamos elegido en el paso anterior continuamos aquí. El objetivo es clasificar en 3 clases,
# A, B y C, dónde es A para consumo immediato, B procesamiento y C deshechos.
# La fórmula es sumatoria(x_i * u(x_i)) / sumatoria(u(x_i)) u es función de pertenencia y x_i es la posición en la que se evalúa en el rango definido (0-100)
# de la función.
