# Sort Characters by Frequency
def sort_char_by_frequency(array):
    freq = {}
    for i in array:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    result = ""
    for i in freq:
        result += i[0]*i[1]
    return result

print(sort_char_by_frequency("tree"))
print(sort_char_by_frequency("cccaaa"))
print(sort_char_by_frequency("Aabb"))
