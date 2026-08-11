class Solution {
    public int candy(int[] ratings){
        int[] candies = new int[ratings.length];
        Arrays.fill(candies, 1);
        
        int i = 1;
        // left -> right
        while(i < ratings.length){
            if(ratings[i] > ratings[i - 1] && candies[i] <= candies[i - 1]){
                candies[i] = candies[i - 1] + 1;
            }
            i ++;
        }
        //right -> left
        i = ratings.length - 1;
        int sum = 0;
        while(i > 0){
            if(ratings[i - 1] > ratings[i] && candies[i - 1] <= candies[i]){
                candies[i - 1] = candies[i] + 1;
            }
            sum += candies[i];
            i --;
        }
        sum += candies[i];
        return sum;
    }
}