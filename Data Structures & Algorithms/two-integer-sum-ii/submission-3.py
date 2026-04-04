class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''prevSum=defaultdict(int)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in prevSum:
                return [prevSum[diff],i+1]
            prevSum[numbers[i]]=i+1
        return []'''
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l)//2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []