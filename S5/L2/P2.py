# Maximum Nesting Depth of Parantheses
def max_depth_parantheses(s):
    max_depth = 0
    current_depth = 0
    for i in s:
        if i == "(":
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif i == ")":
            current_depth -= 1
    return max_depth

print(max_depth_parantheses("(1+(2*3)+((8)/4))+1"))
print(max_depth_parantheses("(1)+((2))+(((3)))"))
print(max_depth_parantheses("1+(2*3)/(2-1)"))
