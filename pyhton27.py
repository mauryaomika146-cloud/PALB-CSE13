def spirallyTraverse(matrix, r, c):
    
    result = []
    
    top = 0
    bottom = r - 1
    left = 0
    right = c - 1
    
    while top <= bottom and left <= right:
        
        # Traverse top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Traverse bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        # Traverse left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result


# Example 1
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

print("Output:", spirallyTraverse(mat, 4, 4))


# Example 2
mat2 = [[1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18]]

print("Output:", spirallyTraverse(mat2, 3, 6))


# Example 3
mat3 = [[32, 44, 27, 23],
        [54, 28, 50, 62]]

print("Output:", spirallyTraverse(mat3, 2, 4))