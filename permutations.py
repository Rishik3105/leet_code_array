def permutations(nums):
    result = []
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for num in nums:
            if num not in path:
                path.append(num)
                backtrack(path)
                path.pop()
    backtrack([])
    return result

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print(permutations(nums))
