# Minimum Number of Jump

def minJumps(arr):
    n = len(arr)
    
    # If only one element
    if n <= 1:
        return 0
    
    if arr[0] == 0:
        return -1
    
    maxReach = arr[0]   
    steps = arr[0]     
    jumps = 1           
    
    for i in range(1, n):
        
        # If reached last index
        if i == n - 1:
            return jumps
        
        # Update maximum reach
        maxReach = max(maxReach, i + arr[i])
        
        steps -= 1
        
        # If no more steps left
        if steps == 0:
            jumps += 1
            
            if i >= maxReach:
                return -1
            
            steps = maxReach - i
    
    return -1


# Example 1
print(minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))

# Example 2
print(minJumps([1, 4, 3, 2, 6, 7]))

# Example 3
print(minJumps([0, 10, 20]))
