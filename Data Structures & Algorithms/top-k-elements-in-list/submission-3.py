class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        res=[]
        for key,val in count.items():
            res.append([val,key])
        res.sort(reverse=True)
        return [res[i][1] for i in range(k)]

        