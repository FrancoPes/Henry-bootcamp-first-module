##
###Stack Data Structure.


class Stack():                     #creamos un stack, el cual es una lista
    def __init__(self):
        self.items = []

    def push(self, item):      #agrgamos uno al final
        self.items.append(item)				

    def pop(self):                 #borramos uno al final
        return self.items.pop()
    
    def is_empty(self):               #devuelve si esta vacia o no  
        return self.items == []
    
    def peek(self):                    #devuelve ultimo elemento de la pila
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):        #simplemente devuelve el stack
        return self.items
    def reverse_string(stack, input_str):      #devuelve del string dado vuelta

    # Loop through the string and push contents
    # character by character onto stack.
     for i in range(len(input_str)):
        stack.push(input_str[i])

     rev_str = ""
     while not stack.is_empty():
        rev_str += stack.pop()

     return rev_str

    
    """
Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))
"""



def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False
    
    
    
    
    
    
    
    
    
    
    
############queue

class Queue(object):
    def __init__(self):
        self.item = []

    def enqueue(self, item):
        self.item.insert(0, item)

    def dequeue(self):
        if self.item:
            self.item.pop()
        else:
            return None

    def peek(self):                  
        if self.item:
            return self.item[-1]

    def isempty(self):
        if self.item == []:
            return True
        else:
            return False

    def size(self):
        return len(self.item)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(item=1)
    queue.enqueue(item=2)
    print("Size\t{}".format(queue.size()))
    print("Peek\t{}".format(queue.peek()))

    queue.dequeue()
    print("Size\t{}".format(queue.size()))
    print("Peek\t{}".format(queue.peek()))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




















































































































