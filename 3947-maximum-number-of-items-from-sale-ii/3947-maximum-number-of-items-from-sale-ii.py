from collections import Counter
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        freq = Counter(factor for factor, price in items)
        limit = max(freq)

        offers = []
        min_price = min(price for factor, price in items)

        for factor, price in items:
            free = sum(
                freq.get(multiple, 0)
                for multiple in range(factor, limit + 1, factor)
            ) - 1

            if free > 0:
                offers.append((price, free))

        offers.sort()
        ans = 0

        for price, free in offers:
            if price >= 2 * min_price:
                break

            buy = min(free, budget // price)

            ans += 2 * buy
            budget -= buy * price

        ans += budget // min_price

        return ans