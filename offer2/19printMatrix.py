# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，
# 如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打
# 印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
import numpy as np

class Solution:
    # matrix类型为二维列表，需要返回列表
    # 代码写的真鸡儿丑
    def printMatrix(self, matrix):
        res = []
        while matrix:
            res.extend(matrix.pop(0))  # 右

            if not matrix:            # 防止就一行
                break
            for line in matrix:        # 下
                if not line:
                    break
                res.append(line.pop())

            if not matrix:            # 防止就一行
                break
            res.extend(matrix.pop(-1)[::-1]) # 左

            if not matrix:            # 防止就一行
                break
            temp = []
            for line in matrix:
                if not line:
                    break
                temp.append(line.pop(0))  # 上
            res.extend(temp[::-1])

        return res



    # matrix类型为二维列表，需要返回列表
    #优雅
    def printMatrix2(self, matrix):
        res = []
        while matrix:
            res.extend(matrix.pop(0))  # left to right
            if matrix and matrix[0]:  # top to dwon
                for row in matrix:
                    res.append(row.pop())
            if matrix:  # right to left
                res.extend(matrix.pop()[::-1])
            if matrix and matrix[0]:  # bottom to up
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res



if __name__ == '__main__':
    li = np.arange(1,17).reshape(4,4).tolist()
    print(Solution().printMatrix([[1],[2],[3],[4],[5]]))
