# Largest odd number in a string
def largest_odd_number_in_string(num: str) -> str:
    for i in range(len(num) - 1, -1, -1):
        if num[i] in '13579':
            return num[:i + 1]
    return ""

print(largest_odd_number_in_string("52"))
print(largest_odd_number_in_string("4206"))
print(largest_odd_number_in_string("35427"))
