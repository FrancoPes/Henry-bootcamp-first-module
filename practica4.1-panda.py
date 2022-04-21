import pandas as pd
import numpy as np

df = pd.read_csv('salary_data.csv', sep=',')
datos = df['Salary']/12
df = df.assign(Monthly = datos) 
print(df)

df1 = df.groupby('Title').max()
print(df1)
print(f'grupos salario media')
# 1) cual es el salario promedio de un junior
df1 = df.groupby('Levels').mean()
print(df1)

#cual es el salario promedio independiente de la categoria
s = df['Salary']
a = int(s.mean())
print(f'El salario promedio de un data science es de {a}')


#cual es el salario maximo
s1 = df['Salary']
b = int(s1.max())
print(f'El salario maximo de un data science es de {b}')

print('salario mensual por categoria')
#agregar una columna con salario mensual
#? NO HACEN FALTA COMILLAS
print(df.groupby('Levels').mean())

#salario minimo de un junior, senior, et

print(df.groupby('Levels').min())

print(df.groupby('Levels').max())

#ELIMINAR LAS FILAS QUE TENGAN UNKNOWS
'''
s1 = df['Levels']
print(df.replace('Unknown',None, inplace=True))
print('ELIMINANDO FILAS CON UNKNOWS --------------------------------------------------------------------------------------------')
print(df.dropna(axis = 0, how = 'any', subset = 'Levels'))
'''
print('ELIMINANDO FILAS CON UNKNOWS --------------------------------------------------------------------------------------------')
df.drop(df.index[df['Levels'] == 'Unknown'], inplace=True)
print(df)

#? con df.drop([]) eliminamos filas o columnas
#? para borrar columnas: df.drop(columns = ' ' , inplace = True)


#hacer un top con las empresar que mas pagan
df3 = df.groupby('Company').mean()
print(df3)
print(df3.sort_values(by=['Salary'], ascending=False))



#!como modifico el archvo