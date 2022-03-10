# Given two numbers represented by two linked lists, write a function that returns the sum list. 
# The sum list is linked list representation of the addition of two input numbers. 
# It is not allowed to modify the lists. 
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head =None

def addLlists(head1, head2):
    cur1 = head1
    cur2 = head2
    
    str1=""
    str2=""
    while cur1:
        str1 = str+cur1.data
        cur1 = cur1.next
    while cur2:
        str2 = str+cur2.data
        cur2 = cur2.next

    x = int(str1)+int(str2)
    llist3 = LinkedList()

    for char in str(x):
        llist3.head = Node(char)
        head.next = 


    

