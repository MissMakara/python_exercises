def reverseWords(words):
    q = words.split( )
    out =[]

    for i in range((len(q)-1),-1,-1):
        out.append(q[i])
    
    outstring = ' '.join(map(str, out))
    return outstring


if __name__=="__main__":
    output = reverseWords("come here Alexa")
    print(output)

            # for index, value in enumerate (nums):
           
            
            # for i in range(index+1, len(nums)):
            #     sum_x = value+nums[i]
            #     if (sum_x == target):
            #         return [index, i]
                