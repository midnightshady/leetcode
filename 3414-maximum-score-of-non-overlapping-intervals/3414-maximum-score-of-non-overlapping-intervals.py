from functools import lru_cache

class Solution:
    def maximumWeight(self, intervals):
        arr = []

        for i, (start, end, weight) in enumerate(intervals):
            arr.append([start, end, weight, i])

        # Sort by start time
        arr.sort()

        n = len(arr)

        # Binary search:
        # first interval whose start > current end
        def find_next(end):
            left = 0
            right = n

            while left < right:
                mid = (left + right) // 2

                if arr[mid][0] > end:
                    right = mid
                else:
                    left = mid + 1

            return left

        @lru_cache(None)
        def solve(i, count):
            if i == n or count == 4:
                return (0, ())

            # Don't take current interval
            skip = solve(i + 1, count)

            # Take current interval
            start, end, weight, index = arr[i]

            next_i = find_next(end)

            next_weight, next_indices = solve(next_i, count + 1)

            take_weight = weight + next_weight
            take_indices = tuple(sorted((index,) + next_indices))

            take = (take_weight, take_indices)

            # Better weight
            if take_weight > skip[0]:
                return take

            if take_weight < skip[0]:
                return skip

            # Same weight → lexicographically smaller
            return min(take, skip, key=lambda x: x[1])

        return list(solve(0, 0)[1])