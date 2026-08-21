class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(i, n, cache):
            if i == n - 1:
                return nums[i]
            elif i >= n:
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = max(rob(i+2, n, cache) + nums[i], rob(i + 1, n, cache))
            return cache[i]
        
        if len(nums) == 1:
            return nums[0]
        
        return max(rob(0, len(nums) - 1, [-1] * len(nums)) , rob(1, len(nums), [-1] * len(nums))) 