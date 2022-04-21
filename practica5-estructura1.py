

#? 1) Implementar un juego, que consista en apilar números enteros del 1 al 20, de forma aleatoria, para lo cual debe usarse una estructura de Pila. 
#? Luego, el usuario debe elegir un número de veces en que se va a quitar elementos de la pila, los cuales, sumados entre sí, no deben superar el valor de 50.
#? El usuario pierde si la suma supera ese valor. Si no lo supera, gana, pero su calificación será 10 menos el número elementos que falten quitar para todavía no superar 50.
#? El programa debe informar si perdió, y si ganó, con qué calificación lo hizo.

#? Consideraciones:<br>
#? a. Se puede usar la función input() para obtener una entrada de teclado.<br>
#? b. Se puede usar la el modulo random para obtener valores aleatorios.
import random



#Reglas del juego
print('JUEGO DE LAS BOLILLAS----------------------------------------------------------------------------------------\n')
print('\nReglas del juego\n')
print('>> El jugador debe escoger el numero de bolillas que desea obtener')
print('>> La suma de las bolillas no debe superar 50')
print('>> El puntaje se obtiene restando a 50 la suma de las bolillas')
print('>> Si la suma supera 50, el jugador queda eliminado')
print('>> gana el jugador que obtenga el menor puntaje')

# Input del usuario
cartas_extraidas = int(input(f'\nIntroduzca el numero de cartas que deseea extraer: '))


#barajar lista y definir la segunda lista
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(lista)
lista2 = []


#defino contador para los for
suma = 0
puntaje = 0
# condicionales
if cartas_extraidas == 1:
    a = lista.pop() 
    lista2.append(a)   
    for i in lista2:
      suma = suma + i
      puntaje = 50 - suma
    print(f'Extrajo la bolilla {a} y su puntaje es de {puntaje} puntos')
    
if cartas_extraidas == 2:
    a = lista.pop()
    b = lista.pop() 
    lista2.append(a)
    lista2.append(b)    
    for i in lista2:
      suma = suma + i
      puntaje = 50 - suma
    print(f'Extrajo dos bolillas: {a} y {b}. Con lo cual, su puntaje es de {puntaje} puntos')  
    
if cartas_extraidas == 3:
    a = lista.pop()
    b = lista.pop() 
    c = lista.pop() 
    lista2.append(a)
    lista2.append(b) 
    lista2.append(c)    
    for i in lista2:
      suma = suma + i
      puntaje = 50 - suma
    if puntaje >= 0:
        print(f'Extrajo tres bolillas: {a}, {b} y {c} . Con lo cual, su puntaje es de {puntaje} puntos')  
    else:
        print(f'Has perdido el juego. Extrajo dos bolillas: {a}, {b} y {c}.suman {suma}')

if cartas_extraidas == 4:
    a = lista.pop()
    b = lista.pop() 
    c = lista.pop() 
    d = lista.pop()
    lista2.append(a)
    lista2.append(b) 
    lista2.append(c)   
    lista2.append(d)  
    for i in lista2:
      suma = suma + i
      puntaje = 50 - suma
    if puntaje >= 0:
        print(f'Extrajo cuatro bolillas: {a}, {b}, {c} y {d} . Con lo cual, su puntaje es de {puntaje} puntos')  
    else:
        print(f'Has perdido el juego. Extrajo dos bolillas: {a}, {b}, {c} y {d}.suman {suma}')

if cartas_extraidas == 5:
    a = lista.pop()
    b = lista.pop() 
    c = lista.pop() 
    d = lista.pop()
    e = lista.pop()
    lista2.append(a)
    lista2.append(b) 
    lista2.append(c)   
    lista2.append(d)
    lista2.append(e)  
    for i in lista2:
      suma = suma + i
      puntaje = 50 - suma
    if puntaje >= 0:
        print(f'Extrajo cinco bolillas: {a}, {b}, {c}, {d} y {e} . Con lo cual, su puntaje es de {puntaje} puntos')  
    else:
        print(f'Has perdido el juego. Extrajo dos bolillas: {a}, {b}, {c}, {d} y {e}.suman {suma}')

if cartas_extraidas == 6:
    a = lista.pop()
    b = lista.pop() 
    c = lista.pop() 
    d = lista.pop()
    e = lista.pop()
    f = lista.pop()
    lista2.append(a)
    lista2.append(b) 
    lista2.append(c)   
    lista2.append(d)
    lista2.append(e)  
    lista2.append(f)
    for i in lista2:
      suma = suma + i
      puntaje = 50 - suma
    if puntaje >= 0:
        print(f'Extrajo seis bolillas: {a}, {b}, {c}, {d}, {e} y {f} . Con lo cual, su puntaje es de {puntaje} puntos')  
    else:
        print(f'Has perdido el juego. Extrajo dos bolillas: {a}, {b}, {c}, {d}, {e} y {f}.suman {suma}')

if cartas_extraidas == 7:
    a = lista.pop()
    b = lista.pop() 
    c = lista.pop() 
    d = lista.pop()
    e = lista.pop()
    f = lista.pop()
    g = lista.pop()
    lista2.append(a)
    lista2.append(b) 
    lista2.append(c)   
    lista2.append(d)
    lista2.append(e)  
    lista2.append(f)
    lista2.append(g)
    for i in lista2:
      suma = suma + i
      puntaje = 50 - suma
    if puntaje >= 0:
        print(f'Extrajo siete bolillas: {a}, {b}, {c}, {d}, {e}, {f} y {g}. Con lo cual, su puntaje es de {puntaje} puntos')  
    else:
        print(f'Has perdido el juego. Extrajo dos bolillas: {a}, {b}, {c}, {d}, {e}, {f} y {g}.suman {suma}')

if cartas_extraidas == 8:
    a = lista.pop()
    b = lista.pop() 
    c = lista.pop() 
    d = lista.pop()
    e = lista.pop()
    f = lista.pop()
    g = lista.pop()
    h = lista.pop()
    lista2.append(a)
    lista2.append(b) 
    lista2.append(c)   
    lista2.append(d)
    lista2.append(e)  
    lista2.append(f)
    lista2.append(g)
    lista2.append(h)
    for i in lista2:
      suma = suma + i
      puntaje = 50 - suma
    if puntaje >= 0:
        print(f'Extrajo ocho bolillas: {a}, {b}, {c}, {d}, {e}, {f}, {g} y {h}. Con lo cual, su puntaje es de {puntaje} puntos')  
    else:
        print(f'Has perdido el juego. Extrajo dos bolillas: {a}, {b}, {c}, {d}, {e}, {f}, {g} y {h}.suman {suma}')

if cartas_extraidas == 9:
    a = lista.pop()
    b = lista.pop() 
    c = lista.pop() 
    d = lista.pop()
    e = lista.pop()
    f = lista.pop()
    g = lista.pop()
    h = lista.pop()
    i = lista.pop()
    lista2.append(a)
    lista2.append(b) 
    lista2.append(c)   
    lista2.append(d)
    lista2.append(e)  
    lista2.append(f)
    lista2.append(g)
    lista2.append(h)
    lista2.append(i)
    for i in lista2:
      suma = suma + i
      puntaje = 50 - suma
    if puntaje >= 0:
        print(f'Extrajo nueve bolillas: {a}, {b}, {c}, {d}, {e}, {f}, {g}, {h} y {i}. Con lo cual, su puntaje es de {puntaje} puntos')  
    else:
        print(f'Has perdido el juego. Extrajo dos bolillas: {a}, {b}, {c}, {d}, {e}, {f}, {g}, {h} y {i}.suman {suma}')
        
if cartas_extraidas > 9:
    print('Extraiga una cantidad de bolillas menor a 9')

'''

#JUEGO MAQUINA DE CASINO. EL JUEGO CONSISTE EN EMPEZAR CON CIERTA CANTIDAD DE DINERO, CUANDO EL USUARIO INTRODUZCA EL DINERO, 
#EMPIEZA EL JUEGO CUANDO EL USUARIO LE DA A ACEPTAR SE LARGA LA MAQUINA
#SI HAY UN ACIERTO TOTAL, EL USUARIO GANA 500 PESOS
#SI HAY UNO PARCIAL, EL USUARIO GANA 50 PESOS
#SI NO HAY ACIERTO, PIERDO 100 PESOS

import random





#1) chequear que haya aciertos o no. realizar los condicionales

a = random.randint(1,5)
b = random.randint(1,5)
c = random.randint(1,5)


vueltas = int(input(f'cuantas vueltas: '))
boton_aceptar = input(f'Quieres tirar: ')
credito = 0

if boton_aceptar == 'si':
    print(f'Has obtenido las bolillas {[a]}-{[b]}-{[c]}')
    if a != b and b != c and a != c:
        print('No has acertado esta vez, sigue intentandolo')
        resultado1 = -50
        credito = vueltas*100 - resultado1
        print(f'tu ganancia es de {credito}')
    if a == b and b == c and a == c:
        print('Acertaste, ganaste $400')
        resultado2 = 400
        credito = vueltas*100 - resultado2
        print(f'tu ganancia es de {credito}')
    if a == b or b == c or a == c:
        print('Has conseguido un acierto, ganaste $50')
        resultado3 = 100
        credito = vueltas*100 - resultado3
        print(f'tu ganancia es de {credito}')
        

    


#2)crear input con el ingreso del dinero y ademas contar el dinero del cliente



'''




