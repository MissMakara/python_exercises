class Node():
    def __init__(self,item):
        self.val = item
        self.right = None
        self.left = None


def iterative_preorder(root):
    stack = []
    if root is None:
        return

    
    if root:
        stack.append(root)

    while stack:
        elem = stack.pop()
        print(elem.val, end=" ")
        if elem.right:
            stack.append(elem.right)
        if elem.left:
            stack.append(elem.left)

    else:
        return  

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
   

    output = iterative_preorder(Head)