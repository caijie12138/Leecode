'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = ''
        for i in s:
            if ord(i)>=48 and ord(i)<=57:
                new += i
            if ord(i)>=65 and ord(i)<=90:
                new += i.lower()
            if ord(i)>=97 and ord(i)<=122:
                new += i
        return new == new[::-1]

