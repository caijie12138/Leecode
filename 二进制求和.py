'''
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_ten = 0
        b_ten = 0
        count_a = 0
        count_b = 0
        for i in a[::-1]:
            a_ten += int(i)*2**count_a
            count_a += 1
        for i in b[::-1]:
            b_ten += int(i)*2**count_b
            count_b += 1
        all_sum = a_ten+b_ten
        res = bin(all_sum)
        return res[2:]            
