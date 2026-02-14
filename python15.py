import math

# Function to merge two sorted arrays without extra space
def mergeArrays(a, b):
    n = len(a)
    m = len(b)
    
    # Initial gap
    gap = math.ceil((n + m) / 2)
    
    while gap > 0:
        i = 0
        j = gap
        
        while j < (n + m):
            
            # Case 1: Both pointers in array a
            if i < n and j < n:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
            
            # Case 2: i in a and j in b
            elif i < n and j >= n:
                if a[i] > b[j - n]:
                    a[i], b[j - n] = b[j - n], a[i]
            
            # Case 3: Both pointers in array b
            else:
                if b[i - n] > b[j - n]:
                    b[i - n], b[j - n] = b[j - n], b[i - n]
            
            i += 1
            j += 1
        
        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)


# Example 1
a = [2, 4, 7, 10]
b = [2, 3]
mergeArrays(a, b)
print("a =", a)
print("b =", b)

# Example 2
a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
mergeArrays(a, b)
print("a =", a)
print("b =", b)
