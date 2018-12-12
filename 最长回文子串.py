class Solution:
    def longestPalindrome(self, s):
        str=''
        max_value = 0
        leftindex = 0
        rightindex = 0
        for i in range(len(s)):
            #如果回文串是奇数
            left = i-1
            right = i+1
            while left>=0 and right < len(s) and left < right:
                if s[left]==s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            left += 1
            right -= 1
            if right-left+1 > max_value:
                max_value = right-left+1
                rightindex = right
                leftindex = left
            #如果回文串是偶数
        for i in range(len(s)):
            #如果回文串是奇数
            left = i
            right = i+1
            while left>=0 and right < len(s) and left < right:
                if s[left]==s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            left += 1
            right -= 1
            if right-left+1 > max_value:
                max_value = right-left+1
                rightindex = right
                leftindex = left
        str = s[leftindex:rightindex+1]
        return str
