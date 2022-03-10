class Node():
    def __init__(self, item):
        self.data = item
        self.right = None
        self.left = None

class Solution():
    def checkBst(self, root):
        if root is None:
            return True

        if root.right is not None and root.left is None and (int(root.right.data) > int(root.data)) and self.checkBst(root.right) is True and self.checkBst(root.left) is True:
            return True
        if root.left is not None and root.right is None and (int(root.left.data) < int(root.data)) and self.checkBst(root.right) is True and self.checkBst(root.left) is True:
            return True
        if root.right is not None and root.left is not None and (int(root.left.data) < int(root.data)) and (int(root.right.data) > int(root.data)) and self.checkBst(root.right) is True and self.checkBst(root.left) is True:
            return True
        else:
            return False


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
   # root.left.right = Node(3)
    root.right.right = Node(8)

    sol = Solution()
    output = sol.checkBst(root)
    print("Outcome is", output)