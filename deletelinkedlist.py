class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

def deleteList(head):
    if head is None:
        return None

    cur = head
    next = None

    if head:
       # head = None
        s = "LinkedList deleted"

        return head


def deleteLinkedList(head):
    if head is None:
        return None

    cur = head
    next = None
    print("linked list is:")
    while cur:
        print(cur.data,end = " ")
        next = cur.next
        del cur.data
        cur = next
    print(" ")
    print("Linked list deleted")
    return cur

if __name__ == "__main__":

    llist = LinkedList()

    llist.head = Node(85)
    second = Node(15)
    third = Node(4)
    fourth = Node(20)

    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = None

    output = deleteLinkedList(llist.head)
    print(output)