# Check whether one string is rotation of another string
def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    if s == goal:
        return True
    for i in range(len(s)):
        if s[i:] == goal[:len(s) - i] and s[:i] == goal[len(s) - i:]:
            return True
    return False

print(rotateString("abcde", "cdeab"))
