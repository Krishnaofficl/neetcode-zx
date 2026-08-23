class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #using prefix sum: currentsum - previoussum = k
        prefix = {0:1}
        res = 0
        total = 0
        for num in nums:
            total += num
            if total-k in prefix:
                res += prefix[total-k]
            prefix[total] = prefix.get(total, 0) + 1

        return res
            