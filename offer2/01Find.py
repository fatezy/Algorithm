# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一
# 个整数，判断数组中是否含有该整数。

class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array:
            return False
        length = len(array[0])
        high = len(array)

        i,j = 0,length-1
        while i< high and j>=0:
            if target == array[i][j]:
                return True
            if target > array[i][j]:
                i += 1
            else:
                j -= 1
        return False



if __name__ == '__main__':
    print(Solution().Find(16,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))