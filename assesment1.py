#convert
class Node():
    def __init__(self, data):
        self.data = data
        self.next =None

class LinkedList():
    def __init__(self):
        self.head =None

def solution(x):
    
    list_x = list(x)
    print(list_x)
    chars = ["*","?","!"]

    length = len(list_x)

    half_len =length/2
    
    left_index =0
    right_index=length-1

    while left_index < right_index:

        item1 =list_x[left_index]
        item2 =list_x[right_index]

        if item1 is not chars and item2 is not chars:
            list_x[left_index] =(item2)
            list_x[right_index] =(item1)
            left_index = left_index+1
            right_index = right_index-1
        
        elif item1 is chars:
            left_index = left_index+1

        elif item2 is chars:
            right_index = right_index -1


    stringx =" "
    print(stringx.join(list_x))    


if __name__ == "__main__":
    x="t?*up*vw"

    solution(x)




