# Implement Least Recently Used Cache
def getLRUCache(lru_cache, key):
    if key in lru_cache:
        lru_cache[key] = lru_cache.pop(key)
        return lru_cache[key]
    return -1

def putLRUCache(lru_cache, key, value):
    if len(lru_cache) >= capacity:
        lru_cache.pop(next(iter(lru_cache)))
    elif key in lru_cache:
        lru_cache.pop(key)
    lru_cache[key] = value
    return lru_cache

lru_cache = {}
capacity = 2
lru_cache = putLRUCache(lru_cache, 1, 1)
lru_cache = putLRUCache(lru_cache, 2, 2)
print(lru_cache)
print(getLRUCache(lru_cache, 1))
lru_cache = putLRUCache(lru_cache, 3, 3)
print(lru_cache)
print(getLRUCache(lru_cache, 2))
lru_cache = putLRUCache(lru_cache, 4, 4)
print(lru_cache)
print(getLRUCache(lru_cache, 1))
print(getLRUCache(lru_cache, 3))
print(getLRUCache(lru_cache, 4))
print(getLRUCache(lru_cache, 2))
