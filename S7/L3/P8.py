# Add Operators
def addOperators(num, target):
    n = len(num)
    results = []

    def dfs(index, prev_operand, current_operand, value, expression):
        if index == n:
            if value == target and current_operand == 0:
                results.append(''.join(expression))
            return
        
        current_operand = current_operand * 10 + int(num[index])
        str_output = str(current_operand)
        if current_operand > 0:
            dfs(index + 1, prev_operand, current_operand, value, expression)
        
        if expression:
            expression.append('+')
            expression.append(str_output)
            dfs(index + 1, current_operand, 0, value + current_operand, expression)
            expression.pop()
            expression.pop()

            expression.append('-')
            expression.append(str_output)
            dfs(index + 1, -current_operand, 0, value - current_operand, expression)
            expression.pop()
            expression.pop()

            expression.append('*')
            expression.append(str_output)
            dfs(index + 1, prev_operand * current_operand, 0, value - prev_operand + (prev_operand * current_operand), expression)
            expression.pop()
            expression.pop()
        else:
            expression.append(str_output)
            dfs(index + 1, current_operand, 0, current_operand, expression)
            expression.pop()
        
    dfs(0, 0, 0, 0, [])
    return results

num = "123"
target = 6
print(addOperators(num, target))

target = 24
num = "232"
print(addOperators(num, target))

target = 36
num = "123"
print(addOperators(num, target))
