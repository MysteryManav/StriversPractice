# Prefix to Postfix Conversion
def prefixToPostfix(prefix):
    stack = []
    operators = set(["+", "-", "*", "/", "^"])
    for ch in prefix[::-1]:
        if ch in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"{op1}{op2}{ch}")
        else:
            stack.append(ch)
    return stack.pop()

print(prefixToPostfix("*+ab-cd"))
print(prefixToPostfix("*+pq-mn"))
print(prefixToPostfix("*-A/BC-/AKL"))
