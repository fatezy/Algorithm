# 在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。求一个数组
# 的小和。

class SmallSum:

    @staticmethod
    def small_sum(arr):
        if not arr or len(arr) < 2:
            return
        sum = SmallSum.merge_sort1(arr, 0, len(arr) - 1)
        return sum

    @staticmethod
    def merge_sort1(arr, l, r):
        """
        :param arr: 待排序数组
        :param l: 起始位置
        :param r: 终止位置
        :return: 结果
        """
        if l == r:
            return 0
        mid = int((l + r) / 2)
        return SmallSum.merge_sort1(arr, l, mid)+SmallSum.merge_sort1(arr, mid + 1, r)+SmallSum.merge(arr, l, mid, r)

    @staticmethod
    def merge(arr, l, m, r):
        help = [0 for i in range(r - l + 1)]
        i, p1, p2,res = 0, l, m + 1,0
        while p1 <= m and p2 <= r:
            res += (r-p2+1)*arr[p1] if arr[p1]<arr[p2] else 0
            help[i] = arr[p1] if arr[p1] < arr[p2] else arr[p2]
            i += 1
            if arr[p1] < arr[p2]:
                p1 += 1
            else:
                p2 += 1
        while p1 <= m:
            help[i] = arr[p1]
            i, p1 = i + 1, p1 + 1
        while p2 <= r:
            help[i] = arr[p2]
            i, p2 = i + 1, p2 + 1

        arr[l:l + len(help)] = help[::]
        return res

    @staticmethod
    def comparator(arr):
        if not arr or len(arr)<2:
            return 0
        res = 0
        for i in range(len(arr)):
            for j in range(0,i):
                res += arr[j] if arr[j] < arr[i] else 0
        return res


if __name__ == '__main__':
    print(SmallSum.small_sum([1, 3, 4, 2, 5]))
    print(SmallSum.comparator([1, 3, 4, 2, 5]))