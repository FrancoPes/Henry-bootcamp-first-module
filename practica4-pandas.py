
import pandas as pd
import numpy as np


df1 = pd.read_csv('q_Emisiones_CO2.csv', sep='|',encoding='latin-1')
print('\nDf de Emisiones-------------------------------------------------------------------------------\n')
print(df1)
print('\nInfo de emisiones-------------------------------------------------------------------------------\n')
print(df1.info())
print('\nshape emisiones-------------------------------------------------------------------------------\n')
print(df1.shape)

print('\nEliminamos columnas vacias------------------------------------------------------------------------------\n')
df1.dropna(axis = 0,inplace = True)
print('Nuevo dataframe')
print(df1)



'''
#leemos el archivo de fifa
print('\nfifa-------------------------------------------------------------------------------\n')
df = pd.read_csv('fifa-statistics.csv', sep=',')
print(df)

#mostrar info del dataframe
print('\nInfo de fifa-------------------------------------------------------------------------------\n')
print(df.info())

#renombramos las columnas, las cambiamos de ingles a espaniol. PODEMOS RENOMBRAR SOLO ALGUNAS
#! SIEMPRE EL INPLACE=TRUE
df.rename(columns={'Date':'Fecha', 'Team':'Seleccion', 'Opponent' : 'Oponente','Goal Scored' : 'Goles'}, inplace=True)
print(df)

df.rename(columns={'Ball Possession %':'Posesion', 'Attempts':'intentos','1st Goal':'1er gol','Round':'Fase'}, inplace=True)
print(df)

#quiero saber solo el nombre del enxabezado
print(df.columns)


#quiero el saber el promedio de goles totales
#una forma de hacerlo es pasar una columna 
print(df['Goles'])
seriegoles = pd.Series(df['Goles'])
print(seriegoles)

a = seriegoles.mean()
print(f'La media de goles es de {a}')

# contar la cantidad de veces que sale argentina
#print(df.groupby('Seleccion').count())

#o bien
serieseleccion = pd.Series(df['Seleccion'])
print(serieseleccion.value_counts())

#quiero saber la posesion de balon de argentina frente a icelandia
p = df.loc[10, 'Posesion']
print(f' la Argentina tuvo un {p}% de posesion frente a islandia')

#quiero saber los goles, posesion anter islandia. esto me devuelve otro dataframe
p = df.loc[(10,11,15), ('Posesion','intentos')]       #esto es totalmente modificable, puedo usar ranfo o lo que sea 
print(p)
#quiero saber los datos de un solo partido en una columna
print( df.loc[10])


#mostrar solo los datos de los partidos de ARGENTINA
print(df.groupby('Seleccion').mean())


#GROUPTBY ES MUY UTIL, ES AGRUPAR POR COLUMNA QUE CUMPLAMN CIERTA CONDICION O FUNCION
#ademas podemos sacar la media de cada variable


#ordenar el dataframe por orden alfabetico de los equipos
print(df.sort_values('Seleccion', ascending=False))

print(df.groupby('Seleccion').min())

# es parecido a lo, queremos ver una parte del dataframe
print(df[(df['Posesion']> 71) & (df['Seleccion'] == 'Argentina')])  #podemos ponerle varias condiciones con &


#nuevo dataframe apartir del anterior
dfarg = df[(df['Posesion']> 71) & (df['Seleccion'] == 'Argentina')]
print(dfarg)
print(dfarg.info())

#REESTRUCTURAR EL DATA FRAME CON PIVOT

dfancho = df.pivot(columns = 'Seleccion', values = 'Goles')
print(dfancho)


#agregar una columna 

goles2 = df['Goles']*2
df = df.assign(Nuevacolumna = goles2)
print(df)









'''