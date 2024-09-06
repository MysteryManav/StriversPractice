# Word Break
def wordBreak(s, wordDict, start):
    if start == len(s):
        return True
    
    for end in range(start + 1, len(s) + 1):
        if s[start:end] in wordDict and wordBreak(s, wordDict, end):
            return True
    return False

s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict, 0))
