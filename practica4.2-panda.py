import pandas as pd
import numpy as np

df = pd.read_csv('q_deathcauses.csv', sep=',')
print(df)

#cual es la principal causa de muerte en argentina

print(df.groupby('Entity').mean())


# muertes en el 2010 por pais
print(df[(df['Year']==2010) & (df['Code'] == 'ARG')])

#MOSTRAR UNA COLUMNA QUE CUMPLA CIERTAS CARACTERISTICAS

df.loc[df.index[df['Company Name'] == 'Mu Sigma']]
#DF.COLUMNS
#
df.isna
