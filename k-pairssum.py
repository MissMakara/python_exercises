
def maxOperations(nums, k):
    count = 0
    #sort the list in ascending order
    nums.sort()
    #start iterating through the list
    start, end = 0, len(nums)-1

    while(start<end):
        #if the total of the first and last is greater than k
        #move on step from the end
        if nums[start] + nums[end] > k:
            end = end-1

        #if the total of the numbers is less than k
        #move one step from the start
        elif (nums[start] + nums[end]< k):
            start=start+1

        
        else:
            start+=1
            end-=1
            count+=1
    return count



if __name__=="__main__":
    output = maxOperations([4,1,2,3],5)
    print("count is",output)