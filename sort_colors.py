class Solution(object):
    def sortColors(self, nums):
        for k in range(1,len(nums)):
            curr=nums[k]
            j=k
            while j>0 and nums[j-1]>curr:
                nums[j]=nums[j-1]
                j-=1
            nums[j]=curr
        return nums
