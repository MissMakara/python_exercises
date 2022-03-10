#search for the root
#recursively print the left subtree
#recursively print the right subtree
def search(list, x):
    if list is None:
        return None

    for value, index in enumerate (list):
        if  value == x:
            return index
        else:
            return False

def postorderWithPreandIn(preorder, inorder):
    root = pre[0]

    #search for the root
    index = search(inorder,root)
    



