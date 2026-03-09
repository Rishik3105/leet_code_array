def searchmatrix(matrix, target):
    for row in matrix:
        if row[0] <= target <= row[-1]:
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = (left + right) // 2

                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
    return False
if __name__ == "__main__":
    rows = int(input("Enter rows: "))
    cols = int(input("Enter cols: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        matrix.append(row)
    target = int(input("Enter your target: "))
    print(searchmatrix(matrix, target))
