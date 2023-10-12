# 238. Product of Arrays Except Self 

def longestConsecutive(nums):
        #to determine smallest value 
        smallest = len(nums)
        for i in range(len(nums)): 
            if nums[i] < smallest: 
                smallest = nums[i]
        #to track consec nums
        longest_consec, length = 0, 0 
        for _ in range(len(nums)): 
            smallest += 1 
            if smallest in nums: 
                length += 1 
            elif length > longest_consec:
                longest_consec = length 
                length = 0 
        return longest_consec 
                
                 
print(longestConsecutive([1, 2, 3, 5, 6, 7, 8]))




    
    
    



        
        