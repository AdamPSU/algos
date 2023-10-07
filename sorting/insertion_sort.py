def insertion_sort(nums): 
    for i in range(2, len(nums)): 
        current = nums[i] #track the current iteration for later
        j = i - 1 
        while (j >= 0 and nums[j] > current): 
            nums[i] = nums[j]
            j -= 1 
        nums[j] = current 
    return nums

print(insertion_sort([1, 2, 4, 3]))

