def maxSubArray(self, A):
    #loop through the array
    #add together continous positives
    max_temp =0 
    max_final =0
    
    for i in A:
        max_temp = max_temp + i
        if (max_final < max_temp):
            max_final = max_temp

        elif max_temp < 0:
            max_temp = 0

    if max_final <= 0:
        return max(A)
    else:
        return max_final