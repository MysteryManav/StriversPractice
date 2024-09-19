# Largest rectangle in histogram
def largestRectangleHistogram(heights):
    max_area = 0
    stack = []
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            element = stack.pop()
            next_smallest = i
            prev_smallest = stack[-1] if stack else -1
            width = next_smallest - prev_smallest - 1
            max_area = max(max_area, width * heights[element])
        stack.append(i)
    while stack:
        element = stack.pop()
        next_smallest = len(heights)
        prev_smallest = stack[-1] if stack else -1
        width = next_smallest - prev_smallest - 1
        max_area = max(max_area, width * heights[element])
    return max_area

print(largestRectangleHistogram([2, 1, 5, 6, 2, 3]))
print(largestRectangleHistogram([2, 4]))
print(largestRectangleHistogram([2, 1, 2]))
