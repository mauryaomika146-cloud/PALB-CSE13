# Function to find minimum and maximum in an array
def findMinMax(arr):
    minimum = arr[0]
    maximum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
        if arr[i] > maximum:
            maximum = arr[i]

    return [minimum, maximum]


arr = [1, 4, 3, 5, 8, 6]

result = findMinMax(arr)

print("Minimum and Maximum:", result)

