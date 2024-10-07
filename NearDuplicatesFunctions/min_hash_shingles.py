def hash_64bit(shingle, func):
    return int.from_bytes(func(shingle.encode('utf-8')).digest()[:8], "little")

def min_hash_shingles(shingles, hash_funcs):
    min_hashed_shingles = set()
    
    for hash_func in hash_funcs:
        min_hash = None
        hashedShingleSet = set()
        for shingle in shingles:
            hashed_value = hash_64bit(shingle, hash_func)
            hashedShingleSet.add(hashed_value)
        min_hash = min(hashedShingleSet)
        min_hashed_shingles.add(min_hash)
    return min_hashed_shingles