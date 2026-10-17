class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        swaps = 0
        def digit_sum(n):
            total = 0

            while n > 0:
                total += n % 10
                n //= 10

            return total
        target = sorted(nums, key=lambda n: (digit_sum(n), n))

        indexMap = defaultdict(int)

        for i in range(len(nums)):
            indexMap[nums[i]] = i
        visited = [False] * len(nums)
        for i in range(len(target)):
            if visited[i] or indexMap[target[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = indexMap[target[j]]
                cycle_size += 1

            swaps += cycle_size - 1
        return swaps