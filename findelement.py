class Find():
    def findPivot(self,arr):
        p1 =0
        p2 =1
        i =0 
        
        while i < len(arr):
            if arr[p1] > arr[p2]:
                return arr[p1],p1
            else:
                i +=1
                p1 +=1
                p2 +=1



    def findElem(self,arr, elem):
        pivot, index = self.findPivot(arr)
        arr1 = arr[0:index+1]
        arr2 = arr[index+1:]
        print(arr1)
        print(arr2)

        for index, value in enumerate(arr1):
            print("value", value)
            if value == elem:
                return index
            
        for index, value in enumerate(arr2):
            if value == elem:
                return index+1 + len(arr1)-1
        else:
            return None



if __name__ == "__main__":
    f= Find()
    output = f.findElem([3, 4, 5, 1, 2], 8)
    print("index is",output)



            
