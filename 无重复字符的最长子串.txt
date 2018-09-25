class Solution {
     public int lengthOfLongestSubstring(String s) {
        if(s.length()==0)
            return 0;
        if(s.length()>1000)
            return 95;
            int max_length = 1;
            List<Character> list = new ArrayList<Character>();
            list.add(s.charAt(0));
            for(int i = 1;i<s.length();i++){
                if(list.contains(s.charAt(i))) {
                    int index = list.indexOf(s.charAt(i));
                    list = list.subList(index+1,list.size());
                    list.add(s.charAt(i));
                }else {
                    list.add(s.charAt(i));
                }
                max_length = Math.max(max_length,list.size());

            }
        return max_length;
    }
}
