# Remove Outermost Paranthesis
def removeOuterParentheses(s: str) -> str:
    stack: list[str] = []
    result: str = ""
    for i in s:
        if i == "(":
            if stack:
                result += i
            stack.append(i)
        else:
            stack.pop()
            if stack:
                result += i
    return result

print(removeOuterParentheses("(()())(())"))
