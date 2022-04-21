#libreria que mas vamos a usar para levantar datos
#nos permite leer facilmente sql, csv, txt, excel
#esta basada en numpy
# usamos un dataframe, lo cual es similar a una tabla
# podemos ordenar y limpiar datos
# es muy eficiente para esa tipo de tareas
#me ahorro mucho de programar


#UN DATAFRAME ES UN CONJUNTO DE SERIES
# las series son analogos a listas o arrays
#  podemos crear una series apartir de una lista o de un dicc
#podemos hacer rangos (analogoa  arange)

#? muy importante: tipos de objetos en pandas
# Series: Estructura de una dimensión.
# DataFrame: Estructura de dos dimensiones (tablas).
# Panel: Estructura de tres dimensiones (cubos)
# Estas estructuras se construyen a partir de arrays de la librería NumPy, añadiendo nuevas funcionalidades

import pandas as pd
import numpy as np

print('\n 1) Series ###################################################################################################\n')
#? 1) Series

#Caracteristicas
#Son homogéneas
# su tamaño es inmutable. no es inmutable el contenido
# crear una serie
# Dispone de un índice que asocia un nombre a cada elemento del la serie

#estructura de una serie
#!pd.Series(data=lista, index=indices, dtype=tipo)

# crear una serie
s1 = pd.Series([1, 3, 5, np.nan, 6, 8])  #np.nan omite el valor faltante pero no cambia el tipo de dato del resto
print(s1)
print(s1[1])

#Creación de una serie a partir de una lista

lista = [1, 7, 2]
s = pd.Series(lista, index = ["x", "y", "z"], dtype = int)
print(s)

#retornar un valor determinado
print(s["y"])

# De diccionario a serie
calories = {"day1": 420, "day2": 380, "day3": 390}
s = pd.Series(calories)
print(s)


# solo una parte del diccionario es una serie
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)



#atributos de las series
print(s.size)        #s.size : Devuelve el número de elementos de la serie s.
print(s.index)        #s.index : Devuelve una lista con los nombres de las filas del DataFrame s.
print(s.dtype)         #s.dtype : Devuelve el tipo de datos de los elementos de la serie s.

# acceder a un elemento a un indice
print(s[0])   #primer elemento de una serie. es lo mismo que en la lista o arrays
print(s['day1'])  #puedo acceder tambien por el indica

#visualizar una serie (HEAD)
print(s.head())


print('\n 1.1) funciones de la Series --------------------------------------------------------------------------------------\n')
#? 1.1) funciones de la Series

#dovlver nro elementos no nulos
#? s.count() 
print(s.count())

#de aqui puedo sacar el numero de elementos nulos (size - count)

# devolver la suma total si son numeros o concatenacion si son str
#? s.sum() 
print(s.sum())

# devolver suma acumulada de los numeros
#? s.cumsum() 
print(s.sum())

# muestra la frecuencia de cada valor de la serie
#? s.value_counts() 
print(s.value_counts())
#FRECUENCIA DE VALORES

# muestra el menor de la serie s
#? s.min() 
print(s.min())

# devuelve el max valor de s
#? s.max() 
print(s.max())


# devuelve la media de s
#? s.mean() 
print(s.mean())

# devuelve la desviacion estandar de s
#? s.std() 
print(s.std())

#devuelve un resumen de estadistica descriptiva
#? s.describe()
print(s.describe())


print('\n 1.2) operaciones con Series --------------------------------------------------------------------------------------\n')
#? 1.2) Operaciones con Series

#sumar dos series
s1 = pd.Series([1,2,3], index = ["x", "y", "z"], dtype = int)
s2 = pd.Series([1,2,3], index = ["x", "y", "z"], dtype = int)
print(s1 + s2)

#sumar, multiplicar dividor, etc por un escalar
print(s1*3)

#logaritmos
import pandas as pd
from math import log
s = pd.Series([1, 2, 3, 4])
s.apply(log)

print('\n 1.4) filtrar Series --------------------------------------------------------------------------------------\n')
#? 1.4) Filtrar Series


#s[condicion] : Devuelve una serie con los elementos de la serie s que se corresponden con el valor True de la lista booleana condicion.   
# condicion debe ser una lista de valores booleanos de la misma longitud que la serie

s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
print(s[s > 5])

print('\n 1.4) Ordenar Series --------------------------------------------------------------------------------------\n')
#? 1.4) Ordenar Series

# s.sort_values(ascending=booleano) : Devuelve la serie que resulta de ordenar los valores la serie s. Si argumento del parámetro ascending es True el orden es creciente y si es False decreciente.
print(s.sort_values(ascending=False))
# SORT VALUES 


#df.sort_index(ascending=booleano) : Devuelve la serie que resulta de ordenar el índice de la serie s. Si el argumento del parámetro ascending es True el orden es creciente y si es False decreciente.
print(s.sort_index(ascending=True))

print('\n 1.5)  Eliminar datos desconocidos --------------------------------------------------------------------------------------\n')
#? 1.5)  Eliminar datos desconocidos

#Los datos desconocidos representan en Pandas por NaN y los nulos por None. 
# Tanto unos como otros suelen ser un problema a la hora de realizar algunos análisis de datos, 
# por lo que es habitual eliminarlos

#? s.dropna(INPLACE = TRUE)
s = pd.Series(['a', 'b', None, 'c', np.NaN,  'd'])
print(s.dropna())

print('\n 2) DATAFRAMES ###################################################################################################\n')
#? 1) DataFrame

# Un objeto del tipo **DataFrame** define un conjunto de datos estructurado en forma de tabla donde cada columna es un objeto de tipo Series
#las filas son registros que pueden contener datos de distintos tipos.
# Un DataFrame contiene dos índices, uno para las filas y otro para las columnas

#? DataFrame(data=diccionario, index=filas, columns=columnas, dtype=tipos)

#crear un DataFrame apartir de diccionario 
datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'],
 'edad':[18, 22, 20, 21],
 'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
 'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
           }

data = pd.DataFrame(datos)
print(data)

# a partir de una lista
#? DataFrame(data=listas, index=filas, columns=columnas, dtype=tipos)
# las listas son filas
df = pd.DataFrame([['María', 18], ['Luis', 22], ['Carmen', 20]], columns=['Nombre', 'Edad'])
print(df)

#pasar una lista de diccionarios a dataframe
# df = pd.DataFrame([{'Nombre':'María', 'Edad':18}, {'Nombre':'Luis', 'Edad':22}, {'Nombre':'Carmen'}])
#print(df)

# crear un DF a partir de un array
# DataFrame(data=array, index=filas, columns=columnas, dtype=tipo) 

dt = pd.DataFrame(np.random.randint(2,3), index = ['fila1', 'fila2'], columns = ['col1', 'col2', 'col3'])
print(dt)

# Creación de un DataFrame a partir de un archivo CSV o Excel
#? read_csv(fichero.csv, sep=separador, header=n, index_col=m, na_values=no-validos, decimal=separador-decimal) 
#!consultar parametros

# Si se pasa True al parámetro columns se exporta también la fila con los nombres de columnas 
# y si se pasa True al parámetro index se exporta también la columna con los nombres de las filas.

#df = pd.read_csv('Emisiones_CO2.csv', sep='|', decimal=',')

# EN EXCEL
#? df.to_csv(fichero.csv, sep=separador, columns=booleano, index=booleano)


print('\n 2.1)  Atributos de los DataFrame --------------------------------------------------------------------------------------\n')
#? 2.1)  Atributos de los DatFrame


#Devolver infor relevante sobre el df
#? df.info()
print(dt.info())

# Devuelve una tupla con el número de filas y columnas del DataFrame df.
#? df.shape
print(dt.shape)

# numero de elementos del dataframe
#? df.size 
print(df.size)

# Devuelve una lista con los nombres de las columnas del DataFrame df
#? df.columns 
print(df.columns)

#  Devuelve una lista con los nombres de las filas del DataFrame df.
#? df.index 
print(df.index)


# df.dtypes : Devuelve una serie con los tipos de datos de las columnas del DataFrame df.
# df.head(n) : Devuelve las n primeras filas del DataFrame df.
# df.tail(n) : Devuelve las n últimas filas del DataFrame df.

print('\n 2.2) Renombrar filas y columnas --------------------------------------------------------------------------------------\n')
#? 2.2)  Renombrar filas y columnas

#? print(df.rename(columns={'nombre':'nombre y apellidos', 'altura':'estatura'}, index={0:1000, 1:1001, 2:1002}))

dt = pd.DataFrame(np.random.randint(2,3), index = ['fila1', 'fila2'], columns = ['col1', 'col2', 'col3'])
print(dt)
print(df.rename(columns={'col1':'primer columna', 'col2':'segunda columna', 'col3':'tercer columna'}, index={'fila1':0, 'fila2':1}))


print('\n 2.3) Reindexar filas y columnas --------------------------------------------------------------------------------------\n')
#? 2.3)  Reindexar filas y columnas

#print(df.reindex(index=[4, 3, 1], columns=['nombre', 'tensión', 'colesterol']))
#agregamos filas o columnas, si no hay datos, es nan


print('\n 2.3) seleccionar elementos --------------------------------------------------------------------------------------\n')
#? 2.3)  Seleccionar elemntos y columnas

# df.loc[fila, columna] : Devuelve el elemento que se encuentra en la fila con nombre fila y la columna de con nombre columna del DataFrame df.
# df.loc[filas, columnas] : Devuelve un DataFrame con los elemento que se encuentra en las filas con los nombres de la lista filas y las columnas con los nombres de la lista columnas del DataFrame df.
# df[columna] : Devuelve una serie con los elementos de la columna de nombre columna del DataFrame df.
# df.columna : Devuelve una serie con los elementos de la columna de nombre columna del DataFrame df. 
# Es similar al método anterior pero solo funciona cuando el nombre de la columna no tiene espacios en blanco.



print('\n 2.4) Anadir columnas a un data frame --------------------------------------------------------------------------------------\n')
#? 2.4)  Anadir columnas a un data frame

# El procedimiento para añadir una nueva columna a un DataFrame es similar al de añadir un nuevo par aun diccionario, 
# pero pasando los valores de la columna en una lista o serie


#Añade al DataFrame df una nueva columna con el nombre nombre y los valores de la lista lista.
#? df['nombrecolumna'] = [lista]   

#Añade al DataFrame df una nueva columna con el nombre nombre y los valores de la serie serie. 

#? df['nombrecolumna'] = pd.Series(serie)   

print('\n 2.5) Operaciones sobre columnas --------------------------------------------------------------------------------------\n')
#? 2.5)  Operaciones sobre columnas

# es lo mismo que operaciones sobre series, exactamente lo mismo

print(df['altura']*100)

print(df['sexo']=='M')

print('\n 2.6) funciones aplicadas a columnas --------------------------------------------------------------------------------------\n')
#? 2.6)  Funciones aplicadas a columnas

#para aplicar una funcion sobre una columna(log o la que sea), usamos la siguiente sintaxis:
#? df[columna].apply(f)

#ejemplo 
#? print(df['altura'].apply(log))

print('\n 2.7) Convertir columna a datetime --------------------------------------------------------------------------------------\n')
#? 2.7)  Convertir columna a datetime

#? print(pd.to_datetime(df.Nacimiento, format = '%d-%m-%Y'))


print('\n 2.8) Descripcion de un data frame --------------------------------------------------------------------------------------\n')
#? 2.8)  Convertir columna a datetime
# SON LOS MISMOS QUE LOS DE UNA COLUMNA O SERIE

#? df.count()
#? df.sum() 
#? df.cumsum() 
#? df.min() 
#? df.max() 
#? df.mean() 
#? df.std() : 
#? df.describe(include = tipo)


print('\n 2.9) ELIMINAR COLUMNA --------------------------------------------------------------------------------------\n')
#? 2.9)  ELIMINAR COLUMNA
# del d[nombre] : Elimina la columna con nombre nombre del DataFrame df.
# df.pop(nombre) : Elimina la columna con nombre nombre del DataFrame df y la devuelve como una serie.

print('\n 2.10) ANADIR FILA --------------------------------------------------------------------------------------\n')
#? 2.10)  ANADIR FILA


#? df.append(serie, ignore_index=True) 
# Devuelve el DataFrame que resulta de añadir una fila al DataFrame df con los valores de la serie serie.
# Los nombres del índice de la serie deben corresponderse con los nombres de las columnas de df.
# Si no se pasa el parámetro ignore_index entonces debe pasarse el parámetro name a la serie, 
# donde su argumento será el nombre de la nueva fila.

#EJEMPLO
#? f = df.append(pd.Series(['Carlos Rivas', 28, 'H', 89.0, 1.78, 245.0], index=['nombre','edad','sexo','peso','altura','colesterol']), ignore_index=True) 

print('\n 2.11) SACAR FILA --------------------------------------------------------------------------------------\n')
#? 2.11) SACAR FILA

#? df.drop(filas) : Devuelve el DataFrame que resulta de eliminar las filas con los nombres indicados en la lista filas del DataFrame df.
# ejemplo: df = pd.read_csv('colesterol.csv')

print('\n 2.12) FILTRAR FILA --------------------------------------------------------------------------------------\n')
#? 2.12) FILTRAR FILA

#mostrar solo filas que cumplan una o varias condiciones                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
#? print(df[(df['sexo']=='H') & (df['colesterol'] > 260)])

print('\n 2.14) ORDENAR DATAFRAME --------------------------------------------------------------------------------------\n')

#? df.sort_values(columna, ascending=booleano) : 
# Devuelve el DataFrame que resulta de ordenar las filas del DataFrame df según los valores del la columna con nombre columna.
#?df.sort_index(ascending=booleano) 
# Devuelve el DataFrame que resulta de ordenar las filas del DataFrame df según los nombres de las filas. 


print('\n 2.14) ELIMINAR FILAR CON DATOS VACIOS O NUL --------------------------------------------------------------------------------------\n')
#? s.dropna(subset=columnas)  
# Devuelve el DataFrame que resulta de eliminar las filas que contienen algún dato desconocido o nulo en las columnas de la lista columna del DataFrame df.


print('\n 2.15) sub dataframe --------------------------------------------------------------------------------------\n')
#? df.groupby(columnas).get_group(valores) 
# Devuelve un DataFrame con las filas del DataFrame df que cumplen que las columnas de la lista columnas presentan los valores de la tupla valores.
# La lista columnas y la tupla valores deben tener el mismo tamaño.

#ejemplos
#? print(df.groupby('sexo').get_group('M'))



print('\n 2.16)Aplicar una función de agregación por grupos --------------------------------------------------------------------------------------\n')

#como lo anterior pero con funciones
#? df.groupby(columnas).agg(funciones)

#funciones basicas
#? np.min : Devuelve el mínimo de una lista de valores.
#? np.max : Devuelve el máximo de una lista de valores.
#? np.count_nonzero : Devuelve el número de valores no nulos de una lista de valores.
#? np.sum : Devuelve la suma de una lista de valores.
#? np.mean : Devuelve la media de una lista de valores.
#? np.std : Devuelve la desviación típica de una lista de valores.



print('\n 2.17)Reestructurar un dataframe --------------------------------------------------------------------------------------\n')
df.melt
df.pivot #se crean tantas columnas nuevas como nombres haya en la columna 'columna'
#es algo asi como trasponer

#sirven para cambiar de formato, ver en profundidas


print('\n 2.18)Creae nueva columna --------------------------------------------------------------------------------------\n')

#nueva columna es el nombre
#goles2 son los datos
goles2 = df['Goles']*2
df = df.assign(Nuevacolumna = goles2)
print(df)



print('\n 2.19)saber nombre de las columnas --------------------------------------------------------------------------------------\n')
#? print(df.columns)

print('\n 2.20)saber los faltantes--------------------------------------------------------------------------------------\n')
#? print(df.info)
#df.isna().sum()

print('\n 2.21)Descartar aquellas filas que tengan más de tres valores faltantes------------------------------------------------------------\n')

# ELIMINO COLUMNAS QUE TENGAN MAS DEL 50PORCIENTO DE FALTANTES
#?titanic_copia.dropna(axis = 1, inplace = True, thresh=titanic_copia.shape[0]*0.5)



print('\n 2.22)Sacar la media de una columna------------------------------------------------------------\n')

#se puede hacer de varias formas, esta es una de ellas
#? print(titanic.Columna.mean())
#? print(titanic.columna.mode()[0])
#? print(titanic.columna.median())
#? print(titanic.columna.std())


print('\n 2.22)Llenar una tabla con valores medios-----------------------------------------------------------\n')


# titanic_copia.fillna(titanic.Age.median(), inplace = True)


print('\n 2.22)Duplicar repetidos-----------------------------------------------------------\n')

#df[['columna1','columna2']].drop_duplicates()


print('\n 2.22)saber cuantas veces se repiten-----------------------------------------------------------\n')

#df['columna'].count_values()

print('\n 2.22)exportar-----------------------------------------------------------\n')

#df.to_csv('nombre')









