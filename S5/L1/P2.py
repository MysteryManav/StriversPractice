# Reverse words in a given string
def reverse_words_string(s: str) -> str:
    s: str = s.strip()
    left: int = 0
    right: int = len(s) - 1
    temp: str = ""
    ans: str = ""
    while left <= right:
        if s[left] != " ":
            temp += s[left]
        elif s[left] == " ":
            if ans != "" and temp != "":
                ans = temp + " " + ans
                temp = ""
            elif ans == "":
                ans = temp
                temp = ""
            else:
                temp = ""
        left += 1
    if temp != "":
        if ans == "":
            ans = temp
        else:
            ans = temp + " " + ans
    return ans

print(reverse_words_string("Let's take LeetCode contest"))
