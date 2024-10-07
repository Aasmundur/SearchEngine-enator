def jaccard(firstSet, secondSet):
    
    setsUnionized = firstSet.union(secondSet)
    print("The unionized set: ", setsUnionized)
    setsIntersected= firstSet.intersection(secondSet)
    print("\nLength of unionized set: ", len(setsUnionized), " Length of the intersected set:", len(setsIntersected), "\n")
    if (len(setsUnionized)==0):
        return 0
    return len(setsIntersected) / len(setsUnionized)