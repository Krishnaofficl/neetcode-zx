class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        passChange = [0]*(1001)

        for t in trips:
            num, start, end = t
            passChange[start] += num
            passChange[end] -= num

        curr = 0
        for p in passChange:
            curr += p
            if curr > capacity:
                return False

        return True