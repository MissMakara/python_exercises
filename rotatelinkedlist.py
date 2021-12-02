#rotating a linked list

#create a Node instance
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

def rotateList(list, k):
    #check if the list is empty
    if self.head is None:
        return

    #traverse to the end of the list
    temp = self.head
    length = 0

    if temp.next != None:
        temp = temp.next
        length = length+1

    temp.next = self.head

    #calculate the no. of hops
    hops = length -k
    temp2 = self.head

    #move the head
    while (hops != 0):
        temp2 = temp2.next

    self.head = temp2.next

    #cut of the tail
    temp2.next= None

    return 

    

if __name__ == '__main__':
    k=1
    linkedlist = LinkedList()
    linkedlist.head = Node(1)
    node2= Node(2)
    node3= Node(3)
    node4= Node(4)
    node5= Node(5)

    linkedlist.head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    #rotate the list
    #check if the list is empty
    if linkedlist.head is None:
        print(0)
    
    #traverse to the end of the list
    temp = linkedlist.head
    length = 0

    while temp.next != None:
        temp = temp.next
        length = length+1

    print(length)
    temp.next = linkedlist.head


    #calculate the no. of hops
    hops = length - k
    

    print (hops)

    temp2 = linkedlist.head

    #move the head
    while (hops != 0):
        temp2 = temp2.next
        hops = hops-1

    
    linkedlist.head = temp2.next

    #cut of the tail
    temp2.next= None


    while (linkedlist.head != None):
        print(linkedlist.head.val, end=',')
        linkedlist.head = linkedlist.head.next
  




#output =   rotateRight(, 2)      
