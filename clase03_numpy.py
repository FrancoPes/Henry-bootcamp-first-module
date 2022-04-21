
#? notas generales
#sirve porque trabaja con arrays, son basicamente matrices
#todos los elementos del array son del mismo tipo
#podes trabajar con mas de una dimension, ndimensiones
# una dimension cero seria un escalar
# un array de una dimension seria un vector
# un array de 3 o mas dimensiones son 'tensores'
#linspace: genera numeros aleatorios en un rango


#? TIPS IMPORTANTES

#? datos homogeneos
#Tip: Algo muy importante que tienes que saber es que los arrays tienen que tener un único tipo de dato. 
# Esto hace que sea muy eficiente almacenarlos y acceder a ellos. #
# Si intentas poner varios tipos de datos, NumPy te cambiará algunos elementos para que todos sean homogéneos

#? rangos en numpy
#La función **np.arange()** funciona parecido a range en Python, solo que en lugar de regresar un generador, retorna un ndarray.
# Sus argumentos principales son: start, stop y step. 
# Con lo que se le puede dar un rango de valores y cada cuánto tienen que aparecer.
# **np.linspace()** toma el tamaño del array y los steps se calcularán  automáticamente

#? arrays mismos elementos
#La función **np.full()** crea un array con un valor en específico. Tiene 2 argumentos
#print(np.full(shape=(2, 2), fill_value=5))
# La función **np.full_like()** sirve si ya se tiene un array
# y se lo quiere tomar como base para crear otro con el mismo tamaño, pero con un mismo valor.

#? Matrices en numpy (son casi lo mismo que arrays)
# **np.array([[1,2,3]])** generamos arrays, mientras que con **np.mat([1,2,3])** generamos matrices
#  Ambos tienen operaciones **.T (traspuesta)** para devolver la matriz de transposición, 
# pero np.mat tiene otras como **H (transposición conjugada)** e **I (matriz inversa)**

#? diferencia entre none y nan
#Cuando tenemos un objeto None incluído en una serie, el “upcasting” de Numpy se resuelve a “object”. 
# Cuando tenemos un np.nan, conservamos una columna de tipo float y podemos seguir operando:
# val1 = np.array([1, None, 2, 3])
 #val1
#array([1, None, 2, 3], dtype=object)
 #val2 = np.array([1, np.nan, 3, 4])
 #val2
#array([ 1., nan,  3.,  4.])
 #val2.dtype
#dtype('float64')



import numpy as np



#? 1) CREACION DE ARRAYS
print('1) CREACION DE ARRAYS *************************************************************************************************')
# Un array de dimension cero es un escalar
print('Crear array de dimension cero ----------------------------------------------------------------------------------')
a = np.array(10)
print(a)
print(a.ndim)

#forma natural de crear un array de una dimension
print('Crear array de dimension uno ----------------------------------------------------------------------------------')
b = np.array([1,2,3,4,5])
print(b)
print(b.ndim)



#forma natural de crear un array de dos dimensiones. cada corchete es una dimension
print('Crear array de dimension dos ----------------------------------------------------------------------------------')
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.ndim)



#forma natural de crear un array de tres dimensiones. cada corchete es una dimension
print('Crear array de dimension tres ----------------------------------------------------------------------------------')
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print(arr.ndim)  #? la funcion ndim nos indica la cantidad de dimensiones



#Crear un array apartir de una lista
print('Crear un array apartir de una lista ----------------------------------------------------------------------------------')
lis = [1,2,3,4,5,6]
a = np.array(lis)
print(a)

#Crear un array con todos ceros
print('Crear un array con todos ceros ----------------------------------------------------------------------------------')
print(np.zeros(4))  #!COMO HAGO UNA MATRIZ?


#Crear un array con todos ceros
print('Crear un array con todos unos ----------------------------------------------------------------------------------')
print(np.ones(4))  #!COMO HAGO UNA MATRIZ?



#? 2) INDEXING ARRAYS
print('2) INDEXING ARRAYS*********************************************************************************************************************')
#si es de una dimension, es lo mismo que en una lista

#obtener un elemento del array de 2 dimensions
print('obtener un elemento del array de 2 dimensions ----------------------------------------------------------------------------------')
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd row: ', arr[1, 4])

#obtener un elemento del array de 3 dimensions
print('obtener un elemento del array de 3 dimensions ----------------------------------------------------------------------------------')
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])  # tercer elemento del 2do, del 1ro





#? 3) SLICING ARRAYS  (REBANAR)
print('3) SLICING ARRAYS *********************************************************************************************************************')
#Mostar solo del 2do elemento al quinto
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#saltar de dos en dos en un rango (el valor del de la derecha determina el salto)
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::-2])

#slicing cuando tenemos 2 dimensiones
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])  #segundo, tercer y cuarto elemento ([1:4]) de ambos argumentos[0:2]






#? 3) ARRAYS DATA TYPE 
print('4) ARRAYS DATA TYPE *********************************************************************************************************************')

# TIPOS DE DATOS Y SU SIMBOLO EN NUMPY

#? i - integer
#? b - boolean
#? u - unsigned integer
#? f - float
#? c - complex float
#? m - timedelta
#? M - datetime
#? O - object
#? S - string
#? U - unicode string
#? V - fixed chunk of memory for other type ( void )

# Datos interos
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# datos strings
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)


#pasar un array de entero a string
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype) #! consultar

# crear otro array pero con otro TIPO de dato. aca paso de booleano a entero
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

# lo mismo pero de float a booleano
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)



#? 4) COPIAS Y VIEWS 
print('4) COPIAS Y VIEWS *********************************************************************************************************************')


#CREAR UNA COPIA
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42  #! ASI SE REASIGNA UN VALOR

print(arr)
print(x)  #notese que en la copia no aparece el 43

#view
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)


#? 5) SHAPE 
print('5) SHAPE *********************************************************************************************************************')

#basicamente nos dice la forma. es una tupla con el tamanio
#debo usar el metodo shape
arr = np.array([[1, 2, 3, 4, 3 ], [5, 6, 7, 8, 6]])
print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)


#? 6) RESHAPE 
print('6) RESHAPE *********************************************************************************************************************')

#RESHAPE DE 1D A 2D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4,3)         #QUE HACE? Como la lista anterior tenia 12 elementos, ahora los separa en 4 de 3 elementos cada uno
print(newarr)


#RESHAPE DE 1D A 3D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)
print(newarr)

#? 7) ITERATING ARRAYS
print('7) ITERATING ARRAYS *********************************************************************************************************************')

#PARA UNA DIMENSION ES LO MISMO QUE UNA LISTA
arr = np.array([1, 2, 3])
for x in arr:
  print(x)
#SI ES DOS DIMENSIONES, TE ITERA VECTOR POR VECTOR  
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

# para iterar cada uno de los elementos de los vectores, hago dos for
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y) #como regla, digamos que tenes que usar tantos for como dimensiones tenes

#iteraciones cuando tengo 3 dimensiones
#si tengo un solo for, me itera solo la matriz. si tengo dos me itera vector. si tengo 3 me itera escalar

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)
#ejemplo de iteracion de escalares en 3d 
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:   
            print(z)
    
#con la funcion nditter, nos itera solo los escalares, independientemente de las dimensiones           
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)

#ITERAR Y CAMBIAR A STRING
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)


#ITERAR Y SALTAR DOS 
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)
  
#ENUMERAR ESCALARES DE N DIMENSIONES
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)
  
  

#? 8) JUNTAR ARRAYS
print('8) JUNTAR ARRAYS *********************************************************************************************************************')
#! Un método particular es **flatten()**, que permite llevar cualquier array a una dimensión
#PARA UNIR DOS ARRAYS, USAMOS EL METODO CONCATENATE
#si queremos unirlo en una de una sola dimension:
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)


# si queremos unirla en una de 2 dimensiones, axis = 1
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

# crea una sola fila
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)

#crea una sola columna
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)

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

#! consultar que hace el split 
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)



#? 9) BUSCAR ELEMENTO
print('9) BUSCAR ELEMENTO *********************************************************************************************************************')
#CON EL METODO WHERE, NOS DICE DONDE ESTA EL ELEMENTO Y CUANTAS VECES E REPITE
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

#PUEDO ANADIR UNA OPERACION
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

#? 10) ORDEN NUMERICO Y ALFABETICO
print('10) ORDEN NUMERICO Y ALFABETICO *********************************************************************************************************************')


#ALFABETICAMENTE. TODO CON EL SORT . 
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))
#BOOLEANO
arr = np.array([True, False, True])
print(np.sort(arr))

#SORT UN ARRAY DE DOS DIMENSIONES
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))


#? 11) FILTRO
print('11) FILTRO *********************************************************************************************************************')
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

#? 12) RANDOM
print('12) RANDOM *********************************************************************************************************************')

#numeros aleatorios enteros NP.RANDOM.RANDINT
# un array de una dimension con numeros aleatorios entre 0 y 100
x= np.random.randint(100, size=(5))
print(x)

# un array de dps dimensiones
x= np.random.randint(100, size=(5, 2))
print(x)

# un array de tres dimensiones
x= np.random.randint(1045260, size=(2,2,2))
print(x)

#! SI QUEREMOS QUE SEA FLOTANTE LE SACAMOS EL INT
x= np.random.rand(5, 2)
print(x)

#generar un array de 2d con los numeros de la lista
x = np.random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

#? 12) aritmetica
print('12) ARITMETICA *********************************************************************************************************************')

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr)


arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)

#multiplicacion
#matmul
# a = np.array([[2,3],[2,3],[2,3]])
# a.shape
#(3, 2)
# b = np.array([[1,6,5,2,7],[1,2,7,0,9]])
# b.shape
#(2, 5)
#np.matmul(a,b)

