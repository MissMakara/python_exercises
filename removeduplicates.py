class Solution():
    def removeDuplicates(x):
        list_x = list(x)
        last = len(list_x)-1
        first = 0

        while first!=last:
            #0 
            for index, value in enumerate(list_x):
                if index == first:
                    pass
                else:
                    if list_x[first] == value:
                        list_x.pop(first)
                        #list_x.pop(index)
                        last = last-1
            first = first+1
        str =""
        return str.join(list_x)


if __name__ =="__main__":
    # option 2
    str = "carpenter"
    set_x =set(list(str))
    str_2 =""
    print(str_2.join(set_x))
    #output = Solution.removeDuplicates("carpenter")
    #print(output)