class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def reverseLinkedList(self):
        prev = None
        next = None
        cur = self.head

        while cur:
            #holds the place for next
            next = cur.next
            #make the cur pointer point backwards
            cur.next = prev

            #move one step forward
            prev = cur
            cur = next

        self.head = prev

    def insertItem(self, head, item):
        if head:
            if item:
                newNode = Node(item)
                #go to the location to be inserted

                #insert the node
                newNode.next = None

        else:
            if item:
                head = Node(item)


def printLinkedList(head):
        cur = head
        
        while cur:
            print(cur.data, end= " ")
            cur = cur.next


def reverseEveryKNodes(head, k):
        if head is None:
            return None

        count = 0
        cur = head
        
        cur2 = head
        prev = None
        next = None

        while cur and count < k:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            count+=1
            
        if next is not None:
            head.next = reverseEveryKNodes(next, k)
        
        return prev
        

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

    output = reverseEveryKNodes(llist.head, 3)
    printLinkedList(output)
