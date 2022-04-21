
#? LISTAS ENLAZADAS

# Son basicamente una secuencia de nodos enlazados de forma Unidireccional (cuando son enlazadas simples). 
# Son una especie de cadena de nodos enlazados de forma unidireccional
# Pueden estar enlazadas de manera simple, doble o multiple. ahora nos concentramos en las simples

#? 1.1 Sobre los nodos:
# Cada nodo es un objeto en si
# Es como si fuera una 'caja' (Box)
# Tiene dos atributos principales
# Valor (entero o string)
# Punter0 (con que nodo esta linkeado). en este caso seria el next

#? 1.2 Creacion de la clase nodos

class Node:
    def __init__(self,val):
        self.data = val        #asignamos los atributos de Node, que son valor y puntero
        self.next = None  
        
    def getData(self):
        return self.data     #obtenemos el dato de un nodo

    def getNext(self):        # pasar al otro nodo (por ahora esta en nulo)
       return self.next

    def setData(self, val):     # esto es para introducir un valor
         self.data = val

    def setNext(self, val):   # introducir el valor del otro
        self.next = val

#creacion de la clase lista enlazada

class LinkedList:
    def __init__(self):         # creamos la lista enlazada y head es = none
         self.head = None
 
    def isEmpty(self):
         """Check if the list is empty"""     #chequeamos que no sea varia
         return self.head is None
 
    def add(self, item):
         """Add the item to the list"""        #funcion agregar items(valores dentro de nodos)
         new_node = Node(item)                   #tiene como parametro el valor o item del nuevo nodo
         new_node.setNext(self.head)             #! CONSULTAR
         self.head = new_node
 
    def size(self):
         """Return the length/size of the list"""    #contamos la cantidades de nodos no nulos
         count = 0
         current = self.head
         while current is not None:
             count += 1
             current = current.getNext()
         return count
 
    def search(self, item):
         """Search for item in list. If found, return True. If not found, return False"""
         current = self.head
         found = False                               #con este metodo buscamos un archivo que este en la lista
         while current is not None and not found:         #itera uno por uno
             if current.getData() is item:
                 found = True
             else:
                 current = current.getNext()
         return found
 
    def remove(self, item):
         """Remove item from list. If item is not found in list, raise ValueError"""
         current = self.head
         previous = None
         found = False
         while current is not None and not found:
             if current.getData() is item:
                 found = True
             else:
                 previous = current
                 current = current.getNext()
         if found:
             if previous is None:
                 self.head = current.getNext()
             else:
                 previous.setNext(current.getNext())
         else:
             raise ValueError
             print ('Value not found')
 
    def insert(self, position, item):
         """
         Insert item at position specified. If position specified is
         out of bounds, raise IndexError
         """
         if position > self.size() - 1:
             raise IndexError
             print ("Index out of bounds.")
         current = self.head
         previous = None
         pos = 0
         if position is 0:
             self.add(item)
         else:
             new_node = Node(item)
             while pos < position:
                 pos += 1
                 previous = current
                 current = current.getNext()
             previous.setNext(new_node)
             new_node.setNext(current)
 
    def index(self, item):
         """
         Return the index where item is found.
         If item is not found, return None.
         """
         current = self.head
         pos = 0
         found = False
         while current is not None and not found:
             if current.getData() is item:
                 found = True
             else:
                 current = current.getNext()
                 pos += 1
         if found:
             pass
         else:
             pos = None
         return pos
 
    def pop(self, position = None):
         """
         If no argument is provided, return and remove the item at the head. 
         If position is provided, return and remove the item at that position.
         If index is out of bounds, raise IndexError
         """
        
         if position > self.size():
             print ('Index out of bounds')
             raise IndexError
             
         current = self.head
         if position is None:
             ret = current.getData()
             self.head = current.getNext()
         else:
             pos = 0
             previous = None
             while pos < position:
                 previous = current
                 current = current.getNext()
                 pos += 1
                 ret = current.getData()
             previous.setNext(current.getNext())
                print(ret)
                return ret
 
    def append(self, item):
         """Append item to the end of the list"""
         current = self.head
         previous = None
         pos = 0
         length = self.size()
         while pos < length:
             previous = current
             current = current.getNext()
             pos += 1
         new_node = Node(item)
         if previous is None:
             new_node.setNext(current)
             self.head = new_node
         else:
             previous.setNext(new_node)
 
    def printList(self):
       """Print the list"""
        current = self.head
        while current is not None:
           print current.getData()
           current = current.getNext()
           
                          
    









































