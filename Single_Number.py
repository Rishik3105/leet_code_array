import array

def singlenumber(nums):
    result = 0
    for num in nums:
        result ^= num        
    return result
if __name__=="__main__":
    nums=array.array('i',map(int,input("Enter your sequence:").split()))
    print(singlenumber(nums))
