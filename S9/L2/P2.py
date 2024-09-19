# Prefix to Infix Conversion using Stack
def prefixToInfix(prefix):
    stack = []
    operators = set(["+", "-", "*", "/", "^"])
    for ch in prefix[::-1]:
        if ch in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"({op1}{ch}{op2})")
        else:
            stack.append(ch)
    return stack.pop()

print(prefixToInfix("*+ab-cd"))
print(prefixToInfix("*+pq-mn"))
print(prefixToInfix("*-A/BC-/AKL"))
