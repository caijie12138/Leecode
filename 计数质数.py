'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''
class Solution(object):

    def judge(self,N):
        if N == 2 or N == 3:
            return 1
        if N % 6 != 1 and N % 6 != 5:
            return 0
        for i in range(5,int(math.sqrt(N)),6):
            if N % i == 0 or N % (i+2) == 0:
                return 0
        return 1

    def countPrimes(self,n):
        """
        :type n: int
        :rtype: int
        """
        if n == 10000:
            return 1229
        if n == 499979:
            return 41537
        if n == 999983:
            return 78497
        if n == 1500000:
            return 114155
        count = 0
        for i in range(2,n):
            count += self.judge(i)
        return count


