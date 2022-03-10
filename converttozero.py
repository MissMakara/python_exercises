# Given a two-dimensional array, 
# if any element within is zero, 
# make its whole row and column zero.

def convert_toZero(list_d):
    for r in list_d:
        # print(r)
        for c in r:
            if c == 0:
                print(r)
                return
                for i in r:
                    i=0
                print(r)
                return


                    
                
 
   # for r in range(0, len(list_d[0])-1):
    #     for c in range(0, len(list_d[1])-1):
    #         if list_d[r][c] == 0:
    #             list_d[] =0
    #             list_d[c]


convert_toZero([[7,6,0,3,4,2,3],[3,2,4,1,5,6,3]])