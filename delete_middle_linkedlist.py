# Given a singly linked list, delete the middle of the linked list.
#find the middle
#get cur = cur.next
#prev.next = cur
class Node():
    def __init__(self, item):
        self.data = item
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None

class Solution():
    def delLinkedlist(self,head):
        if head is None:
            return None
        self.printlist(head)
        print("")
        fast = head 
        slow = head
        prev =None
        next =None

        while fast is not None and fast.next is not None:
            prev =slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = slow.next
        slow.next =None
        
        self.printlist(head)
        return head

    def printlist(self,head):
        if head is None:
            return None
        
        cur =head
        while cur:
            print(cur.data, end=" ")
            cur=cur.next
    

if __name__ == "__main__":

    llist = LinkedList()

    llist.head = Node(85)
    second = Node(15)
    third = Node(4)
    fourth = Node(20)
    fifth = Node(25)

    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next =None
   

    sol = Solution()
    output = sol.delLinkedlist(llist.head)
    #print(output)

        

