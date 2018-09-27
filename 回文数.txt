class Solution {
    public boolean isPalindrome(int x) {
        Boolean flag = true;
        String s = String.valueOf(x);
        if (s.length() % 2 == 0) {
            for (int i = 0; i < s.length() / 2; i++)
                if (s.charAt(i) != s.charAt(s.length() - i - 1)) {
                    flag = false;
                    break;
                }
        } else {
            for (int i = 0; i < s.length() / 2; i++)
                if (s.charAt(i) != s.charAt(s.length() - i - 1)) {
                    flag = false;
                    break;
                }
        }
        return flag;
    }
}
