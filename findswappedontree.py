# Two nodes of a BST are swapped, correct the BST

class Node():
    def __init__(self,  item):
        self.left = None
        self.right = None
        self.data = item



class Solution():
    def __init__(self):
        self.list_x = []

    def findSwapped(self,root):
        list_y =self.inorderTraversal(root)
        p1 =0
        p2 =1
        count =0
        while count < len(list_y):
            if  list_y[p1] > list_y[p2]:
                temp1 = p1
                count +=1
                p1 +=1
                p2 +=1
                break

            else:
                count +=1
                p1 +=1
                p2 +=1

        while count < len(list_y):   
            if list_y[p1] > list_y[p2]:
                temp2 = p2

                count +=1
                p1 +=1
                p2 +=1
                break

            else:
                count +=1
                p1 +=1
                p2 +=1

        print("temp 1", temp1)
        print("temp 2", temp2)
        temp3 = list_y[temp1]
        list_y[temp1] = list_y[temp2]
        list_y[temp2] = temp3
        
        return list_y
    def createTree(self,arr):
        if arr is None:
            return None

        print(arr)
        #find the mid point 
        x = len(arr)//2
        root = Node(arr[x])
        print(arr[0:x])
        print(arr[x:])
        root.left = self.createTree(arr[0:x])
        root.right = self.createTree(arr[x:])

        #make the mid point the root
        #divide the arr in half
        #recursively call the function on the halves
        return root

    def inorderTraversal(self,root):
        if root is None:
            return None
    
        if root:
           self.inorderTraversal(root.left)
           self.list_x.append(root.data)
           self.inorderTraversal(root.right)
        return self.list_x

if __name__=="__main__":
    root = Node(6)
    root.left = Node(10)
    root.right = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(7)
    root.right.right = Node(12)

    sol =Solution()
    output = sol.createTree([1, 2, 3, 6, 7, 10, 12])
    #print(output)
