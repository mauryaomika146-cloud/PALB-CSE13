# Reverse an array using Two Pointer Algorithm
# Input is already given in the code

def reverseArray(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


arr = [1, 4, 3, 2, 6, 5]

reverseArray(arr)

print("Reversed Array:", arr)





        
     