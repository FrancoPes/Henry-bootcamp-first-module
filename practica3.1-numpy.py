
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

#veo las dimensiones
print(arr.ndim)

#quiero un elemento
print('5th element on 2nd row: ', arr[1, 1, 2])

#slicing de arrays
#es lo mismo que 
arr1 = arr[0:2,0,0:2]
print(arr1)

#vemos el tipo de dato
print(arr.dtype)

# vemos la forma
print(arr.shape)


#iterar todos los elementos del array, independiente de las dimensiones
for x in np.nditer(arr):
  print(x)
  
# iterar y cambiar a string
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

#enumerar 
for idx, x in np.ndenumerate(arr):
  print(idx, x)
  
# concatenar o juntar 2 arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0)
print(arr)
print(arr.shape)

arr = np.stack((arr1, arr2), axis=0)
print(arr)
print(arr.shape)
#arr = np.hstack((arr1, arr2))
#print(arr)

#buscar valores
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)


#filtrar
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


#matriz identidad
print(np.identity(4))


#juntar dos vectores en una misma matriz (VERTICALL STACK)

v1 = np.array([1,2,3,4])
v2 = np.array([11,22,33,44])

matrix = np.vstack([v1,v2])
print(matrix)

#vstack me apila vectores
matrix = np.vstack([v1,v2,v2,v1,v2,v1])
print(matrix)

#HORIZONTAL STACK (HSTACK)
matrix = np.hstack([v1,v2,v1])
print(matrix)

#como cargar
# arr1 = np.genfromtxt('name' , delimiter = )

#! puedo importar un csv ?
















