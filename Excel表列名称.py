'''
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"
'''
class Solution(object):
    def convertToTitle(self,n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        if n>=26 and n<=26*26:
            length = math.ceil(math.log(n,26))
        elif n>26*26:
            length = math.ceil(math.log(n-26,26))
        else:
            length = 1
        for i in range(int(length)):
            if i == length-1:
                res += str(chr(n + 64))
            else:
                if n%26==0:
                    res += str(chr(26+64))
                    n -= 26
                else:
                    res += str(chr(n % 26 + 64))
            n = n // 26
        return res[::-1]


