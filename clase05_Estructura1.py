#la idea es organizar datos para usarlos de forma mas independientes
#si tengo mis libros desordenados, como se donde esta un libro x
# como los ordenos?





print('PILAS---------------------------------------------------------------------------------------------------\n')
#? 1) PILAS
# una primera estructura son las PILAS
# el concepto de pilas es colectar datos. los acomodamos de una forma especial
# usamos push para agregar un dato. pop para sacar
# despues tenemos los queue (colas)
# aqui usamos el metodo Last in first out (LIFO)

# Para implementar una pila, por lo tanto, necesitamos dos operaciones simples:
#? push – agrega un elemento a la parte superior de la pila:
#? pop – elimina el elemento en la parte superior de la pila:

#! CREAR UNA CLASE

#ejemplo de implementacion : Imagina que eres un desarrollador que trabaja en un nuevo procesador de textos. 
# Tiene la tarea de crear una función de deshacer, lo que permite a los usuarios retroceder en sus acciones 
# hasta el comienzo de la sesión.
#Una pila es ideal para este escenario. Podemos registrar cada acción que realiza el usuario empujándola a la pila


#? CREAR UNA CLASE:
class Estructura_Pila(object):  #creamos una clase que sea una pila
     def __init__(self):
         self.__list = []       #metemos una lista
 
     # Lo que hace el push es agregar un elemento a la pila. simplemente es un APPEND
     def push(self, item):
         self.__list.append(item)
 
     # Quitar un elemento de la Pila. es un simple pop
     def pop(self):
         return self.__list.pop()
 
     # Obtener el elemento superior de la pila
     def peek(self):
         if self.__list:
             return self.__list[-1]
         else:
             return None
 
     # Determinar si la Pila está vacía
     def is_empty(self):
         return self.__list == []
 
     # Devuelve el número de elementos en la Pila
     def size(self):
         return len(self.__list)


print('\nCOLAS---------------------------------------------------------------------------------------------------\n')
#? 2) COLAS
#Las colas, como sugiere el nombre, siguen las Primero en entrar primero en salir (FIFO) principio. 
# Como si esperara en una cola las entradas del cine,

#Para implementar una cola, por lo tanto, necesitamos dos operaciones simples:

#? enqueue – agrega un elemento al final de la cola:
#? dequeue – elimina el elemento al principio de la cola:

class Estructura_Cola(object):
     def __init__(self):
         self.__list = []      #creamos una cola, por supuesto que necesitamos una lista
 
     # Agregar un elemento en la Cola
     def enqueue(self, item):
         self.__list.append(item)
 
     # Quitar un elemento de la Cola
     def dequeue(self):
         return self.__list.pop(0)
 
     # Verificar si la Cola está vacía
     def is_empty(self):
         return self.__list == []
 
     # Devolver cantidad de elementos den la Cola
     def size(self):
         return len(self.__list)
