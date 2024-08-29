# Reverse Stack using Recursion
def insertStack(stack, temp):
    if len(stack) == 0:
        stack.append(temp)
    else:
        val = stack.pop()
        insertStack(stack, temp)
        stack.append(val)

def reverseStack(stack):
    if len(stack) > 0:
        temp = stack.pop()
        reverseStack(stack)
        insertStack(stack, temp)

stack = [34, 3, 31, 98, 92, 23]
reverseStack(stack)
print(stack)
