#use hash table/ dictionary to solve the two sum problem
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target. 
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.


#create a hash table
#have a value value difference mapping in the dict
#if yo visit a value add it to the dict as a key with the index as the value
#for each number visited, check the difference required to the target, 
#check if it is in the dict, if so return the index
#else, add the number to the dict and proceed to the next element on the list

class Solution():
    def findSum(self, arr, target):
        if arr is None:
            return -1

        new_dict = dict()

        for index, value in enumerate(arr):
            diff = target - value

            if diff in new_dict.keys():
                print (new_dict[diff], index)
                return

            else:
                if index not in new_dict.values():
                    new_dict[value] = index


sol = Solution()
sol.findSum([2,3,1,-1,6,4], 10)






