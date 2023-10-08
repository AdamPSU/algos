#49. Group Anagrams 


def group_anagrams(strs): 
    groupAnagrams = {}
    for i in range(len(strs)): 
        if str(sorted(strs[i])) not in groupAnagrams.keys(): 
            groupAnagrams[str(sorted(strs[i]))] = [strs[i]]
        else: 
            groupAnagrams[str(sorted(strs[i]))].append(strs[i])
    
    res = []
    for val in groupAnagrams.values(): 
        res.append(val)

    return res




        

