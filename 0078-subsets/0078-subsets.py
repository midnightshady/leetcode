class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def explore(arr, current, i):
            if i == len(arr):
                result.append(current.copy())
                return

            # Choice 1: Choose
            current.append(arr[i])
            explore(arr, current, i + 1)
            current.pop()

            # Choice 2: Skip
            explore(arr, current, i + 1)
        explore(nums, [], 0)
        return result