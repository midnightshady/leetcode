class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            if height[left] < height[right]:
                width = right - left
                heights = height[left]
                area = width * heights
                left += 1
            else:
                width = right - left
                heights = height[right]
                area = width * heights
                right -= 1
            result = max(result, area)
        return result