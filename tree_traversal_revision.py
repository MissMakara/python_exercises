class Node():
    def __init__(self, item):
        self.right = None
        self.left =None
        self.data = item

def inorder_recursion(root):
    #left>root>right
    if root:
        inorder_recursion(root.left)
        print(root.data)
        inorder_recursion(root.right)

def preorder_recursion(root):
    if root:
        print(root.data, end=" ")
        preorder_recursion(root.left)
        preorder_recursion(root.right)

def postorder_recursion(root):
    if root:
        postorder_recursion(root.left)
        postorder_recursion(root.right)
        print(root.data, end=" ")

def inorder_with_stack(root):
    #push the root to stack
    #make root.left to be root and push to stack
    #once all left is done, check is there is stack
    #pop and print
    #make root = popped.right and repeat the process above

    stack = []
    while True:
        if root:
            stack.append(root)
            root = root.left
            #print(stack)
        else:
            if stack:
                #print("in stack")
                x=stack.pop()
                print(x.data, end=" ")
                root = x.right 

            else:
                return

def preorder_with_stack(root):
    #if root push to stack
    #if root and if stack,
    #pop the stack and print the popped item
    #push the popped.right to stack
    #push the popped.left to stack
    #repeat
    #when nothing is in stack, return
    #if there is nothing in root return
    stack =[]
    if root:
        stack.append(root)
        while True:
            if stack:
                popped =stack.pop()
                print(popped.data, end=" ")
                
                if popped.right:
                    stack.append(popped.right)
                if popped.left:
                    stack.append(popped.left)
            else:
                return    
    else:
        return

def postorder_with_2_stacks(root):
    stack1=[]
    stack2 =[]
    if root:
        stack1.append(root)
        while True:    
            if stack1:
                popped = stack1.pop()
                stack2.append(popped)
                if popped.left:    
                    stack1.append(popped.left)
                if popped.right:
                    stack1.append(popped.right)
                
            elif stack2:
                x = stack2.pop()
                print(x.data, end=" ")

            else:
                return

if  __name__ == "__main__":
    # root = Node(1)
    # second = Node(2)
    # third = Node(3)
    # fourth = Node(4)
    # fifth = Node(5)
    # sixth = Node(6)
    # seventh = Node(7)

    # root.left = second
    # root.right = third
    # second.left = fourth
    # second.right = fifth
    # third.left = sixth
    # third.right = seventh
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    #print(root.left.data)
    postorder_with_2_stacks(root)

