'''
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(46340,0,-1):
            if i**2 <= x:
                return i
#看评论里还有使用牛顿法的，详情请见：https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)
