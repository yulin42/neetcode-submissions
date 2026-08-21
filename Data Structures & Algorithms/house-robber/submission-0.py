class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1 for i in range(len(nums))]
        def rob(i):
            if i == len(nums) - 1:
                return nums[i]
            elif i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = max(nums[i] + rob(i+2), rob(i+1))
            return cache[i]
        
        return rob(0)