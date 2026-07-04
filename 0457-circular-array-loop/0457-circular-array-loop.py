class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):

            # Already visited
            if nums[i] == 0:
                continue

            slow = fast = i
            direction = nums[i] > 0

            while True:

                # -------- slow --------
                next_slow = next_index(slow)

                if nums[next_slow] == 0 or (nums[next_slow] > 0) != direction:
                    break

                # -------- fast step 1 --------
                next_fast = next_index(fast)

                if nums[next_fast] == 0 or (nums[next_fast] > 0) != direction:
                    break

                # -------- fast step 2 --------
                next_fast2 = next_index(next_fast)

                if nums[next_fast2] == 0 or (nums[next_fast2] > 0) != direction:
                    break

                slow = next_slow
                fast = next_fast2

                # Self loop
                if slow == next_index(slow):
                    break

                if slow == fast:
                    return True

            # ---------- Mark visited path ----------
            cur = i
            while nums[cur] != 0 and (nums[cur] > 0) == direction:
                nxt = next_index(cur)
                nums[cur] = 0
                cur = nxt

        return False
        