from functools import cmp_to_key

def largestNumber(nums):
    nums = list(map(str, nums))
    def cmp(a, b):
        if a + b > b + a:
            return -1
        if a + b < b + a:
            return 1
        return 0
    nums.sort(key=cmp_to_key(cmp))
    res = ''.join(nums)
    return "0" if res[0] == "0" else res
if __name__ == "__main__":
    nums = [3,30,34,5,9]
    print(largestNumber(nums))
