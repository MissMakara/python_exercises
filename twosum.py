def twoSum(nums, target):
   for index1, value1 in enumerate (nums):
            for index2, value2 in enumerate (nums):
                if index1!=index2:

                    if value1 + value2 == target:
                  
                        return [index1, index2]

if __name__=="__main__":
    output = twoSum([2,3,3,5,5,5],6)
    print(output)

                