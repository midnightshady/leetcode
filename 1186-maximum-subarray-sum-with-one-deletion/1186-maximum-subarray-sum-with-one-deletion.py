class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        no_delete , one_delete = arr[0], float('-inf')
        ans = arr[0]

        for i in range(1, len(arr)):
            n = arr[i]

            prev_no_delete = no_delete
            prev_one_delete = one_delete
            no_delete = max(n, prev_no_delete + n)
            one_delete = max(prev_one_delete + n, prev_no_delete)

        
            ans = max(ans, no_delete, one_delete)
        return ans 

        