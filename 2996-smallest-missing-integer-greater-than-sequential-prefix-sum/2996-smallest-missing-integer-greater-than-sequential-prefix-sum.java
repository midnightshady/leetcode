class Solution{
    public int missingInteger(int[] nums){
        int i = 0;
        int j = 1;
        int sum = 0;

        while (j < nums.length) {
            sum += nums[i];

            if(nums[j] - nums[i] != 1){
                break;
            }
            j++;
            i++;
        }
        if(j == nums.length){
            sum += nums[i];
        }
        int candidate = sum;
        boolean found = true;

        while (found) {
            found = false;

            for (int num : nums) {
                if (num == candidate) {
                    found = true;
                    candidate++;
                    break;
                }
            }
        }
        return candidate;
    }
}