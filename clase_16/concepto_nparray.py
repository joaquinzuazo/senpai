# si solo vamos a utilizar un metodo de la libreria "x", podemos importar solo ese metodo
# from numpy import array
# array([1, 2, 3, 4, 5])

# import numpy as np # importo todo el modulo y lo llamo con el alias "np"
from time import time # importo solo el metodo "time" del modulo "time"
from numpy import array

array_1 = array([[0., 4., 1.], [7., 2., 12.]])
array_2 = array([[1, 2, 2], [5, 5, 5]])

print(array_1.dtype) # podemos verificar el tipo de dato de un array
print(array_2.dtype) # podemos verificar el tipo de dato de un array