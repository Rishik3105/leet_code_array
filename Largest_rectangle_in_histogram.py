def largestRectangleArea(heights):
    stack = []  
    max_area = 0
    heights.append(0)
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            max_area = max(max_area, h * width)
        stack.append(i)
    return max_area
if __name__ == "__main__":
    heights = list(map(int, input("Enter heights: ").split()))
    print(largestRectangleArea(heights))
