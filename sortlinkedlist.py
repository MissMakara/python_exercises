# "Given the head of a linked list, return the list after sorting it in ascending order. 
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?"

class Node():
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None


class Solution():
    def sortList(self,head):
        if head is None or head.next is None:
            return 
            
        cur = head
        next = None

        while cur is not None and cur.next is not None:
            next = cur.next
            
            if next.data < cur.data:
                temp = next.next
                next.next = cur
                cur.next = temp
            else:
                cur = next


        return head



    def printList(self, head):
        if head is None:
            return None
        
        cur = head
        next = None

        while cur:
            print(cur.data,end=" ")

            cur = cur.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(4)
    llist.head.next = Node(2)
    llist.head.next.next = Node(1)
    llist.head.next.next.next =Node(3)

    sol = Solution()
    print("unsorted list\n")
    sol.printList(llist.head)
    
    output = sol.sortList(llist.head)
    print("\nsorted list\n")
    sol.printList(output)
   