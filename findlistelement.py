#create the Node
class Node:
    def __init__(self, item):
        self.val = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    
    def findelem(self, elem):
        temp = self.head

        while (temp !=None):
            if temp.val == elem:
                return True
            else:
                temp = temp.next

        return False

    def getnthnode(self, pos):
        temp = self.head
        count = 0

        while temp!= None:
            if count != pos:
                temp = temp.next
                count = count+1
            else:
                return temp.val

        return False

    def getnfromlast(self, pos):
        #traverse to the end and get the length
        temp = self.head
        length = 0

        

        while temp!=None:
            temp = temp.next
            length =length +1
        print (length)

        if pos > length:
            x = "The position is not within the list"
            return x

        #calculate no. of hops from the beginning
        hops = length - pos

        #go to the element
        temp2 = self.head
        while hops!= 0:
            temp2 = temp2.next
            hops =hops-1

        return temp2.val
            

    
if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    #connect the nodes
    linkedlist.head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    #call  the find element node
    output = linkedlist.getnfromlast(0)
    print(output)

            
