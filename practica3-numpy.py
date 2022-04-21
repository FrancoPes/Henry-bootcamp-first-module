
#?  Ejercicio 1**: Responder las siguientes preguntas:
#?  ¿Qué operaciones se pueden hacer tanto en un arreglo de Numpy como en una lista? Dar un ejemplo en una celda.
#?  ¿Qué operaciones se pueden hacer en un arreglo de Numpy pero NO en una lista? Explorar algunas opciones y dar un ejemplo en una celda.
#? ¿Cuál es la diferencia entre un arreglo de forma -shape- (n,), (n,1) y (1,n)? Pueden crear arreglos para intentar responder esa pregunta.


#sumarle un elemento un valor

# arr = arr1 + 1


#? Ejercicio 2**:
#? Escribir un arreglo con números enteros del 0 al 9. Pista: arange
#? Escribir un arreglo con 100 números equiespaciados del 0 al 9. Pista: linspace

import numpy as np

arr1 = np.random.randint(9, size=(5))
print(arr1)

rr = arr1 + 1 #sumarle un elemento un valor
#aqui el 5 es el salto, pero no determinamos los elemetos
arr2 = np.arange(0,100,5)
print(arr2)
#aqui determinamos los elementos y lo hacemos equistante
arrl = np.linspace(0,10,9)
print(arrl)

#? Ejercicio 3**:
#? Escribir un arreglo con números enteros del 10 al 100 y seleccionar aquellos que son divisibles por 3<br>
#? Pista: mask

arr = np.arange(10,101,1)
filter_arr = arr % 3 == 0
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
 
print(newarr)
print(filter_arr) #si emprimimos el filtro nos sale booleanos

#? Ejercicio 4**:
#? Crear un arreglo de ceros de `shape` (5,10).
#? Reemplazar la segunda y cuarta fila con unos
#? Reemplazar la tercera y octava columna con dos (2).
#NOTA: CADA ELEMENTO TIENE SU SHAPE, SEA VECTOR, MATRIZ O ELEMENTO
# .t es para trasponer
arr = np.full(shape=(5, 10), fill_value=0)
arr[1] = 2
arr[2] = 1
arr[3] = 2
arr[4] = 1
print(arr)
print(arr.T)

#aqui tambien puedo usar el slicing        
 # @ es similar al metodo matmul          
  # para hacer la diagonal con unos se usa np.eye
#como trabajar imaginarios en numpy
      
#? https://numpy.org/doc/stable/reference/random/legacy.html 
#? https://www.machinelearningplus.com/python/101-numpy-exercises-python/

#? 3) crear un array de puros booleanos
arrb = np.full((3, 3), True, dtype=bool)
print(arrb)

#? 4. How to extract items that satisfy a given condition from 1D array?
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr1 = arr[arr//2 == 1]
print(arr1)

#? 5. How to replace items that satisfy a condition with another value in numpy array?
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for x in arr:
    if x%2 == 0:
        arr[x] = -1
print(arr)

#? 7. How to reshape an array?
#arr = np.random.randomint(100, size=(16))
#arr1 = arr.reshape((4,4))
#print(arr1)

#? 8. How to stack two arrays vertically?
# np.vstack([a, b])


#? 9. How to stack two arrays horizontally?
#np.hstack([a, b])

#? 10. How to generate custom sequences in numpy without hardcoding?


#? 11. How to get the common items between two python numpy arrays?
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)

#? 12. How to remove from one array those items that exist in another?
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

# From 'a' remove all of 'b'
np.setdiff1d(a,b)
#> array([1, 2, 3, 4])

#? 13. How to get the positions where elements of two arrays match?
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

np.where(a == b)

#?  14. How to extract all numbers between a given range from a numpy array?
index = np.where((a >= 5) & (a <= 10))
 
#? 15. How to make a python function that handles scalars to work on numpy arrays?
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

pair_max = np.vectorize(maxx, otypes=[float])

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max(a, b)

#? 16. How to swap two columns in a 2d numpy array?
arr = np.arange(9).reshape(3,3)
arr[:, [1,0,2]]

#? 18. How to reverse the rows of a 2D array?
# Input
arr = np.arange(9).reshape(3,3)

# Solution
arr[::-1]

#? 19. How to reverse the columns of a 2D array?
# Input
arr = np.arange(9).reshape(3,3)

# Solution
arr[:, ::-1]
#> array([[2, 1, 0],
#>        [5, 4, 3],
#>        [8, 7, 6]])

#?25. How to import a dataset with numbers and texts keeping the text intact in python numpy?

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

# Print the first 3 rows
iris[:3]

#? 26. How to extract a particular column from 1D array of tuples?
# Input:
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
print(iris_1d.shape)

# Solution:
species = np.array([row[4] for row in iris_1d])
species[:5]

#? 27. How to convert a 1d array of tuples to a 2d numpy array?
iris_2d = np.array([row.tolist()[:4] for row in iris_1d])
iris_2d[:4]

#? 28. How to compute the mean, median, standard deviation of a numpy array?
#mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
#print(mu, med, sd)

#? 34. How to filter a numpy array based on two or more conditions?
# condition = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)
#iris_2d[condition]


#? 37. How to find if a given array has any null values?
# np.isnan(iris_2d).any()

#? 45. How to find the most frequent value in a numpy array?
#vals, counts = np.unique(iris[:, 2], return_counts=True)
#print(vals[np.argmax(counts)])

#? 47. How to replace all values greater than a given value to a given cutoff?
print(np.where(a < 10, 10, np.where(a > 30, 30, a)))


#? 50. How to convert an array of arrays into a flat 1d array?
#array_of_arrays = np.array([arr1, arr2, arr3])

#? 58. How to find the duplicate records in a numpy array?

# Input
np.random.seed(100)
a = np.random.randint(0, 5, 10)

## Solution
# There is no direct function to do this as of 1.13.3

# Create an all True array
out = np.full(a.shape[0], True)

# Find the index positions of unique elements
unique_positions = np.unique(a, return_index=True)[1]

# Mark those positions as False
out[unique_positions] = False
















