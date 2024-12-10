class Solution {
    public boolean checkValidString(String s) {
        int openLow = 0, openHigh = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                openLow++;
                openHigh++;
            } else if (c == ')') {
                openLow = Math.max(0, openLow - 1);
                openHigh--;
            } else { // c == '*'
                openLow = Math.max(0, openLow - 1);
                openHigh++;
            }

            if (openHigh < 0) {
                return false;
            }
        }

        return openLow == 0;
    }
}
