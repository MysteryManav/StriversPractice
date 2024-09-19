# Trapping Rainwater
def trappingRainwater(height):
    n =len(height)
    left = 0
    right = n - 1
    res = 0
    maxLeft = 0
    maxRight = 0
    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= maxLeft:
                maxLeft = height[left]
            else:
                res += maxLeft - height[left]
            left += 1
        else:
            if height[right] >= maxRight:
                maxRight = height[right]
            else:
                res += maxRight - height[right]
            right -= 1
    return res

print(trappingRainwater([0,1,0,2,1,0,1,3,2,1,2,1]))
