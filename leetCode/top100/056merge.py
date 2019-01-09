# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e




class Solution(object):


    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x.start) # 对类进行排序
        res = [] # 二维列表
        res.append(intervals[0])
        for i in range(len(intervals)):
            if res[-1].end >= intervals[i].start and res[-1].end < intervals[i].end:
                res[-1].end = intervals[i].end
            if res[-1].end < intervals[i].start:
                res.append(intervals[i])
        return res


if __name__ == '__main__':
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))

