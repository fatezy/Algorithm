# “student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，
# 正确的句子应该是“I am a student.”。

class Solution:
    def ReverseSentence(self, s):
        if not s:
            return ""
        s_list = s.split(' ')
        s_list = [i[::-1] for i in s_list]

        return " ".join(s_list)[::-1]

if __name__ == '__main__':
    print(Solution().ReverseSentence("student. a am I"))