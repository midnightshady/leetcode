class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()

        low = 1
        high = position[-1] - position[0]
        ans = 0

        def can_place(distance):
            balls = 1
            last_position = position[0]

            for i in range(1, len(position)):
                if position[i] - last_position >= distance:
                    balls += 1
                    last_position = position[i]

                    if balls >= m:
                        return True

            return False

        while low <= high:
            mid = (low + high) // 2

            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans