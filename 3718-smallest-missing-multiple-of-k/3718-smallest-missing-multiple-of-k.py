class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        multiple = k

        while True:

            found = False

            for num in nums:
                if num == multiple:
                    found = True
                    break

            if not found:
                return multiple

            multiple += k