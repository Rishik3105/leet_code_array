import array

def removeduplicates(nums):
    stop = len(nums)
    if stop == 0:
        return []
    start = 0
    count = 1
    result = [nums[0]]  
    for i in range(1, stop):
        temp = nums[i]
        if temp == nums[start]:
            count += 1
            if count <= 2:
                result.append(temp)
        else:
            count = 1
            result.append(temp)
        start += 1
    return result
  
if __name__ == "__main__":
    nums = array.array('i', map(int, input("Enter your sequence: ").split()))
    result = removeduplicates(nums)
    print("Output length:", len(result))
    print("Modified array:", result)
