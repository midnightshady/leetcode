class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n = len(nums)

        # value ke saath original index store karo
        arr = []

        for i in range(n):
            arr.append((nums[i], i))

        # values ke according sort
        arr.sort()

        i = 0

        while i < n:

            j = i

            # ek group find karo
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # is group ke original indices
            indices = []

            for k in range(i, j + 1):
                indices.append(arr[k][1])

            # original indices ko sort karo
            indices.sort()

            # values already sorted hain
            for k in range(len(indices)):
                nums[indices[k]] = arr[i + k][0]

            i = j + 1

        return nums