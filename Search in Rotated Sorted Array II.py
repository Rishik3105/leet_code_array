import array

def search(nums, target):
    if target in nums:
        return True
    else:
        return False
        
if __name__ == "__main__":
    nums = array.array('i', map(int, input("Enter your sequence: ").split()))
    target = int(input("Enter target: "))
    print(search(nums, target))
