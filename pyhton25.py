def allPalindromes(arr):
    for num in arr:
        s = str(num)
        if s != s[::-1]:
            return False
    return True


arr1 = [111, 222, 333, 444, 555]
arr2 = [121, 131, 20]

print(
    "Output:", allPalindromes(arr1),
    "\nOutput:", allPalindromes(arr2)
)