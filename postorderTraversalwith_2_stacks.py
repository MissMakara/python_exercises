class Node():
    def __init__(self,item):
        self.val = item
        self.right = None
        self.left = None

def postorderwith_2_Stacks(root):
    stack_1 = []
    stack_2 = []
    if root is None:
        return
    
 
    if root:
        stack_1.append(root)
        
        while stack_1:
            x = stack_1.pop()
            stack_2.append(x.val)
            if x.left:
                stack_1.append(x.left)
            if x.right:
                stack_1.append(x.right)

    while stack_2:
        print(stack_2.pop(),end=" ")
  

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

    output = postorderwith_2_Stacks(Head)