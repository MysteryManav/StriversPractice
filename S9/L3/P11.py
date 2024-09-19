# Maximal Rectangles
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

def maximalRectangles(matrix):
    if not matrix:
        return 0
    n = len(matrix[0])
    heights = [0] * n
    max_area = 0
    for row in matrix:
        for i in range(n):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0
        max_area = max(max_area, largestRectangleHistogram(heights))

    return max_area

print(maximalRectangles([
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
]))    
