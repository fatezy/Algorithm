
class Solution:
    def kmp1(self,M,N):
        """
        暴力匹配算法
        :param M:
        :param N:
        :return:
        """
        if not M or not N:
            return None

        for i in range(len(M)):
            if i+len(N)<=len(M) and M[i:i+len(N)] == N:
                return i
        return -1


    def kmp2(self,M,N):
        """
        kmp匹配算法，next长度与N相同，next[i]的值代表的含义是指match[i]位置的前缀子串和
        后续子串的最大匹配长度。
        如： N = "abc1abc1",则最后一个字符即N[7]的前缀子串(不包括当前的字符)与后缀子串(不包含首字符)的最大匹配长度为3，即abc
        1. 先生成next数组
        2. 对M,N利用next数组进行匹配
        :param M: 母串
        :param N: 子串
        :return:
        """
        if not M or not N:
            return
        mi,ni = 0,0
        next_array = self.getNextArray(N)
        while mi < len(M) and ni < len(N):
            if M[mi] == N[ni]:
                mi += 1
                ni += 1
            elif next_array[ni] == -1:
                mi += 1
            else:
                ni = next_array[ni]
        return mi-ni if ni == len(N) else -1  # ni == len(N)代表匹配成功

    def getNextArray(self,N):
        if not N:
            return []
        if len(N) == 1:
            # 当字符长度为1的时候，前缀子串和后缀子串均为空，因此next数组为第一个字符为-1
            return [-1]
        next_array = [0 for i in range(len(N))]
        next_array[0],next_array[1] = -1,0
        pos = 2  # 后缀子串待匹配的位置
        cn = 0  # 前缀子串待匹配的位置
        while pos < len(N):
            if N[pos-1] == N[cn]:
                next_array[pos] = cn+1
                cn += 1
                pos += 1
            elif cn > 0:
                cn = next_array[cn]
            else:
                next_array[pos] = 0
                pos += 1
        return next_array




if __name__ == '__main__':
    print(Solution().getNextArray("abc1abc1"))
    print(Solution().kmp1("google","oo"))
    print(Solution().kmp2("google","oo"))





