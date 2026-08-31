class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next

        index = 1

        first = -1
        last = -1
        minDist = float('inf')

        while curr.next:
            # Check if curr is a critical point
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                # First critical point
                if first == -1:
                    first = index

                # From second critical point onwards
                if last != -1:
                    minDist = min(minDist, index - last)

                last = index

            prev = curr
            curr = curr.next
            index += 1

        # Less than 2 critical points
        if first == last:
            return [-1, -1]

        # Last - first = maximum distance
        maxDist = last - first

        return [minDist, maxDist]