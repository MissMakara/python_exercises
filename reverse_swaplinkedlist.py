class Node():
    def __init__(self,item):
        self.data = item
        self.next=None
       

class LinkedList():
    def __init__(self):
        self.head =None

def halfList(Head):
    slow = Head
    fast = Head
    prev =None

    while fast:
        prev=slow
        slow = slow.next
        fast =fast.next.next

    Head2 = slow
    prev.next =None
    return Head, Head2

def reverseList(head):
    cur =head
    prev =None
    next = None

    while cur:
        next = cur.next
        cur.next = prev

        prev = cur
        cur = next

    return prev

def mergeAlternateList(head, head2):
    cur = head
    cur2 = head2
    prev=head

    while cur and cur2:
        next = cur.next
        next2 = cur2.next
       
        
        # q_curr.next = p_next  # change next pointer of q_curr
        # p_curr.next = q_curr  # change next pointer of p_curr
 
        cur.next = cur2
        cur2.next = next

        
        cur = next
        cur2 = next2
    
    return prev


def printList(head):
    cur = head

    while cur:
        print(cur.data, end=" ")
        cur =cur.next

    
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

    print("initial list")
    printList(llist.head)
    print(" ")
    list1, list2 = halfList(llist.head)
    print("List 1:")
    printList(list1)
    print("")
    print("List 2")
    printList(list2)
    print("")
    print("Reversing List 2")
    output = reverseList(list2)
    printList(output)

    print("")
    print("Alternately merging List i and List 2")
    merged = mergeAlternateList(list1, output)
    # merged = merge(list1, list2)
    printList(merged)