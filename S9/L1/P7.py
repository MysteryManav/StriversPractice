# Check Balanced Paranthesis
def checkBalancedParanthesis(s):
    stack = []
    for i in s:
        if i in ["(", "{", "["]:
            stack.append(i)
        else:
            if not stack:
                return False
            elif i == ")" and stack[-1] != "(" or i == "}" and stack[-1] != "{" or i == "]" and stack[-1] != "[":
                return False
            else:
                stack.pop()
    return not stack

print(checkBalancedParanthesis("()"))
print(checkBalancedParanthesis("()[]{}"))
print(checkBalancedParanthesis("(]"))
print(checkBalancedParanthesis("([)]"))
