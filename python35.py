def groupAnagrams(strs):
    anagrams = {}
    
    for word in strs:
        key = ''.join(sorted(word))
        
        if key not in anagrams:
            anagrams[key] = []
        
        anagrams[key].append(word)
    
    return list(anagrams.values())


strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]

print(
    "Output:", groupAnagrams(strs1),
    "\nOutput:", groupAnagrams(strs2),
    "\n Output:", groupAnagrams(strs3))
