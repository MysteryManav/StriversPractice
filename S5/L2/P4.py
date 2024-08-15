# String to Integer (Atoi):
def myAtoi(s):
    neg = False
    first = True
    ans = 0
    for i in s:
        if i == " " and first:
            continue
        elif i == "-" and first:
            neg = True
            first = False
        elif i == "+" and first:
            neg = False
            first = False
        elif i.isdigit():
            first = False
            ans = ans*10 + int(i)
        else:
            break

    if neg:
        if ans.bit_length() >= 32:
            return -2**31
        return -ans
    else:
        if ans.bit_length() >= 32:
            return 2**31 - 1
    return ans

print(myAtoi("42"))
print(myAtoi("2147483648"))
print(myAtoi("  +0 123"))
print(myAtoi("-91283472332"))
print(myAtoi("0-1"))
print(myAtoi("  -0012a42"))
