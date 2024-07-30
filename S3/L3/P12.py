# Maximum product subarray in an array
def max_product_subarray(array):
    n = len(array)
    prod1 = array[0]
    prod2 = array[0]
    result = array[0]

    for i in range(1, n):
        temp = max(array[i], prod1 * array[i], prod2 * array[i])
        prod2 = min(array[i], prod1 * array[i], prod2 * array[i])
        prod1 = temp

        result = max(result, prod1)

    return result

a = [1, 2, -3, 0, -4, -5]
print("The maximum product subarray is:", max_product_subarray(a))
