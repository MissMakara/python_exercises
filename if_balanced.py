class Node():
    def __init__(self,item):
        self.data = item
        self.right = None
        self.left = None
    
class Solution:
    def height(self, root):
        if root is None:
            return -1
            
        #for whichever subtree is longer, it returns that+1 count recursively
        return max(self.height(root.left),self.height(root.right))+1

    def isBalanced(self, root):
        
        if root is None:
            return True

        if root:
           # if root.left:
            lheight = self.height(root.left)
           # elif root.right:
            rheight = self.height(root.right)
            

            if abs(int(lheight - rheight))<= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)

    sol = Solution()
    output = sol.isBalanced(root)
    print("Outcome is", output)