# “student. a am I”。后来才意识到，这家伙原来把句子单
# 词的顺序翻转了，正确的句子应该是“I am a student.”

class Solution:
    def ReverseSentence(self, s):
        if not s:
            return ''
        strs = s.split(" ")
        res =''
        for i in strs[::-1]:
            res += i[::] +' '

        return res[:len(res)-1]

    def ReverseSentence2(self, s):

        return " ".join(s.split(" ")[::-1]) #join代表以空格作为连接符


if __name__ == '__main__':
    print(Solution().ReverseSentence2('student. a am I'))

