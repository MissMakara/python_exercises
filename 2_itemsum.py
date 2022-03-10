#Given an array of integers and a value, determine 
# if there are any two integers in the array 
# whose sum is equal to the given value.

def determiner(list_x, value):
    if list_x is None:
        return

    for i in range(0, len(list_x)-1):
        for x in range(0, len(list_x)-1):
            if i ==x:
                pass

            if list_x[i]+list_x[x]== value:
                return [list_x[i], list_x[x]]
            
    
if __name__ == "__main__":
    output = determiner([3,4,2,5,6,2,5,1,2], 7)
    print(output) 