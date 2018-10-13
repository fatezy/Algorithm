# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为
# We%20Are%20Happy。

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        if not s:
            return ''
        else:
            return s.replace(' ','%20')


    def replaceSpace2(self,s):
        if not s:
            return ''

        res =''
        for c in s:
            if c==' ':
                res += '%20'
            else:
                res +=c

        return res



