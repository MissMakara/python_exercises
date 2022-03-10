#create a huffman tree from given character frequencies
#
import operator
class Node():
    def __init__(self, item):
        self.data = item
        self.right = None
        self.left =None

class Huffman():
    def __init__(self, x):
        # {"a":10,"e":15,"i":12,"o":3,"u":4,"s":13,"t": 1}
        self.dict_x = x
        self.temp_str =""
        
    def createList(self):

        vals = self.dict_x.values()
        vals_list =list(vals)
    
        return vals_list
        #create the tree
        #[1, 3,  4, 10, 12, 13, 15]

    def createNodesFromList(self):
        #return a list of Nodes
        arr = self.createList()
        print(arr)
        arr.sort()
        print("sorted",arr)
        nodelist =[]
        for i in arr:
            nodelist.append(Node(i))
        
        
        return nodelist
    
        
    def createTree(self, nodelis):
        print("creating the tree ..")

        #take a list of nodes and recursively create a tree
        if len(nodelis) > 1:

            print(nodelis[0].data, nodelis[1].data)
            node_s = nodelis[0].data + nodelis[1].data
            
            #mke node 1 and 2 children to sum
            x = nodelis.pop(0)
            y = nodelis.pop(0)
            nodesum = Node(node_s)
            nodesum.left = x
            nodesum.right = y

            nodelis.insert(0,nodesum)


            sorted_lis = self.sortList(nodelis)
            self.createTree(sorted_lis)
        else:
            print("tree completed ..")
            print("nodelis is", nodelis[0].left.data)
            self.createCodes(nodelis)
        
    def sortList(self, lis):
        print("sorting...")
        count = 0
        p1 = 0
        p2 = 1
        while True:
            if count < (len(lis)-1):
                print("initial:",lis[p1].data,lis[p2].data)
                if lis[p1].data > lis[p2].data:
                    #swap them
                    temp = lis[p1].data
                    lis[p1].data = lis[p2].data
                    lis[p2].data = temp
               
                count += 1
                p1 +=1
                p2 +=1
            else:
                break


        self.printTree(lis[0])
        return lis

    def printTree(self, tree):
        #tree = lis[0]
       if tree:
            self.printTree(tree.left)
            print(tree.data, end=" ")
            self.printTree(tree.right)

    def searchNode(self, tree, elem,temp_str):
        #print(temp_str)
        temp_str = " "

        if tree is None:
            return " "
        if tree.data == elem:
            # print("temp string is",temp_str)
            return " "
        else:
            if tree.left:
                # temp_str = temp_str+"0"
                temp_str ="0"
                return self.searchNode(tree.left, elem,temp_str)

            if tree.right:
                temp_str="1"
                return self.searchNode(tree.right, elem, temp_str)
                
        return temp_str         

    def createCodes(self, lis):
        #print(new_dict)
        # create a new dict
        #get the old public dict
        #iterate through the dict as you search for the values
        #as you search for the value down the tree, append a 0 to the temp string as you go left
        #append/concat a 1 to the temp string as you go left
        #once you get the value in the tree, return the string and create a new dict entry with the key and string values
        
        new_dict ={}
       
        tree = lis[0]
       
        print("Produced tree..")
        self.printTree(tree)

        for key, value in self.dict_x.items():
            self.temp_str =""
            print("")
            print("search for value", value)
            self.searchNode(tree, value, self.temp_str)
            
            print("returned value",self.temp_str)
            print("")
            new_dict[key] = self.temp_str

        print(new_dict)
        return new_dict
    
    
     

if __name__ == "__main__":
    h = Huffman({"a":10,"e":15,"i":12,"o":3,"u":4,"s":13,"t": 1})

    nodeslis = h.createNodesFromList()
    #print(nodeslis)
   
    h.createTree(nodeslis)
    #print("tree output is",tree)
    #h.createCodes(tree)


   
