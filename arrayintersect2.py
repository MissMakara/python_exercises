from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        if (1 <= len(nums1) and len(nums2) <= 1000):
            x = Counter(nums1)
            y= Counter(nums2)

            x&=y
            out = list(x.elements())
            return out
            
s = Solution()
interc = s.intersect([1,2,2,1],[2,2])
print(interc)