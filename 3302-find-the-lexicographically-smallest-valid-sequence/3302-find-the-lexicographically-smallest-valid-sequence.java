class Solution {
    public int[] validSequence(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();

        int [] rightHandSideMatchLength = new int[n + 1];

        int rightMatched = 0;
        int i = n - 1;
        int j = m - 1; 

        while(i >= 0){
            if(j >= 0 && word1.charAt(i) == word2.charAt(j)){
                rightMatched++;
                j --;
            }
            rightHandSideMatchLength[i] = rightMatched;
            i--;
        }

        List<Integer> seq = new ArrayList<>();
        boolean changePower = true;

        i = 0;
        j = 0;

        while(i < n && j < m){
            if (word1.charAt(i) == word2.charAt(j)){
                seq.add(i);
                j ++;
            }
            else if(changePower == true && rightHandSideMatchLength[i + 1] >= m - j - 1){
                seq.add(i);
                j ++;
                changePower = false;
            }
            i ++;
        }
        if(j == m){
            return seq.stream().mapToInt(Integer::intValue).toArray();
        } 
       return new int[0];
    }
}