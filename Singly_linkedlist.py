class Node:
    def __init__(self,data):
        self.data = data 
        self.val = None
#-----------------------------------------------------------------------------------------------
class Linkedlist:
    def __init__(self):
        self.head = None
#-----------------------------------------------------------------------------------------------
#             Tarversal function
#-----------------------------------------------------------------------------------------------
    def Display(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"---->",end = " ")
                n = n.val
#-----------------------------------------------------------------------------------------------
#         insert beigning data in linkedlist function
#-----------------------------------------------------------------------------------------------
    def add_begin(self,data):
        new_node = Node(data)
        new_node.val= self.head
        self.head = new_node
#-----------------------------------------------------------------------------------------------
#        insert end data in linkedkist fucntion
#-----------------------------------------------------------------------------------------------
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head 
            while n.val is not None:
                n = n.val
            n.val = new_node
#-----------------------------------------------------------------------------------------------
#         insert after data in linked list function
#-----------------------------------------------------------------------------------------------
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.val
        if n is None:
            print("node is not present in ll")
        else:
            new_node =  Node(data)
            new_node.val = n.val
            n.val = new_node
#-------------------------------------------------------------------------------------------------
#          insert before data in linked list function
#-------------------------------------------------------------------------------------------------
    def add_before(self,data,x):
        if self.head is None:
            print("linkedlist is empty")
            return 
        if self.head.data == x:
            new_node = Node(data)
            new_node.val = self.head
            self.head = new_node
            return
        n = self.head
        while n.val is not None:
            if n.val.data == x:
                break
            n = n.val
        if n.val is None:
            print("Node is not found !")
        else:
            new_node = Node(data)
            new_node.val = n.val
            n.val = new_node
#---------------------------------------------------------------------------------------------------
#       insert empty check 
#---------------------------------------------------------------------------------------------------
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linkedlist is not empty")
#----------------------------------------------------------------------------------------------------
#         delete begining in linked list 
#----------------------------------------------------------------------------------------------------
    def delete_begin(self):
        if self.head is None:
            print("ll is empty so we cant delete node")
        else:
            self.head = self.head.val
#---------------------------------------------------------------------------------------------------
#          delete end linked list
#---------------------------------------------------------------------------------------------------
    def delete_end(self):
        if self.head is None:
            print("linkedlist is empty")
        elif self.head.val is None:
            self.head = None
        else:
            n = self.head
            while n.val.val is not None:
                n = n.val
            n.val = None
#---------------------------------------------------------------------------------------------------
#       delete by value linkedlist
#---------------------------------------------------------------------------------------------------
    def delete_by_value(self,x):
        if self.head is None:
            print("can't delete ll is empty!")
            return 
        if x == self.head.data:
            self.head = self.head.val
            return
        n = self.head
        while n.val is not None:
            if x == n.val.data:
                break
            n = n.val
        if n.val is None:
            print("Node is not present!")
        else:
            n.val = n.val.val
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
ll = Linkedlist()   
ll.add_begin(10)
ll.add_before(11,10)
ll.insert_empty(12)
ll.add_after(50,10)
ll.add_end(50)
ll.add_begin(20)
# ll.add_after(20,30)
# ll.add_end(50)
ll.delete_by_value(10)
ll.delete_begin()
ll.delete_end()
ll.Display()
