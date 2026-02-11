def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        current = intervals[i]
        last = merged[-1]

        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged
if __name__ == "__main__":
    n = int(input("Enter number of intervals: "))
    intervals = []

    for i in range(n):
        start, end = map(int, input(f"Enter interval {i+1} (start end): ").split())
        intervals.append([start, end])

    result = merge_intervals(intervals)

    print("Merged Intervals:")
    for interval in result:
        print(interval)
