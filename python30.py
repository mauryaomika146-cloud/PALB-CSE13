def rowWithMax1s(arr):
    n = len(arr)
    m = len(arr[0])

    max_row_index = -1
    j = m - 1   

    for i in range(n):
        while j >= 0 and arr[i][j] == 1:
            j -= 1
            max_row_index = i

    return max_row_index

arr1 = [
    [0,1,1,1],
    [0,0,1,1],
    [1,1,1,1],
    [0,0,0,0]]
print("Output:", rowWithMax1s(arr1))

arr2 = [
    [0,0],
    [1,1]]
print("Output:", rowWithMax1s(arr2))

arr3 = [
    [0,0],
    [0,0]]
print("Output:", rowWithMax1s(arr3))