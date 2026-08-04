class Solution:
    def stoneGameIII(self, values: List[int]) -> str:
        
        n = len(values)
        dp = [float("-inf")]*(n+1)
        dp[n] = 0
        for i in range(n-1,-1,-1):
            for j in range(i,min(i+3,n)):
                dp[i] = max(dp[i],sum(values[i:j+1])-dp[j+1])

        ans = dp[0]
        if ans == 0:
            return "Tie"
        return "Alice" if ans>0 else "Bob"