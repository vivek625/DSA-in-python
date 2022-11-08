class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None



class doublyLL:
    def __init__(self):
        self.head = None
#------------------------------------------------------------------------------------------
#               Forward Traversing 
#------------------------------------------------------------------------------------------
    def print_LL(self):
        if self.head is None:
            print("Linkedlist is empty!")
        else:
            n = self.head 
            while n is not None:
                print(n.data,"-->",end = " ")
                n = n.nref
#------------------------------------------------------------------------------------------
#                   Backward Traversing
#------------------------------------------------------------------------------------------
    def print_LL_reverse(self):
        print()
        print("-------Reverse")
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                
                print(n.data,"-->",end = " ")
                n = n.pref
#-----------------------------------------------------------------------------------------
#                  Insert Empty Function
#-----------------------------------------------------------------------------------------
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty!")
#------------------------------------------------------------------------------------------
#              add begin data in Linked list function
#------------------------------------------------------------------------------------------
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
#-------------------------------------------------------------------------------------------
#         add end data in linked list function
#-------------------------------------------------------------------------------------------
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
#-------------------------------------------------------------------------------------------
#       add after data in linked list function
#-------------------------------------------------------------------------------------------
    def add_after(self,data,x):
        if self.head is None:
            print("ll is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is Not present in DLL")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node
#---------------------------------------------------------------------------------------------
#         add before data in linked list function
#---------------------------------------------------------------------------------------------
    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given node is Not present in DLl")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node
#----------------------------------------------------------------------------------------------
#     delete begining in linked list function
#----------------------------------------------------------------------------------------------
    def delete_begin(self):
        if self.head is None:
            print("DLL is empty can't delete!")
            return
        if self.head.nref is None:
            self.head = None
            print("Dll is empty after deleting the node !")
        else:
            self.head = self.head.nref
            self.head.pref = None
#-----------------------------------------------------------------------------------------------
#         delete end in linked list function
#-----------------------------------------------------------------------------------------------
    def delete_end(self):
        if self.head is None:
            print("Dll is empty can't delete!")
            return
        if self.head.nref is None:
            self.head = None
            print("Dll is empty after deleting the node !")
        else:
            n = self.head 
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None
#----------------------------------------------------------------------------------------------
#             delete by value in linked list function
#----------------------------------------------------------------------------------------------
    def delete_by_value(self,x):
        if self.head is None:
            print("Dll us empty can't delete!")
            return 
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print("x is not present in DLL")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("x is Not present in DLL !")
                
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
A = doublyLL()
# A is object
A.print_LL()
A.insert_empty(2)    # --------> insert fucntion 
A.add_begin(10)      # --------> add begin function
A.add_after(30,10)   # --------> add after function
A.add_before(40,30)  # --------> add before function
A.add_end(100)       # --------> add end function
A.delete_begin()     # --------> delete begin fucntion
A.delete_end()       #---------> delete end  data function 
A.delete_by_value(30)#---------> delete by value fucntion
A.print_LL()         #---------> Traversing function forward
A.print_LL_reverse() #---------> Traversing function backward
