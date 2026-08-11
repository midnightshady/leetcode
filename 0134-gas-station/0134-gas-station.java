class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost){
        int n = gas.length;
        int [] diff = new int[n];
        for(int i = 0; i < n; i ++){
            diff[i] = gas[i] - cost[i];
        }
        int total = 0;
        for (int i = 0; i < n; i ++){
            total += diff[i];
        }
        if(total < 0){
            return -1;
        }
        int sm = 0;
        int start = 0;
        for (int i = 0; i < n; i ++){
            sm += diff[i];
            if(sm < 0){
                sm = 0;
                start = i + 1;
            }
        }
        return start;
    }
}