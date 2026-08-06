class Solution {
    public int jump(int[] nums) {
        int curReach = 0;
        int curMax = 0;
        int jumps = 0;

        for (int i = 0; i < nums.length - 1; i ++){
            curMax = Math.max(curMax, i + nums[i]);
            if (i == curReach){
                jumps ++;
                curReach = curMax;
            }
        }
        return jumps;
    }
}