#given a list
# find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum."

def maxSubArray(nums):
    if nums is None:
        return 0
    p = 0
    prev = -1
    count = 1
    sub_array = []
    sum_ = 0
    max_ = nums[0]
    
    while count < len(nums):
        sum_ += nums[p]
        
        if max_ <= sum_:
            max_= sum_
            if prev != (p-1):
                print ("skipped 1")
                sub_array = []
                
            sub_array.append(nums[p])
            print(sub_array)
            prev = p

        
            #sub_array = []
        
        count +=1
        p +=1
        print("p is",p)
        #prev +=1
        print("prev is",prev)

    print (sub_array)
#how do you handle the one negative number between the positives
#how do you handle if the array consists of only negative numbers?
s
maxSubArray([-2,1,-3,4,-1,2,1,-5,4])