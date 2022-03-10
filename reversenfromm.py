class Node:
    def __init__(self,item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def reverse(head,m,n):
    if head is None:
        return 
    cur = head
    prev =None

    j = m
    x = abs(n- m)
    
    #get the first sub linked list
    while cur and m-1>1:
        m= m-1
        cur = cur.next
   
    temp2 = cur.next
    cur.next = None

    return cur

    # print("x is", x)
    # while temp2 and x>1:
    #     temp2 = temp2.next
    #     x = x-1

    # cur3 = temp2.next
    #temp2.next =None

    #revere temp2
    # while temp2:
    #     next = temp2.next
    #     temp2.next = prev

    #     prev = temp2
    #     temp2 = next
        

    # while x > 0:
    #     if cur:
    #         next = cur.next
    #         cur.next = prev
    #         x= x-1
    #         prev = cur
    #         cur = next

    

def printList(head):
    cur = head

    while cur:
        print(cur.data, end=" ")
        cur = cur.next

if __name__ == "__main__":
    llist = LinkedList()

    llist.head = Node(85)
    second = Node(15)
    third = Node(4)
    fourth = Node(20)
    fifth =Node(3)
    sixth = Node(9)
    seventh = Node(10)
    eigth = Node(32)
    ninth = Node (6)
    tenth =Node(12)


    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next =sixth
    sixth.next = seventh
    seventh.next =eigth
    eigth.next = ninth
    ninth.next = tenth
    tenth.next = None

    print("initial linked list:")
    printList(llist.head)
    output = reverse(llist.head,4,8)
    print(" ")
    print("new list:")
    printList(output)

