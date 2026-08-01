class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for x in range(len(heights)):
            char = heights[x]
            while(stack and char < heights[stack[-1]]):
                height = heights[stack.pop()]
                if not stack:
                    low_lim = -1
                else:
                    low_lim = stack[-1]
                upper_lim = x
                width = upper_lim - low_lim - 1
                area = height * width
                ans = max(ans, area)
            stack.append(x)
        while stack:
            height = heights[stack.pop()]
            if stack : low_limit = stack[-1]
            else :low_limit = -1
            upper_limit = len(heights)
            width = upper_limit - low_limit - 1
            area = height * width
            ans = max(ans, area)
        return ans