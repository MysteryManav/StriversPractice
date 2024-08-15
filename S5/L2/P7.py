# Sum of beauty of all substrings
def beautySum(s: str) -> int:
        ans = 0
        for i in range(len(s)):
            freq = [0]*26
            for j in range(i, len(s)):
                freq[ord(s[j])-97] += 1
                ans += max(freq) - min(x for x in freq if x)
        return ans

print(beautySum("aabcb"))
print(beautySum("aabcbaa"))
