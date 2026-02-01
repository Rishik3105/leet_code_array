import array

def jump(nums):
    n = len(nums)
    temp = 0          
    min_jump = 0    
    jump = 0          
    for i in range(n - 1):
        temp = max(temp, i + nums[i])
        if i == jump:
            min_jump += 1
            jump = temp
    return min_jump


if __name__ == "__main__":
    nums = array.array('i', map(int, input("Enter your sequence: ").split()))
    print(jump(nums))
