class Solution:
    def checkValidString(self, s):
        minBalance = 0
        maxBalance = 0

        for ch in s:

            if ch == '(':
                minBalance += 1
                maxBalance += 1

            elif ch == ')':
                minBalance -= 1
                maxBalance -= 1

            else:  # '*'
                minBalance -= 1
                maxBalance += 1

            # Even maximum possible balance is negative
            if maxBalance < 0:
                return False

            # Negative minimum balance is not possible
            minBalance = max(0, minBalance)

        return minBalance == 0