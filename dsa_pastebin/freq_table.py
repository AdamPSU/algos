def freq_table(nums): 
    '''Increments the value by 1 every time it encounters the key. 
    If the key hasn't been defined yet, the value is initialized to 1.'''
    freq = {} 
    for num in nums: 
        freq[num] = freq.get(num, 0) + 1
    return freq 


























