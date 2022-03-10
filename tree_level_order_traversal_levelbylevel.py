class Node():
    def __init__(self,item):
        self.val = item
        self.right = None
        self.left = None

def levelorderTraversal2(root):
    q = []
    
    if root is None:
        return
    
    cur = root
    q.append(cur)

    while q:
        size = len(q)
        while size > 0:
            elem = q.pop(0)
            print(elem.val, end=" ")
            if elem.left:
                q.append(elem.left)

            if elem.right:
                q.append(elem.right)
            
            size = size-1

        print("\n")
    

 

if __name__== "__main__":
    Head = Node(400)
    second = Node(200)
    third = Node(100)
    four = Node(120)
    five = Node(160)
    six = Node(320)
    seven = Node(780)
    nine = Node(220)
    ten = Node(300)
    eleven =Node(560)
    twelve = Node(720)

    Head.left = second
    second.left = four
    second.right = five
    Head.right = third
    third.right = ten
    third.left = nine
    four.left = six
    four.right= seven
    nine.right = eleven
    eleven.left = twelve
   

    output = levelorderTraversal2(Head)

   # print (output)

    