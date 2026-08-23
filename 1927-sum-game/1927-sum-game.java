class Solution {
    public boolean sumGame(String num){
        int leftQnmarkcount = 0;
        int rightQnmarkcount = 0;
        int leftKnownsum = 0;
        int rightKnownsum = 0;;
        
        int n = num.length();
        
        for (int i = 0; i < n; i++) {
            if (num.charAt(i) == '?') {
                if (i < n / 2){
                    leftQnmarkcount++;
                }
                else{
                    rightQnmarkcount++ ;
                }
            }
            else{
                    if (i < n / 2){
                        leftKnownsum += num.charAt(i) - '0';
                    }
                    else{
                        rightKnownsum += num.charAt(i) - '0' ;
                    }
                }  
            }
            int totalQnmarkcount = leftQnmarkcount + rightQnmarkcount;
            if(totalQnmarkcount % 2 == 1){
                return true;
            }
            int LEFT = 2 * leftKnownsum + 9 * leftQnmarkcount;
            int RIGHT = 2 * rightKnownsum + 9 * rightQnmarkcount;
            if(LEFT == RIGHT){
                return false;
            }
            else{
                return true;
            }
        }
    }