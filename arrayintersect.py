class Solution:
    def intersect(self, nums1, nums2):
        if (1 <= len(nums1) and len(nums2) <= 1000):
            nums_merge=[]
          
            for i in nums1:
                print(i)
                for j in nums2:
                    #print(j)

                    if (i == j):
                        nums_merge.append(i)
                    
                        nums1.remove(i)
                        nums2.remove(j)

        print(nums_merge)


s= Solution()
s.intersect([1,2,2,1],[2,2])