#left>root>right
class Node:
    def __init__(self, item):
        self.val = item
        self.right = None
        self.left = None

def inorderTraversalx(root):

    if root is None:
        return None
    
    else:
        print("root has stuff")

    stack = []
    
    #while True:
    if root:
        print("push to stack")
        stack.append(root)
        if root.left:
            root= root.left

    else:
        if stack:
            elem = stack.pop()
            print(elem.val)
            if root.right:
                root = elem.right

        else:
            return 

if __name__=="__main__":
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
    six.left = seven
    six.right = nine

    output = inorderTraversalx(Head)


