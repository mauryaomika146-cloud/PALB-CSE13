def rotate (arr,k):
    n = len(arr)
    last = arr[n-1]
    #kth time
    k = k %n
    for _ in range(k): 
      last = arr[n-1]
    #clockwise
      for i in range(n-1,0,-1):
        arr[i] =arr[i-1]

      arr[0] = last
    return arr
arr =[1,2,3,4,5]
k = 2
print("Array:",arr)
print(f"output:{rotate(arr,k)}")