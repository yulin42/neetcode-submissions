class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        cache = [[False] * n for _ in s]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or cache[i + 1][j - 1]):
                    cache[i][j] = True
                    if j - i + 1 > resLen:
                        resIdx = i
                        resLen = j - i + 1
                        
        return s[resIdx : resIdx + resLen]