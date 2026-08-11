class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        if sum(diff) < 0:
            return - 1
        sm = 0
        start = 0
        for i in range(len(diff)):
            sm += diff[i]
            if sm < 0:
                sm = 0
                start = i + 1
        return start