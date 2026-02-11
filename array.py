import array

def jumpgame(nums):
    start,temp=0,0
    while len(nums)>temp:
        first=nums[start]
        temp=nums[first]
        if temp ==0:
            break
    if temp == len(nums):
        return True
    else:
        return False 
if __name__=="__main__":
    nums=array.array('i',map(int,input("Enter your sequence:").split()))
    print(jumpgame(nums))
