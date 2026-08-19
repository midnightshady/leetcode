class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):

        rows = {}

        for row, seat in reservedSeats:

            if 2 <= seat <= 9:
                if row not in rows:
                    rows[row] = 0

                rows[row] |= 1 << (seat - 2)

        ans = (n - len(rows)) * 2

        for mask in rows.values():

            left = 0b00001111
            middle = 0b00111100
            right = 0b11110000

            if (mask & left) == 0 and (mask & right) == 0:
                ans += 2

            elif ((mask & left) == 0 or
                  (mask & middle) == 0 or
                  (mask & right) == 0):
                ans += 1

        return ans