def firstMissingPositive(nums):
    nums.sort()
    if 1<=len(nums) <=5*10**5:
        
        for i in range (0,len(nums)-1):
            if -231 <= nums[i] <= 231 - 1:
                #should start with a one
                #if all are following each other, should get the end +1
                if nums[i] > 0:
                    if nums[i+1]-nums[i] >1:
                        return nums[i]+1
                    

output =firstMissingPositive([7,8,9,11,12])
print(output)