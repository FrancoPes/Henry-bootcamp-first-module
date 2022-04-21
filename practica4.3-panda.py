



#! REVISAR ESTOS ENLACES SI ESTAS EN PROBLEMA
'''
https://github.com/KeithGalli/pandas/blob/master/Pandas%20Data%20Science%20Tutorial.ipynb

PROYECTO REAL
https://github.com/KeithGalli/Pandas-Data-Science-Tasks/blob/master/SalesAnalysis/SalesAnalysis.ipynb
'''



#---------------------------------------------------------------------------------------------------------------------------------------------#
#PRACTICA DE TODAS LAS FUNCIONES DE PANDAS


#? importamos archivo, separamos columnas
from cmath import log
from numpy import column_stack
import pandas as pd
df = pd.read_csv('salary_data.csv', sep=',')

#---------------------------------------------------------------------------------------------------------------------------------------------#
#Info basica
#? imprimir columnas 
print(df.columns)
print(df.describe())

#? ver info basicas
print(df.info)

#? ver el tamanio del dataframe
print(df.size)

#? ver cuantas columnas y filas
print(df.shape)

#? detectar filas
print(df.index)

#?detecta valores nulos
print(df.isna().sum())
#---------------------------------------------------------------------------------------------------------------------------------------------#
#cambiar nombre filas o columnas
#? cambiar nombre de una columna o fila
print(df.rename(columns={'Company':' Empresa'}))

#? reindexar
#print(df.reindex(index=[4, 3, 1], columns=['nombre', 'tensión', 'colesterol']))


#---------------------------------------------------------------------------------------------------------------------------------------------#
#SELLECIONAR DATO O DATOS (FILAS O COLUMNAS). PUEDO SACAR UN DATA FRAME MAS CHICO DE ACA
#? LOC df.loc[fila, columna]: devolveme el elemento que esta en fila uno, columna salary
print(df.loc[1, 'Salary'])

#? seleccionar filas con cierto tipo de dato por columna
print(df.loc[df['Salary'] == 10000])

print(df.loc[1:10, 'Salary':'Levels'])

#?saleccionar un dato que cumpla ciertas condiciones

#VER UNA FILA O VARIAS EN PARTICULAR
#ILOC TAMBIEN

#---------------------------------------------------------------------------------------------------------------------------------------------#
#AGREGAR UNA COLUMNA CON EL METODO APPLY o assign

#? con assign para una transformacion simple
datos = df['Salary']/12
df = df.assign(Monthly = datos) 
print(df)


#? con apply para funciones mas complejas. debo meter una funcion lamba u otra mas compleja definida afuera
df['log salario'] = df['Salary'].apply(lambda x: x / 100)
print(df)

#? se puede hacer una columna SIN APPLY O ASSING:

df['log salario'] = df['Salary'] + df['Monthly'] 
#---------------------------------------------------------------------------------------------------------------------------------------------#

#AGREGAR FILA

#? df.append(serie, ignore_index=True) 
#? f = df.append(pd.Series(['Carlos Rivas', 28, 'H', 89.0, 1.78, 245.0], index=['nombre','edad','sexo','peso','altura','colesterol']), ignore_index=True) 


#---------------------------------------------------------------------------------------------------------------------------------------------#
#ELIMINAR FILA O COLUMNA: ESPECIFICAR AXIS
print(df.drop('Salary',  axis = 1))
print(df.drop(1,  axis = 0))

#? ELIMINAR FILAS QUE CUMPLAN UNA CONDICION
df.drop(df.index[df['Levels'] == 'Unknown'], inplace=True)
df.drop(df.index[df['Salary'] > 110000], inplace=True)
print(df)

#? eliminar filas repetidas
df.drop_duplicates()
# contar repetidos df['columna'].count_values()

#? eliminar filas con datos nulos
print(df.dropna(subset='Salary') ) 

#? llenar valores vacios titanic_copia.fillna(titanic.Age.median(), inplace = True)

#eliminar columnas que tengan mas del 50% de faltantes
#?titanic_copia.dropna(axis = 1, inplace = True, thresh=titanic_copia.shape[0]*0.5
#---------------------------------------------------------------------------------------------------------------------------------------------#
#FILTRAR DATAFRAMES

#filtramos un data frame cuyas columna cumple ciertas condiciones
print(df[(df['Company']=='Cox Communications Inc') & (df['Salary'] > 260)])


lista = ['Argentina','Brazil','Chile','Colombia','Ecuador','Mexico','Peru']
df2 = df[(df['Entity'].isin(lista) == True) & (df['Year'] == 2019)]
#---------------------------------------------------------------------------------------------------------------------------------------------#

#Ordenar df por cierta columna. Agrupar por cierta columna

print(df.sort_values('Salary', ascending=False))
#groupby
#print(df.groupby('sexo').get_group('M'))
#df.sort_index(ascending=booleano) 

#funciones basicas del groupby
#? print(df.groupby('sexo').get_group('M'))
#? np.min : Devuelve el mínimo de una lista de valores.
#? np.max : Devuelve el máximo de una lista de valores.
#? np.count_nonzero : Devuelve el número de valores no nulos de una lista de valores.
#? np.sum : Devuelve la suma de una lista de valores.
#? np.mean : Devuelve la media de una lista de valores.
#? np.std : Devuelve la desviación típica de una lista de valores.

#---------------------------------------------------------------------------------------------------------------------------------------------#

#Reestructurar un data frame
#? pasar de formato largo a ancho
#df.pivot(index=filas, columns=columna, values=valores) : Devuelve el DataFrame que resulta de convertir el DataFrame df de formato largo a formato ancho. Se crean tantas columnas nuevas como valores distintos haya en la columna columna. Los nombres de estas nuevas columnas son los valores de la columna columna mientras que sus valores se toman de la columna valores. Los nombres del índice del nuevo DataFrame se toman de los valores de la columna filas.
# ES MUY SIMILAR A UN GROUPBY

#? pasar de formato ancho a largo
# df.melt Devuelve el DataFrame que resulta de convertir el DataFrame df de formato ancho a formato largo. Todas las columnas de lista columnas se reestructuran en dos nuevas columnas con nombres nombre-columnas y nombre-valores que contienen los nombres de las columnas originales y sus valores, respectivamente. Las columnas en la lista id-columnas se mantienen sin reestructurar. Si no se pasa la lista columnas entonces se reestructuran todas las columnas excepto las columnas de la lista id-columnas.
#---------------------------------------------------------------------------------------------------------------------------------------------#
# FUSIONAR DATASETS
df.merge












































