class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        target = total//2
        dp = [False]*(target+1)
        dp[0] = True

        for num in nums:
            for j in range(target,num-1,-1):
                #if cur num is 5 and j is 6
                #then if we can form 1 i.e.,d[1] = dp[6-5 #j-num] 
                #then we can form dp[6] vice varsa for dp[5] and dp[1]
                if dp[j-num]:
                    dp[j] = True
                if dp[target]:
                    return True

        return dp[target]