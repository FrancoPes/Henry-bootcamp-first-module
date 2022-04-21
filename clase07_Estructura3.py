


#? ARBOLES EN GENERAL
#Arboles en python: son estructuras de nodos que basicamente tienen distintas direcciones
#son como un arbol pero al reves
#al primer nodo le llamamos raiz
# padre: nodo que tiene hijos
#hijos: nodos que decienden de otros nodos
# hermanos: nodos que comparten el mismo padre
# hojas: nodos sin hijos, estan en el ultimo nivel
# nivel: numero de conexiones entre un nodo x y la raiz
#! OJO: siempre debe haber un solo camino, los nodos g=hermanos no pueden estar conectados
#camino: secuencia de nodos


#? 1) ARBOL BINARIO
# es un tipo de arbol en el cual cada nodo puede tener como maximo 2 hijos o ninguno



class Nodo:
    def __init__(self, dato):     #creamos el nodo. cada nodo tiene 3 atributos:
        self.dato = dato           # el dato
        self.right = None          #ir a la derecha
        self.left = None           #ir a la izquierda
                                    #LISTO, creada la clase nodo
                                
                                
class Binarytree(object):        #creamos la clase arbol binario
    def __init__(self):      #le pasamos como parametro la raiz, es decir que el primer elemento
        self.root_atributo = None    
    def insert(self, dato):         #si no hay ninguna raiz, el valor es la nueva raiz
        if self.root_atributo is None:
            self.root_atributo = Nodo(dato)
        else: 
            self._insert(dato, self.root_atributo)   #sino pasa a la siguiente funcion (_insert)
    def _insert(self, dato, current_node):             #si daro es menor al current_node
        if dato < current_node:
            if current_node.left is None:              #si el hijo de la izquierda de current es nulo
                current_node.left = Nodo(dato)           #hacemos un nodo a la izquierda
            else:
                self._insert(self, dato, current_node.left)    # si no, aplicamos lo mismo pero no el hijo izquiedo (recursividad)
        elif dato > current_node:     
            if current_node.right is None:
                current_node.right = Nodo(dato)
            else:
                self._insert(self, dato, current_node.right)   
        else:
            print('El valor ya esta en el arbol')           #OJO, SI SELECCIONAMOS LOS VALORES POR MAYOR O MENOR, NO PODEMOS TENER REPETIDOS
            
    
    def find_value(self, dato):
        if self.root_atributo != None:                   #si hay contenido en el arbol
            is_found = self.find(self, dato, self.root_atributo)
            if is_found == True:              # si lo encuentro, devolve true. para que lo encuentre pasamos a la otra funcion
                return True
            else:                            #si no lo encuentra, falso
                return False
        else:
            return None
                                   #para saber cuando lo encuentro, recurro a la otra funcion
        
    def find (self, dato, current_node):                          
        if dato > current_node and current_node.right != None:      #la idea es recorrer hasta que el dato sea igual al current node
            return self.find(self, dato, current_node.right)                  #cuando eso es true, isfound es true
        elif dato < current_node and current_node.left != None:
            return self.find(self, dato, current_node.left)
        else:
            if dato == current_node.dato:
                return True
            
    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)
        
        
tree = Binarytree(1)
tree.root.left = Nodo(2)
tree.root.right = Nodo(3)
tree.root.left.left = Nodo(4)
tree.root.left.right = Nodo(5)

print(tree.height(tree.root))
        
   
   
  #  def preorder_print(self,start, transversal):      
        
        
        
        
        
        
        
        
        
              

                    
                










#? 2) Arbol binario AVL

#Es un tipo de arbol que se balancea automaticamente
#se mantiene todo el tiempo balanceado


#? 2) Arbol heap

# cada nodo contiene un valor mayor o igual al de sus hijos
# la suma de los hijoS SI PUEDE Sser mayor a la de su padre
























































