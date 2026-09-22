from typing import List


class Node:
    def __init__(self, k):
        self.prod = 1
        self.cnt = [0] * k


class SegmentTree:
    def __init__(self, nums, k):
        self.k = k
        self.n = len(nums)
        self.tree = [None] * (4 * self.n)

        self.build(1, 0, self.n - 1, nums)

    def merge(self, left, right):
        k = self.k

        node = Node(k)

        # Product of complete left + right segment
        node.prod = (left.prod * right.prod) % k

        # Prefixes completely inside left
        for r in range(k):
            node.cnt[r] = left.cnt[r]

        # Prefixes that cross into right
        for r in range(k):
            node.cnt[(left.prod * r) % k] += right.cnt[r]

        return node

    def build(self, index, l, r, nums):
        if l == r:
            node = Node(self.k)

            value = nums[l] % self.k

            node.prod = value
            node.cnt[value] = 1

            self.tree[index] = node
            return

        mid = (l + r) // 2

        self.build(index * 2, l, mid, nums)
        self.build(index * 2 + 1, mid + 1, r, nums)

        self.tree[index] = self.merge(
            self.tree[index * 2],
            self.tree[index * 2 + 1]
        )

    def update(self, index, l, r, pos, value):
        if l == r:
            node = Node(self.k)

            value %= self.k

            node.prod = value
            node.cnt[value] = 1

            self.tree[index] = node
            return

        mid = (l + r) // 2

        if pos <= mid:
            self.update(index * 2, l, mid, pos, value)
        else:
            self.update(index * 2 + 1, mid + 1, r, pos, value)

        self.tree[index] = self.merge(
            self.tree[index * 2],
            self.tree[index * 2 + 1]
        )

    def query(self, index, l, r, ql, qr):

        # Completely inside query range
        if ql <= l and r <= qr:
            return self.tree[index]

        mid = (l + r) // 2

        # Query only left
        if qr <= mid:
            return self.query(
                index * 2,
                l,
                mid,
                ql,
                qr
            )

        # Query only right
        if ql > mid:
            return self.query(
                index * 2 + 1,
                mid + 1,
                r,
                ql,
                qr
            )

        # Query overlaps both sides
        left = self.query(
            index * 2,
            l,
            mid,
            ql,
            qr
        )

        right = self.query(
            index * 2 + 1,
            mid + 1,
            r,
            ql,
            qr
        )

        return self.merge(left, right)


class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)

        tree = SegmentTree(nums, k)

        ans = []

        for index, value, start, x in queries:

            # Permanent update
            tree.update(
                1,
                0,
                n - 1,
                index,
                value
            )

            # Query [start, n-1]
            node = tree.query(
                1,
                0,
                n - 1,
                start,
                n - 1
            )

            ans.append(node.cnt[x])

        return ans