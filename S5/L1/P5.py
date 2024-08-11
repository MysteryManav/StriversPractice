# Isomorphic Strings
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    index_s = [0] * 256
    index_t = [0] * 256
    for i in range(len(s)):
        if index_s[ord(s[i])] != index_t[ord(t[i])]:
            return False
        index_s[ord(s[i])] = i + 1
        index_t[ord(t[i])] = i + 1
    return True

print(is_isomorphic("egg", "add"))
print(is_isomorphic("foo", "bar"))
print(is_isomorphic("paper", "title"))
