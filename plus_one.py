import array
def plusone(nums):
    nums=int("".join(map(str,nums)))
    nums+=1
    nums=list(map(int,str(nums)))
    return nums
if __name__=="__main__":
    nums=array.array('i',map(int,input("Enter your array:").split()))
    print(plusone(nums))
