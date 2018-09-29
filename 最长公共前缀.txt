class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        dict = {}
        str = strs[0]
        same = ''
        for str_ in strs[1::]:
            if str=='' or str_=='':
                return ''
            if str[0]!=str_[0] :
                return ''
            for i in range(min(len(str),len(str_))):
                if str_[i] == str[i]:
                    same += str[i]
            str = same
            same = ''

        return str
