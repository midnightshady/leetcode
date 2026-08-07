class Solution {
    public int lengthOfLastWord(String s) {
        // StringBuilder ans = new StringBuilder();

        int i = s.length() - 1;

        while(i >= 0){
            while(i >= 0 && s.charAt(i) == ' '){
                i --;
            }
            if (i < 0){
                break;
            }
            int end = i;

            while (i >= 0 && s.charAt(i) != ' '){
                i --;
            }
            int start = i;

            return end - start;
        }
        return 0;
    }
}