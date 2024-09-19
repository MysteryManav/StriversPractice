# Implement Least Frequently Used Cache
def getLFUCache(lfu_cache, key):
    if key in lfu_cache:
        lfu_cache[key][1] += 1
        return lfu_cache[key][0]
    return -1

def putLFUCache(lfu_cache, key, value):
    if key in lfu_cache:
        lfu_cache[key] = [value, lfu_cache[key][1] + 1]
    elif len(lfu_cache) >= capacity:
        min_freq = float("inf")
        min_key = None
        for k, v in lfu_cache.items():
            if v[1] < min_freq:
                min_freq = v[1]
                min_key = k
        lfu_cache.pop(min_key)
        lfu_cache[key] = [value, 0]
    else:
        lfu_cache[key] = [value, 0]
    return lfu_cache

lfu_cache = {}
capacity = 2
lfu_cache = putLFUCache(lfu_cache, 1, 1)
lfu_cache = putLFUCache(lfu_cache, 2, 2)
print(lfu_cache)
print(getLFUCache(lfu_cache, 1))
lfu_cache = putLFUCache(lfu_cache, 3, 3)
print(lfu_cache)
print(getLFUCache(lfu_cache, 2))
lfu_cache = putLFUCache(lfu_cache, 4, 4)
print(lfu_cache)
print(getLFUCache(lfu_cache, 1))
print(getLFUCache(lfu_cache, 3))
print(getLFUCache(lfu_cache, 4))
print(getLFUCache(lfu_cache, 2))
