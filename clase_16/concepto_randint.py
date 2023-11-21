from numpy import random

array_3d = random.randint(10, size=(3, 2, 2)) # 3 matrices de 2x2

print(array_3d, end='\n\n')
print("Shape:", array_3d.shape)
print("Dim:", array_3d.ndim)


array_3d = random.randint(10, size=(3, 1, 4)) # 3 matrices de 2x4

print(array_3d, end='\n\n')
print("Shape:", array_3d.shape) # podemos verificar la forma de un array con el atributo "shape" (filas, columnas)
print("Dim:", array_3d.ndim) # podemos verificar la dimension de un array con el atributo "ndim" (dimensiones)