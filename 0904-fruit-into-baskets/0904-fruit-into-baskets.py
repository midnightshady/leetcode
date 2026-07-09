class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left, right, res, total = 0, 0, 0, 0
        freq = {}

        for right in range(len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right], 0) + 1

            while len(freq) > 2:
                f = fruits[left]
                freq[f] -= 1
                left += 1

                if not freq[f]:
                    freq.pop(f)
            total = right - left + 1
            res =max(res, total)

        return res