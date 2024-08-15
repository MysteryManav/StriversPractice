# Count number of substrings
def number_of_substrings(s, k):
    n = len(s)
    distinct = 0
    for i in range(n):
        dist_count = 0
        count = [0]*26
        for j in range(i, n):
            if count[ord(s[j]) - ord('a')] == 0:
                dist_count += 1
            count[ord(s[j]) - ord('a')] += 1
            if dist_count == k:
                distinct += 1
            if dist_count > k:
                break
    return distinct

print(number_of_substrings("abc", 2))
print(number_of_substrings("abaaca", 1))
