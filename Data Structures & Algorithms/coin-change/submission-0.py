class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        for i in coins:
            dp[i] = 1
        
    
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]

            res = -1
            
            for coin in coins:
                if coin > amount:
                    continue
                rest = dfs(amount - coin)
                if rest != -1:
                    if res == -1:
                        res = rest + 1
                    else:
                        res = min(res, rest + 1)
            
            dp[amount] = res
            return res

        print(dp)
        return dfs(amount)