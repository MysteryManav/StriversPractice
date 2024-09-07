# Check if a number is even or not
def checkEven(num):
    if num & 1:
        return False
    return True

print(checkEven(5))
print(checkEven(6))
print(checkEven(7))
print(checkEven(8))
