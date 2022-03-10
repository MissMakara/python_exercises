class Node():
    def __init__(self, item):
        self.val = item
        self.right = None
        self.left = None

def levelorderTraversal(root):
    q = []
    cur = root
    if root is None:
        return

    while True:
        print(cur.val, end=" ")
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)

        if q:
            value_x = q.pop(0)
            cur = value_x

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
    six.left = seven
    six.right = nine

    output = levelorderTraversal(Head)

    print (output)
