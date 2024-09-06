# Letter Combinations of a Phone Number
def letterCombinations(digits):
    if digits == "":
        return []
    phone = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    def backTrack(index, path):
        if index == len(digits):
            ans.append(path)
            return
        for letter in phone[digits[index]]:
            backTrack(index+1, path+letter)
    ans = []
    backTrack(0, "")
    return ans

digits = "23"
print(letterCombinations(digits))
