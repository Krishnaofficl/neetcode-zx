class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt,ch] for ch,cnt in count.items()]
        heapq.heapify(maxHeap)
        res = ""

        prev = None

        while maxHeap or prev:
            
            if prev and not maxHeap:
                return ""
            cnt , ch = heapq.heappop(maxHeap)
            cnt += 1
            res += ch

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt!=0:
                prev = [cnt,ch]

        return res