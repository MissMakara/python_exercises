
class Node():
    def __init__(self,item):
        self.val = item
        self.right = None
        self.left =None
	# @param A : root node of tree
	# @return a list of integers
def inorderTraversal2(root):
    print("starting...")
    #root = A 
    stack = []
    outlist = []
    length = 0 

    if root is None:
        return
    
    while True:
        if root:
            print("append root")
            stack.append(root)
            root= root.left

        else:
            if stack:
                print("there is smn in the stack stack")
                x_value = stack.pop()
                outlist.append(x_value.val)
                root = x_value.right
            
            else:

                return outlist 

def inorderTraversal( A):
    curr = A
    ans = []
    stack = []
    
    while True:
        
        if curr:
            stack.append(curr)
            curr = curr.left
            
        else:
            if stack:
                temp = stack.pop()
                ans.append(temp.val)
                curr = temp.right
                    
            else:
                return ans

if __name__== "__main__":
    Head = Node(1)
    second = Node(2)
    third = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    nine = Node(9)

    Head.left = second
    second.left = four
    second.right = five
    Head.right = third
    third.right = six
    six.left = seven
    six.right = nine

    output = inorderTraversal2(Head)

    print (output)
