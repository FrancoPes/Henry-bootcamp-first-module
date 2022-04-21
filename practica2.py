



#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#? 1.  Abrir el archivo "Emisiones_CO2.csv" y cargar sus datos en un diccionario.
import os                                                       #Con r somo modificamos el archivo
archivo = open('Emisiones_CO2.csv', 'r', encoding= 'ISO-8859-1')  #Usamos encoding para poder trabajar con acentos
dicc_emisiones = {  'cod_pais' : [],              # definimos un diccionario
                    'nom_pais' : [],
                    'region' : [],
                    'anio' : [],
                    'co2' : [],
                    'co2_percapita' : []}
s = True

    
for i in archivo: 
        if not s :       
            columna = i.split('|')      
            dicc_emisiones['cod_pais'].append(columna[0])  
            dicc_emisiones['nom_pais'].append(columna[1])   
            dicc_emisiones['region'].append(columna[2])
            dicc_emisiones['anio'].append(columna[3])
            dicc_emisiones['co2'].append((columna[4]))
            dicc_emisiones['co2_percapita'].append((columna[5]))
        else:
            s = False    
            
    
print(dicc_emisiones['co2'])  
    
       
    
#print(dicc_emisiones['region'])




#! Como hago para que no me tome el primer elemento? BUSCAR UNA MANERA MAS EFICIENTE DE SALTARME LA PRIMER FILDA
#! como saco el /n ?
#! no lo puedo convertir a binario



#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#? 2) a) ¿Cuántas variables hay? 
#siete variables
#?  b) ¿Qué tipos de datos usar para cada una? 
#?  c) ¿Qué tipo de variables son? 
#?  d) ¿Hay valores faltantes? 
#?  e) ¿Cuál es el total de emisiones de CO2 para 'América Latina y Caribe' en el año 2010?


#co2 = list(dicc_emisiones['co2'])
#co2.pop(0)
#print(co2)











#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#? 3) Generar una función que reciba como parámetro un diccionario, 
#? cuyas listas de valores tienen el mismo tamaño 
#? y sus elementos enésimos están asociado 
#? Y otros dos parámetros que indican la clave 
#? por la cual debe ordenarse y si es descendente o ascendente.
#?La función debe devolver el diccionario ordenado, 
#? teniendo en cuenta de no perder la relación entre los elementos enésimos.<br>
#?Recibe tres argumentos:<br>
#?        diccionario:    Diccionario a ordenar.<br>
#?        clave:          Clave del diccionario recibido, por la cual ordenar.<br>
#?           descendente:    Un valor booleano, que al ser falso indica ordenamiento descendente y                        ascendente si es verdadero. 
#?                        Debe tratarse de un parámetro por defecto en True.<br>
#?Si el parámetro diccionario no es un tipo de dato diccionario ó el parámetro clave no se encuentra dentro de las claves del diccionario, debe devolver nulo.<br>
#?    Ej:<br>
#?        dicc = {'clave1':['c','a','b'],
#?                'clave2':['casa','auto','barco'],
#?                'clave3':[3,1,2]}
#?        OrdenarDiccionario(dicc, 'clave1')          debe retornar {'clave1':['a','b','c'],
#?                                                               'clave2':['auto','barco','casa'],
#?                                                               'clave3':[1,2,3]}
#?       OrdenarDiccionario(dicc, 'clave3', False)   debe retornar {'clave1':['c','b','a'],
#?                                                               'clave2':['casa','barco','auto'],
#?                                                                'clave3':[3,2,1]}
#? Diccionario para usar de ejemplo:
def dic(dicc, descendente = True):
    
    dicc = { 
                  }
    
 #! no puedo usar sort porque rompe la relacion entre los datos
def ordernardiccionario(diccionario, clave, ascendente=True):
    return 0 