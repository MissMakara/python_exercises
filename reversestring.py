# "Given an input string, reverse the string word by word."

def reverseStringElements(x):
    list_x = list(x)
    list_x.reverse()
    str_ = ""
    str_x = str_.join(list_x)
    print(str_x)

def reverseStringWords(x):
    lis_ = x.split()
    lis_.reverse()
    #str_ = ""
    print(" ".join(lis_))
    # print(' '.join(x.split()[::-1]))


reverseStringWords("Given an input string, reverse the string word by word.")