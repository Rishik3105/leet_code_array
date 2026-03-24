import array 

def search(nums,target):
    if target not in nums:
        return True
    else:
        return False
 
if __name__=="__main__":
    nums=array.array('i',map(int,input("Enter your sequence:").split()))
    target=input("target:")
    print(search(nums,target))
