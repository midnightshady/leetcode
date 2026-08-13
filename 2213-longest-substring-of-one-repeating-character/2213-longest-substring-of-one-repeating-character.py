class Solution:

    class Node:
        def __init__(self, ch=None):
            if ch is not None:
                self.maxLen = 1
                self.prefixLen = 1
                self.suffixLen = 1
                self.firstChar = ch
                self.lastChar = ch
                self.length = 1
            else:
                self.maxLen = 0
                self.prefixLen = 0
                self.suffixLen = 0
                self.firstChar = ''
                self.lastChar = ''
                self.length = 0

    def longestRepeating(self, s, queryCharacters, queryIndices):

        n = len(s)

        self.chars = list(s)
        self.tree = [None] * (4 * n)

        self.build(1, 0, n - 1)

        ans = []

        for i in range(len(queryIndices)):

            index = queryIndices[i]
            ch = queryCharacters[i]

            self.chars[index] = ch

            self.update(1, 0, n - 1, index, ch)

            ans.append(self.tree[1].maxLen)

        return ans

    def build(self, node, start, end):

        if start == end:
            self.tree[node] = self.Node(self.chars[start])
            return

        mid = (start + end) // 2

        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)

        self.tree[node] = self.merge(
            self.tree[2 * node],
            self.tree[2 * node + 1]
        )

    def update(self, node, start, end, index, ch):

        if start == end:
            self.tree[node] = self.Node(ch)
            return

        mid = (start + end) // 2

        if index <= mid:
            self.update(2 * node, start, mid, index, ch)
        else:
            self.update(2 * node + 1, mid + 1, end, index, ch)

        self.tree[node] = self.merge(
            self.tree[2 * node],
            self.tree[2 * node + 1]
        )

    def merge(self, left, right):

        res = self.Node()

        res.length = left.length + right.length
        res.firstChar = left.firstChar
        res.lastChar = right.lastChar

        res.maxLen = max(
            left.maxLen,
            right.maxLen
        )

        res.prefixLen = left.prefixLen
        res.suffixLen = right.suffixLen

        if left.lastChar == right.firstChar:

            # Repeating sequence crosses the boundary
            res.maxLen = max(
                res.maxLen,
                left.suffixLen + right.prefixLen
            )

            # Entire left segment is same character
            if left.prefixLen == left.length:
                res.prefixLen = (
                    left.length + right.prefixLen
                )

            # Entire right segment is same character
            if right.suffixLen == right.length:
                res.suffixLen = (
                    right.length + left.suffixLen
                )

        return res