# Write a function to find the 2nd largest element in a binary search tree

class Node():
    def __init__(self, item):
        self.data= item
        self.right = None
        self.left = None


class Solution():
    def find_elem(self,root):
        if root is None:
            return
        
        stack = []

        while root:
            print("passed")
            stack.append(root)
            #check if right
            #check if left
            root = root.right
            #pop twice
        
        else:
            print(stack)
            if stack:
                x = stack.pop()
                # print("x is",x.data)
                if x.left:
                    # print(x.left.data)
                    root = x.left
                else:
                    #x is the highest item
                    #thus y will be the second highest item
                    y = stack.pop()
                    print("y is",y.data)
                    return y.data   

#if no right but no left
#so root=root.left



if __name__=="__main__":
    root = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh = Node(7)
    eighth =Node(8)
    ninth =Node(9)

    root.left = second
    root.right = sixth
    second.left = third
    second.right = fourth
    fourth.left = fifth
    sixth.left = seventh
    sixth.right = eighth
    eighth.left = ninth

sol = Solution()
output = sol.find_elem(root)
print(output)
