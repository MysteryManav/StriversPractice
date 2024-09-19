# Infix to Prefix
def infixToPrefix(infix):
    stack = []
    result = ""
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    for ch in infix[::-1]:
        if ch == ")":
            stack.append(ch)
        elif ch == "(":
            while stack and stack[-1] != ")":
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

    return result[::-1]

print(infixToPrefix("a+b*c-d/e"))
print(infixToPrefix("(p+q)*(m-n)"))
print(infixToPrefix("a+b"))
