'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        start = [1, 1]
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1, 1]]
        res = [[1],[1,1]]
        for i in range(2, numRows):
            res_step = [1]
            for i in range(len(start) - 1):
                j = i + 1
                res_step.append(start[i] + start[j])
            res_step.append(1)
            res.append(res_step)
            start = res_step
        return res
            
        
