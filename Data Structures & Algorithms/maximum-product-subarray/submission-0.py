class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1
        
        for num in nums:
            tmp = curMin * num
            curMin = min(num * curMin, num * curMax, num)
            curMax = max(tmp, num * curMax, num)
            res = max(curMax, res)
        
        return res