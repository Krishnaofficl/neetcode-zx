class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0

        for i in range(n):
            height = heights[i]

            right = i+1
            while right<n and heights[right] >= height:
                right+=1

            left = i
            while left >= 0 and heights[left] >= height:
                left -= 1

            right -= 1
            left += 1

            area = max(area, height*(right - left + 1))
        
        return area