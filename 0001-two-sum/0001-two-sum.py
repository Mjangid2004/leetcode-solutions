class Solution(object):
    def twoSum(self, nums, target):
        # indexed_nums = sorted((val, i) for i, val in enumerate(nums))

        # l = 0
        # r = len(nums) - 1
    
        # while l < r:
        #     current_sum = indexed_nums[l][0] + indexed_nums[r][0]
        
        #     if current_sum == target:
        #         return [indexed_nums[l][1], indexed_nums[r][1]]
        
        #     elif current_sum < target:
        #         l += 1
        #     else:
        #         r -= 1
            
        # return [] 
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i, j