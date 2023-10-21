class Solution:
    def threeSum(self, nums):
        triples = [] 
        nums.sort()

        for i, num in enumerate(nums): 
            left, right = i + 1, len(nums) - 1 
            if num == nums[i-1]: 
                continue 
            while left < right: 
                threeSum = num + nums[left] + nums[right]

                if threeSum > 0: 
                    right -= 1 
                elif threeSum < 0: 
                    left += 1 
                else: 
                    triples.append(num, nums[left], nums[right])
            left += 1 
            while nums[left] == nums[left-1] and left < right: 
                left += 1 
        return triples
                
            

            
                



