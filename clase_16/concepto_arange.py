import time
from numpy import arange

my_arr = arange(10000000)  # Utilizando NumPy Arrays
my_list = list(range(10000000)) # Utilizando Listas Python

# Podemos verificar la diferencia en tiempo de ejecución entre ambos tipos de datos
start_time = time()
my_arr2 = my_arr * 2 # Multiplicamos cada elemento del array por 2
print("Tiempo de ejecución Numpy:", time() - start_time)

start_time = time()
my_list2 = [x * 2 for x in my_list] # Multiplicamos cada elemento de la lista por 2
print("Tiempo de ejecución Listas:", time() - start_time)