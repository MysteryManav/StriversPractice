# Palindrome Partitioning
def is_palindrome(s):
    return s == s[::-1]

def partition(s):
    def backTrack(start, path):
        if start == len(s):
            ans.append(path)
            return
        for i in range(start, len(s)):
            if is_palindrome(s[start:i+1]):
                backTrack(i+1, path+[s[start:i+1]])
    ans = []
    backTrack(0, [])
    return ans

s = "aabb"
print(partition(s))
