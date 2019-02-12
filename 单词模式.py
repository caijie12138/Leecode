给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。

这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_sp = str.split()
        if len(str_sp)==1 and len(pattern) ==1:
            return True
        if len(str_sp)==1 or len(str_sp)!=len(pattern):
            return False
        dic = {}
        for i in range(len(pattern)):
            if dic.get(pattern[i]) == None and str_sp[i] not in dic.values():
                dic[pattern[i]] = str_sp[i]
            else:
                if str_sp[i] != dic.get(pattern[i]):
                    return False
        return True
