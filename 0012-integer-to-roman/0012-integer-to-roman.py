class Solution:
    def intToRoman(self, num: int) -> str:
        ones = [
            "", "I", "II", "III", "IV",
            "V", "VI", "VII", "VIII", "IX"
        ]

        tens = [
            "", "X", "XX", "XXX", "XL",
            "L", "LX", "LXX", "LXXX", "XC"
        ]

        hundreds = [
            "", "C", "CC", "CCC", "CD",
            "D", "DC", "DCC", "DCCC", "CM"
        ]

        thousands = [
            "", "M", "MM", "MMM"
        ]

        maps = [ones, tens, hundreds, thousands]

        result = ""
        place = 0

        while num > 0:
            temp = num % 10
            result = maps[place][temp] + result

            num //= 10
            place += 1

        return result