


#LISTAS ENLAZADAS SIMPLE
class Node:                     # Definimos el nodo que tiene dos atributos
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:                # Creamos la linked list
    def __init__(self):
        self.head = None          #solo la cabeza que es un none

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:     #si la lista esta vacia, el dato ingresado es la cabeza
            self.head = new_node
            return

        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next     #m
        last_node.next = new_node
    
    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node != None:   
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
#-------------------------------------------------------------------------------------------------------------------------#
    def prepend(self, data):
        new_node = Node(data)        #PONEMOS UN NODO PRIMERO ANTES DE LA CABEZA

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):  #INSERTAMOS UN NODO DESPUES DE OTRO X

        if not prev_node:
            print("Previous node is not in the list")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node
    
    
    def delete_node(self, key):                  

        cur_node = self.head

        if cur_node != None and cur_node.data == key:   #SI EL QUE QUIERO BORRAR ESTA EN LA CABEZA
            self.head = cur_node.next
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):   #0 ES EL PRIMERO Y ASI

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node 
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None
        
        
    
    
    
    '''swap by changing the next attribute of node'''
    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return 

        prev_1 = None 
        curr_1 = self.head 
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1 
            curr_1 = curr_1.next

        prev_2 = None 
        curr_2 = self.head 
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2 
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return 

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next
        
    ''' Alternate swap node function , swap by changing the data attribute of node '''
    def swap_nodes_alt(self, key_1, key_2):
        if key_1 == key_2:
            return
        curr  = self.head
        x , y = None , None # Assign None to avoid reference error
        while curr :
            if curr.data == key_1:
                x = curr # key_1 found
            if curr.data == key_2:
                y =curr # key_2 found
            curr = curr.next
        
        if x and y: # Check if both key's exist
            x.data , y.data = y.data , x.data
        else : 
            return
        
    def reverse_iterative(self):    #nos da la lista pero al reves

        prev = None 
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            
            self.print_helper(prev, "PREV")
            self.print_helper(cur, "CUR")
            self.print_helper(nxt, "NXT")
            print("\n")

            prev = cur 
            cur = nxt 
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)
   
    def merge_sorted(self, llist):
    
        p = self.head 
        q = llist.head
        s = None
    
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p 
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s 
        while p and q:
            if p.data <= q.data:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q 
        if not q:
            s.next = p 
        return new_head
    def remove_duplicates(self):   #sacamos los duplicados
        
        cur = self.head
        prev = None

        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # Remove node:
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n):

        # # Method 1:
        # total_len = self.len_iterative()

        # cur = self.head 
        # while cur:
        #     if total_len == n:
        #         print(cur.data)
        #         return cur
        #     total_len -= 1
        #     cur = cur.next
        # if cur is None:
        #     return

        # Method 2:
        p = self.head
        q = self.head

        count = 0
        while q and count < n:
            q = q.next
            count += 1

        if not q:
            print(str(n) + " is greater than the number of nodes in list.")
            return

        while p and q:
            p = p.next
            q = q.next
        return p.data
    def rotate(self, k):
        p = self.head 
        q = self.head 
        prev = None
        
        count = 0
        
        while p and count < k:
            prev = p
            p = p.next 
            q = q.next 
            count += 1
        p = prev
        while q:
            prev = q 
            q = q.next 
        q = prev 

        q.next = self.head 
        self.head = p.next 
        p.next = None

    def count_occurences_iterative(self, data):   #numero de veces que se repite
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count 

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0 
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)
    
    def is_palindrome(self):   #CAPICUA
        # Method 1:
        # s = ""
        # p = self.head 
        # while p:
        #     s += p.data
        #     p = p.next
        # return s == s[::-1]

        # Method 2:
        # p = self.head 
        # s = []
        # while p:
        #     s.append(p.data)
        #     p = p.next
        # p = self.head
        # while p:
        #     data = s.pop()
        #     if p.data != data:
        #         return False
        #     p = p.next
        # return True

        # Method 3
        p = self.head 
        q = self.head 
        prev = []
        
        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i-1]
    
        count = 1

        while count <= i//2 + 1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True
    
    def move_tail_to_head(self):   #MOVER LA COLA A LA CABEZA
        
        last = self.head 
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next
        last.next = self.head 
        second_to_last.next = None 
        self.head = last
    
    def sum_two_lists(self, llist):
        p = self.head  
        q = llist.head

        sum_llist = LinkedList()

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0 
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_llist.print_list()
        
    
        
        
        
        
        
        
        
        
        
        
llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()

#llist = LinkedList()
#llist.append("A")
#llist.append("B")
#llist.append("C")
#llist.append("D")

#llist.print_list()

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

# llist.prepend("E")
llist.insert_after_node(llist.head.next, "E")

