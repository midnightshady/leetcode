class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)

        positions1 = []
        positions2 = []

        # 1s ki positions nikaalo
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    positions1.append((i, j))

                if img2[i][j] == 1:
                    positions2.append((i, j))

        offsets = {}
        ans = 0

        # img1 ke har 1 ko img2 ke har 1 se match karo
        for r1, c1 in positions1:
            for r2, c2 in positions2:

                dr = r2 - r1
                dc = c2 - c1

                offset = (dr, dc)

                offsets[offset] = offsets.get(offset, 0) + 1

                ans = max(ans, offsets[offset])

        return ans