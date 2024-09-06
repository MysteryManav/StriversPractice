# Generate Parenthesis
def parenthesisCount(n, left, right, string):
    if len(string) == n*2:
        result.append(string)
        return
    
    if left < n:
        parenthesisCount(n, left+1, right, string=string+'(')
    if right < left:
        parenthesisCount(n, left, right+1, string+')')

result = []
parenthesisCount(3, 0, 0, '')
print(result)
