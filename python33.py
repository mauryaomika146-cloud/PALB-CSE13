def combinationSum2(candidates, target):
    candidates.sort()
    result = []
    
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            if candidates[i] > remaining:
                break
            
            path.append(candidates[i])
            backtrack(i + 1, path, remaining - candidates[i])
            path.pop()
    
    backtrack(0, [], target)
    return result


candidates1 = [10,1,2,7,6,1,5]
target1 = 8

candidates2 = [2,5,2,1,2]
target2 = 5

print(
    "Output:", combinationSum2(candidates1, target1),
    "\nOutput:", combinationSum2(candidates2, target2))
