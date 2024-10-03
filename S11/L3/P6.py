# Top K frequent elements
def kFrequentElements(arr, k):
    freq = {}
    for i in arr:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
    freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    return list(freq.keys())[:k]

print(kFrequentElements([1,1,1,2,2,3], 2))
print(kFrequentElements([1], 1))
print(kFrequentElements([3,0,1,0], 1))
