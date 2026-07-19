class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for ch in operations:
            if ch == "C":
                stack.pop()
            elif ch == "D":
                temp = 2*stack[-1]
                stack.append(int(temp))
            elif ch == "+":
                temp = (stack[-1]) + (stack[-2])
                stack.append(int(temp))
            else:
                stack.append(int(ch))
        
        Sum = 0
        for i in stack:
            Sum = Sum + i

        return Sum 