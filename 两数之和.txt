class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> list = new HashMap<Integer,Integer>();
        int[] result = new int[2];
        for(int i = 0;i<nums.length;i++)
            list.put(nums[i],i);
        for(int j = 0;j<nums.length;j++)
            if(list.containsKey(target-nums[j]) && j!=list.get(target-nums[j])){
                result[0]=j;
                result[1]=list.get(target-nums[j]);
                return result;
            }
        return result;
    }
}
