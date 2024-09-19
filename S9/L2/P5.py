# Postfix to Infix
def postfixToInfix(postfix):
    stack = []
    operators = set(["+", "-", "*", "/", "^"])
    for ch in postfix:
        if ch in operators:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(f"({op1}{ch}{op2})")
        else:
            stack.append(ch)
    return stack.pop()

print(postfixToInfix("abc*+de*f+g*+"))
print(postfixToInfix("ab*c+"))
