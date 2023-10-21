def longestSubarray(nums, diff):
    max = 0
    left, right = 0, 1 
    
    while (right <= len(nums)-1): 
        if abs(nums[right] - nums[right - 1]) <= diff:
            right += 1 
        else: 
            new_max = len(nums[left:right])
            if new_max > max: 
                max = new_max 
            left = right 
            right += 1

    new_max = len(nums[left:right])
    if new_max > max: 
        max = new_max 

    return max 
