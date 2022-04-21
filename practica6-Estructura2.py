
import pandas as pd
import numpy as np


df = pd.read_csv('q_Emisiones_CO2.csv', sep='|',encoding='latin-1')
print('\nDf de Emisiones-------------------------------------------------------------------------------\n')
df.dropna(axis = 0, inplace = True)
print(df)



#? 1) Cargar el dataset "Emisiones_CO2.csv" provisto en la clase 2 en un Dataframe de Pandas, quitar los registros que contengan valores faltantes 
#? e implementar una nueva columna, que contenga el resultado de una función Hash aplicada sobre el campo "Código de País" y se denomine "Clave_Hash".<br>
#? Consideraciones: Se puede utilizar la función provista.

def hash_function(key):
    return sum(index * ord(character) for index, character in enumerate(repr(key), start=1))

a = 'ABW'
print(hash_function(a))

print('Hasheado de Codigo de pais------------------------------------------------------------------------------\n')

#df = df.assign(Hash  = hash_function(df['Código de país']) )
df['Hash'] = df['Código de país'].apply(hash_function)

print(df)

#print(df.loc[4997, 'Hash'])

#? 2. A partir del Dataframe creado en el punto 1, construir uno nuevo, que contenga solo los valores distintos de la tupla "Clave_Hash", 
#? "Código de País" , "Nombre de país" y "Región". Quitando luego del dataframe original los campos "Código de País" , 
#? "Nombre de país" y "Región"


print('Nuevo Data frame------------------------------------------------------------------------------\n')

df1 = df[['Hash','Código de país','Nombre del país','Región']].drop_duplicates()
df1.drop(['Nombre del país','Región'],axis = 1, inplace = True)
print(df1)
#! SIEMPRE ACLARAR EL AXIS
#? SIEMPRE ACLARAR EL AXIS
# SIEMPRE ACLARAR EL AXIS


#Reorganizar la dataframe



















