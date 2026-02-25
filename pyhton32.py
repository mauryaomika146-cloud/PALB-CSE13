def combinationSum(candidates, target):
    result = []
    
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i]) 
            path.pop()
    
    backtrack(0, [], target)
    return result


candidates1 = [2,3,6,7]
target1 = 7

candidates2 = [2,3,5]
target2 = 8

candidates3 = [2]
target3 = 1

print(
    "Output:", combinationSum(candidates1, target1),
    "\nOutput:", combinationSum(candidates2, target2),
    "\nOutput:", combinationSum(candidates3, target3)
)