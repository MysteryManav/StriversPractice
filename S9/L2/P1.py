# Infix to Postfix Conversion using Stack
def infixToPostfix(infix):
    stack = []
    result = ""
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    for ch in infix:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()
        elif ch in precedence:
            while stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[ch]:
                result += stack.pop()
            stack.append(ch)
        else:
            result += ch
    while stack:
        result += stack.pop()

    return result

print(infixToPostfix("a+b*c-d/e"))
print(infixToPostfix("(p+q)*(m-n)"))
print(infixToPostfix("a+b*(c^d-e)^(f+g*h)-i"))
