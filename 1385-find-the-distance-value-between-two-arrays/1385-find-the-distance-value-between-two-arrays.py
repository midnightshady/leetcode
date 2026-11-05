class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2 = sorted(arr2)
        count = 0

        for num in arr1:
            low = 0
            high = len(arr2) - 1
            found = False

            while low <= high:
                mid = (low + high) // 2

                if abs(num - arr2[mid]) <= d:
                    found = True
                    break

                elif arr2[mid] < num - d:
                    low = mid + 1

                else:
                    high = mid - 1

            if not found:
                count += 1

        return count


