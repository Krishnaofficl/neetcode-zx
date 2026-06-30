
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            cur = heapq.heappop(stones) - heapq.heappop(stones)
            if abs(cur):
                heapq.heappush(stones,cur)

        return abs(stones[0]) if stones else 0

