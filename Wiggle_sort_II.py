class Solution(object):
    def wiggleSort(self, nums):
        res = []
        arr = sorted(nums)
        x = len(arr)
        mid = (x + 1) // 2
        i = mid - 1
        j = x - 1
        while i >= 0 or j >= mid:
            if i >= 0:
                res.append(arr[i])
                i -= 1
            if j >= mid:
                res.append(arr[j])
                j -= 1
        nums[:] = res
