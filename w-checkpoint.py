# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas. 
import pandas as pd
import numpy as np

def Ret_Pregunta01():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df = pd.read_csv('Fuentes_Consumo_Energia.csv', sep=',', decimal = '.', encoding='utf-8')
    return len(df.index)

def Ret_Pregunta02():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "Fuentes_Consumo_Energia.csv".
    Esta función debe eliminar la columna 'Code' y luego informar la cantidad de columnas
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df = pd.read_csv('Fuentes_Consumo_Energia.csv', sep=',', decimal = '.', encoding='utf-8')
    df.drop('Code',  axis = 1, inplace = True)
    return (int(len(df.columns)))

def Ret_Pregunta03():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros sin tener en cuenta aquellos con valores faltantes
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df = pd.read_csv('Fuentes_Consumo_Energia.csv', sep=',', decimal = '.')
    df.drop('Code',  axis = 1, inplace = True)    #Punto anterior
    df.dropna(inplace=True)
    return (len(df.index))


def Ret_Pregunta04():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "Fuentes_Consumo_Energia.csv".
    El ExaJulio es una unidad diferentes al TWh, es decir, no tiene sentido sumarlos o 
    buscar proporciones entre ellos, la fórmula de conversión es:
    277.778 Teravatios/Hora (TWh) = 1 Exajulio
    Los campos terminados en "_EJ" corresponden a mediciones en Exajulios, 
    y los terminados en "_TWh" corresponden a Teravatios/Hora.
    La consigna es crear un nuevo campo, que se denomine "Consumo_Total" 
    y que guarde la sumatoria de todos los consumos expresados en Exajulios (convirtiendo a
    esta medida los que están en Teravatios/Hora)
    Esta función debe informar el consumo total para la entidad 'World' y año '2019', 
    redondeado a 2 decimales, retornando ese valor en un dato de tipo float.
    '''
    #Tu código aca:
    df = pd.read_csv('Fuentes_Consumo_Energia.csv', sep=',', decimal = '.')
    df.drop('Code',  axis = 1, inplace = True)   #punto 2
    df.dropna(inplace=True)     #punto 3
    a = 277.778
    df['Consumo_Total_TWH'] = (df['Coal_Consumption_EJ']*a) + (df['Gas_Consumption_EJ']*a) + (df['Oil_Consumption_EJ']*a) + df['Wind_Generation_TWh'] + df['Nuclear_Generation_TWh'] + df['Solar_Generation_TWh']+ df['Geo_Biomass_Other_TWh'] + df['Hydro_Generation_TWh'] 
    df1 = df[(df['Entity']=='World')]
    b = df1.loc[df1.Year.idxmax()]['Consumo_Total_TWH']
    return round(b,2)                                           
    

def Ret_Pregunta05():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar el año de mayor generación de energía solar (Solar_Generation_TWh) 
    para la entidad 'Europe' retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df = pd.read_csv('Fuentes_Consumo_Energia.csv', sep=',', decimal = '.')
    df.drop('Code',  axis = 1, inplace = True)   #punto 2
    df.dropna(inplace=True)     #punto 3
    df1 = df.loc[df['Entity'] == 'Europe'] 
    return int(df1.loc[df1.Solar_Generation_TWh.idxmax()]['Year'])

def Ret_Pregunta06(m1, m2):
    '''
    Esta función recibe dos array de Numpy de 2 dimensiones cada uno, y devuelve el valor booleano
    True si es posible realizar una multiplicación entre ambas matrices, 
    y el valor booleano False si no lo es
    Ej:
        n1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
        n2 = np.array([[3,3],[4,4],[5,5]])
        print(Ret_Pregunta06(n1,n2))
            True            -> Valor devuelto por la función en este ejemplo
        print(Ret_Pregunta06(n2,n1))
            False            -> Valor devuelto por la función en este ejemplo
    '''
    #Tu código aca:
    if m1.shape[1] == m2.shape[0]:
        return True
    else: 
        return False
 

def Ret_Pregunta07():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar cuál de la siguiente lista de países tuvo mayor generacíon de 
    energía eólica (Wind_Generation_TWh) en el año 2019:
        * Argentina
        * Brazil
        * Chile
        * Colombia
        * Ecuador
        * Mexico
        * Peru
    Debe retornar el valor en un dato de tipo string.
    '''
    #Tu código aca:
    df = pd.read_csv('Fuentes_Consumo_Energia.csv', sep=',', decimal = '.')
    df.drop('Code',  axis = 1, inplace = True)   #punto 2
    df.dropna(inplace=True)     #punto 3
    lista = ['Argentina','Brazil','Chile','Colombia','Ecuador','Mexico','Peru']
    df1 = df[(df['Entity'].isin(lista) == True) & (df['Year'] == 2019)]
    df1.sort_values('Solar_Generation_TWh', ascending=False, inplace =True)
    return str(df1.loc[df1.Solar_Generation_TWh.idxmax()]['Entity'])     
  

def Ret_Pregunta08():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de entidades diferentes que están presentes en el dataset
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df = pd.read_csv('Fuentes_Consumo_Energia.csv', sep=',', decimal = '.')
    df.drop('Code',  axis = 1, inplace = True)   #punto 2
    df.dropna(inplace=True)     #punto 3
    return (len(df['Entity'].unique()))

def Ret_Pregunta09():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar el promedio de consumo de carbón (Coal_Consumption_EJ) 
    en la entidad 'Europa' entre los años 1980 y 2000 (ambos inclusive), retornando ese valor en
    un dato de tipo entero.
    '''
    #Tu código aca:
    df = pd.read_csv('Fuentes_Consumo_Energia.csv', sep=',', decimal = '.')
    df.drop('Code',  axis = 1, inplace = True)   #punto 2
    df.dropna(inplace=True)     #punto 3
    df1 = df.loc[df['Entity'] == 'Europe']
    df2 = df1.loc[df1['Year'] >= 1980 ]
    df3 = df2.loc[df1['Year'] <= 2000 ]
    a = (df3['Coal_Consumption_EJ'].mean())
    
    return round(a,2)

def Ret_Pregunta10(lista):
    '''
    Esta función recibe como parámetro un objeto de la clase Lista() definida en el archivo Lista.py.
    Debe recorrer la lista y retornan la cantidad de nodos que posee. Utilizar el método de la clase
    Lista llamado getCabecera()
    Ejemplo:
        lis = Lista()
        lista.agregarElemento(1)
        lista.agregarElemento(2)
        lista.agregarElemento(3)
        print(Ret_Pregunta10(lista))
            3    -> Debe ser el valor devuelto por la función Ret_Pregunta10() en este ejemplo
    '''
    #Tu código aca:
    i = 0
    cabecera = lista.getCabecera()
    while cabecera:
        cabecera = cabecera.getSiguiente()
        i +=1
        
    return i