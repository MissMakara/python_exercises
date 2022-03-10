class Node():
    def __init__(self, item):
        self.val = item
        self.right = None
        self.left = None

def peek(stack):
    if len(stack)>0:
        return stack[-1]
    
    return None

def postorderwith_1_Stack(root):
    stack = []
    
    while True:
        if root is not None:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        
        else:
            if stack:
                popped = stack.pop()
                if popped.right == peek(stack):
                    y = peek(stack)
                    x = stack.pop()
                    stack.append(popped)
                    root = y
                else:
                    print(popped.val,end=" ")
                    root = None
            else:
                return

if __name__== "__main__":
    Head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth =Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh = Node(7)

    Head.right = third
    Head.left = second
    second.right = fifth
    second.left = fourth
    third.right =seventh
    third.left = sixth

    
    
    
    # Head = Node(400)
    # second = Node(200)
    # third = Node(100)
    # four = Node(120)
    # five = Node(160)
    # six = Node(320)
    # seven = Node(780)
    # nine = Node(220)
    # ten = Node(300)
    # eleven =Node(560)
    # twelve = Node(720)

    # Head.left = second
    # second.left = four
    # second.right = five
    # Head.right = third
    # third.right = ten
    # third.left = nine
    # four.left = six
    # four.right= seven
    # nine.right = eleven
    # eleven.left = twelve
   

    output = postorderwith_1_Stack(Head)
            



