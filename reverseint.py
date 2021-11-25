#to reverse an integer and have it retain whether it's positive or negative
def reverse(x):
    if -2**31 <= x <= 2**31 - 1:
        str_x = str(x)
        arr = list(str_x)
        arr2 = list()
        separator =""

        if arr[0]=='-':
            temp = arr.pop(0)
            for i, element in enumerate (reversed(arr)):
                arr2.append(element)
                


            final = (str(separator.join(arr2)))
            final = int(temp+final)
            
            if (-2**31< final <2**31-1):
                return final
            else:
                return 0
        else:
            for i, element in enumerate (reversed(arr)):
                arr2.append(element)
            final = (str(separator.join(arr2)))
            final = int(final)
            
            if (-2**31< final <2**31-1):
                return final
            else:
                return 0
            



output = reverse(-321)
print(output)