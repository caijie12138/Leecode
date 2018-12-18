'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return self.generate(rowIndex+1)

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        start = [1, 1]
        if numRows == 0:
            return []
        if numRows == 1:
            return [1]
        if numRows == 2:
            return [1, 1]
        for i in range(2, numRows):
            res_step = [1]
            for i in range(len(start) - 1):
                j = i + 1
                res_step.append(start[i] + start[j])
            res_step.append(1)
            start = res_step
        return start
