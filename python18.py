# Check if b is subset of a

def isSubset(a, b):
    freq = {}
    
    # Store frequency of elements in a[]
    for num in a:
        freq[num] = freq.get(num, 0) + 1
    
    # Check elements of b[]
    for num in b:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1
    
    return True


# Example 1
print(isSubset(
    [11, 7, 1, 13, 21, 3, 7, 3],
    [11, 3, 7, 1, 7]
))

# Example 2
print(isSubset(
    [1, 2, 3, 4, 4, 5, 6],
    [1, 2, 4]
))

# Example 3
print(isSubset(
    [10, 5, 2, 23, 19],
    [19, 5, 3]
))
