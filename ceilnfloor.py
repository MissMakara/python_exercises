#find the ceil and floor of the given element
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution():

    def findCeilnFloor(self, root, elem):
        if root is None:
            return -1,-1
        
        while root:
            if root.data == elem:

                print(root.data, root.data)
                
                return root.data, root.data
         
        
            if elem > root.data:
                if root.right is None:
                    return root.data, -1
                
                elif root.right.data > elem:
                    return root.right.data, root.data
                
                else:
                    self.findCeilnFloor(root.right, elem)
                
            if elem < root.data:
                if root.left is None:
                    return root.data, -1

                elif root.left.data < elem:
                    return root.data, root.left.data

                else:
                    self.findCeilnFloor(root.left, elem)


if __name__=="__main__":
    root = Node(8) 
    root.left = Node(4)
    root.right = Node(12)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.right.left = Node(10)
    root.right.right = Node(14)

    sol =Solution()
    ceil, floor = sol.findCeilnFloor(root,1)
    #infinite loop with leaf nodes
    #won't return for an element not in the tree
    #yet i have handled it in the code
    print("ceil:", ceil, "floor", floor)

