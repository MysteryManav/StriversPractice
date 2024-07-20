# Keep track of count of elements in an array
mp = {}
array = [10, 5, 10, 15, 10, 5]
for i in range(len(array)):
    if array[i] in mp:
        mp[array[i]] += 1
    else:
        mp[array[i]] = 1
for _ in mp:
    print(_, mp[_])
