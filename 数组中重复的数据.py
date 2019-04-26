'''
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]
'''
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            while i != nums[i]-1:
                if nums[i] != nums[nums[i]-1]: 
                    tmp = nums[i]
                    nums[i] = nums[nums[i]-1]
                    nums[tmp-1] = tmp
                else:
                    res.append(nums[i])
                    break
        return list(set(res))
        
