import hashlib
from NearDuplicatesFunctions.k_shingle import k_shingle
from NearDuplicatesFunctions.jaccard import jaccard
from NearDuplicatesFunctions.min_hash_shingles import min_hash_shingles


def NearDuplicates(firstString, secondString):
    firstShingleSet = k_shingle(firstString, 3)
    secondShingleSet = k_shingle(secondString, 3)

    hash_funcs = [hashlib.sha256, hashlib.sha1, hashlib.sha512, hashlib.sha384, hashlib.sha224, hashlib.blake2b, hashlib.md5]
    firstHashedSet = min_hash_shingles(firstShingleSet, hash_funcs)
    secondHashedSet = min_hash_shingles(secondShingleSet, hash_funcs)
    print(firstHashedSet, secondHashedSet)
    jaccardScore = jaccard(firstHashedSet, secondHashedSet)
    return jaccardScore

