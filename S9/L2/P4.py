# Postfix to Prefix Conversion
def postfixToPrefix(postfix):
    stack = []
    operators = set(["+", "-", "*", "/", "^"])
    for ch in postfix:
        if ch in operators:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(f"{ch}{op1}{op2}")
        else:
            stack.append(ch)
    return stack.pop()

print(postfixToPrefix("abc*+de*f+g*+"))
print(postfixToPrefix("ABC/-AK/L-*"))
