
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


if __name__ == '__main__':
    print(Solution().kmp1("google","ooa"))





