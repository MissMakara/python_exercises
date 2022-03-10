# "Given an unsorted integer array, 
# find the smallest missing positive integer...
# Your algorithm should run in O(n) time and uses constant extra space."

class Solution():
    def findSmallest(self,arr):
        p= 0
        arr.sort()
        for i in range(len(arr)-1):
            
            if (arr[i+1] - arr[i]) > 1:
                if arr[i]+1 > 0:
                    print(arr[i]+1)
                    return

            else:
                print(arr[i]+1)
                return
    def mergeSort(self,arr):
        if len(arr) > 1:
            #divide the array in two
            #call the merge sort function on both halves
            left = arr[:len(arr)//2]
            right = arr[len(arr)//2:]

            self.mergeSort(left)
            self.mergeSort(right)

            #merge step
            #compare the left most element of each half array 
            # and put the bigger one in the new array
            
            l= 0 #will point to the leftmost elem in the left array
            
            r = 0 #will point to the leftmost elem in the right array

            ind = 0 #tracks the index in the merged array

            #iterate through each array
            while l < len(left) and r <len(right):
                if left[l] <= right[r]:
                    final.append(left[l])
                    l +=1


                else:
                    final.append(right[r])
                    r +=1
    

            #if at all all elements of one array are bigger than the second array
            #so after the first while loop elements still remain in one of the arrays

            while l < len(left) and r == (len(right)-1):
                final.append(left[l])
                l+=1

            while r< len(right) and l ==(len(left)-1):
                final.append(right[r])
                r+=1

        print(final)
        return final
        




sol = Solution()
sol.findSmallest([-2,3,4,5,2])
sol.mergeSort([-2,3,4,5,2])