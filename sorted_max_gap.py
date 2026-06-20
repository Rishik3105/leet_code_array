class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2:
            return 0
        else:
            nums_sorted=sorted(nums)
            res=0
            for i in range(1,len(nums_sorted)):
                prev=nums_sorted[i-1]
                curr=nums_sorted[i]
                diff=curr-prev
                res=max(diff,res)
            return res
        
