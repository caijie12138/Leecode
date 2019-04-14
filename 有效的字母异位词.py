给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        dic2 = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for j in t:
            if j not in dic:
                return False
            else:
                if j not in dic2:
                    dic2[j] = 1
                else:
                    dic2[j] += 1
        for key in dic:
            if dic[key] != dic2[key] or len(dic)!=len(dic2):
                return False
        return True
