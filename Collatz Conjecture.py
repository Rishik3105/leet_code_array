import array

def checking(n):
    count=0
    if n==1:
        return 1
    elif n==0:
        return 0
    while n>1:
        if n%2==0:
            n=n//2
        else:
            n=(3*n)+1
        count+=1
    return count
if __name__ == "__main__":

    nums = list(map(int, input("Enter numbers: ").split()))
    print(checking(nums[0]))
