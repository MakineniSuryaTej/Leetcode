class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j, area = 0, n - 1, 0
        while i < j:
            area = max(area, (j - i)*min(height[i], height[j]))
            if height[i] < height[j]: i += 1
            else: j -= 1
        return area
