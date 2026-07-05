class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, maxHeap = "", []
        for cnt,ch in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if cnt:
                heapq.heappush(maxHeap,(cnt,ch))

        while maxHeap:
            count,ch = heapq.heappop(maxHeap)
            if len(res)>1 and res[-1] == res[-2] == ch:
                if not maxHeap:
                    break
                count2,ch2 = heapq.heappop(maxHeap)
                res += ch2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap,(count2,ch2))

            else:
                res += ch
                count += 1

            if count:
                heapq.heappush(maxHeap,(count,ch))

        return res