class Solution {
    public int maxArea(int[] height) {
        int max_area = 0;
        for(int i = 0,j = height.length-1;i<j;) {
            if ((j - i) * (height[i] > height[j] ? height[j] : height[i]) > max_area)
                max_area = (j - i) * (height[i] > height[j] ? height[j] : height[i]);
            if (height[i] > height[j])
                j--;
            else
                i++;
        }
        return max_area;
    }
}
