class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = right

        while left <= right:
            mid = (left + right) // 2

            current_load = 0
            days_needed = 1

            for weight in weights:
                if current_load + weight <= mid:
                    current_load += weight
                else:
                    days_needed += 1
                    current_load = weight

            if days_needed <= days:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


