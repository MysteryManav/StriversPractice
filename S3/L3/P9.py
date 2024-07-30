# Find the repeating and missing number
def repeating_and_missing_number(array):
    n = len(array)
    xr = 0
    for i in range(n):
        xr ^= array[i]
        xr ^= i+1
    set_bit = xr & ~(xr-1)
    x = 0
    y = 0
    for i in range(n):
        if array[i] & set_bit:
            x ^= array[i]
        else:
            y ^= array[i]
        if (i+1) & set_bit:
            x ^= i+1
        else:
            y ^= i+1
    print("Repeating number: ", y)
    print("Missing number: ", x)

array = [4, 3, 6, 2, 1, 1]
repeating_and_missing_number(array)
