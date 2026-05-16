# Clasificacion de huevos logica difusa
# Sientanse con la libertad de restructurar y modularizar los procesos. Estamos en fase de construcción (planeación)


# *** Entrada *** #
# Tenemos que definir como vamos a aceptar y modelar los datos de entrada.
# Para el modelado podemos crear un objeto Egg, con los atributos que vamos a considerar de este
# Como es simiulacion, podemos generar aleatoriamente (dentro de un rango) valores de los atributos
# para cada instancia de huevo. Esto puede ser en el constructor
# A partir de ahí cada huevo tendría su método de fuzzificación donde cada atributo iría a la función
# de membresía triangular o trapezoidal.

# *** Base de conocimiento *** #
# Después entra en una de las clasificaciones de cada característica
# ej. 0.3 de pequeño, 0. 7 de mediano, 0.5 de grande. (Aquí podríamos hacer varias cosas quedarnos con el más significativo,
# promediar, o calcular con todas **termina siendo m^n  donde n son las categorias/reglas y n las características del huevo**)
# Y esta es la parte intermedia o dónde consultamos nuestra base de conocimiento


# *** Salida *** #
# Defuzzificación, depende como hayamos elegido en el paso anterior continuamos aquí. El objetivo es clasificar en 3 clases,
# A, B y C, dónde es A para consumo immediato, B procesamiento y C deshechos.
