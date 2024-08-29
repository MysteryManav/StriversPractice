# Sort a stack using recursion
def insertStack(stack, temp):
    if len(stack) == 0 or stack[-1] <= temp:
        stack.append(temp)
    else:
        val = stack.pop()
        insertStack(stack, temp)
        stack.append(val)

def sortStack(stack):
    if len(stack) > 0:
        temp = stack.pop()
        sortStack(stack)
        insertStack(stack, temp)

stack = [34, 3, 31, 98, 92, 23]
sortStack(stack)
print(stack[::-1])
