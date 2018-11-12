class QuickSort:
    @staticmethod
    def quick_sort(arr):
        if not arr or len(arr)<2:
            return arr
        QuickSort.quick_sort_helper(arr,0,len(arr)-1)
        return arr



    @staticmethod
    def quick_sort_helper(arr,l,r):
        if l<r:
            p = QuickSort.partition(arr,l,r)
            QuickSort.quick_sort_helper(arr,l,p[0]-1)
            QuickSort.quick_sort_helper(arr,p[1]+1,r)


    @staticmethod
    def partition(arr,l,r):
        """
        对数组进行划分，大于num放于右边，小于num放于左边
        :param arr:
        :param l:
        :param num:
        :return:
        """
        less = l-1 # 小的区域
        more = r # 大的区域
        curr = l
        while  curr < more:
            if arr[curr] < arr[r]:
                less += 1
                arr[curr],arr[less] = arr[less],arr[curr]
                curr += 1
            elif arr[curr] > arr[r]:
                more -= 1
                arr[curr],arr[more] = arr[more],arr[curr]
            else:
                curr += 1

        arr[more],arr[r] = arr[r], arr[more]
        return [less+1,more]

if __name__ == '__main__':
    print(QuickSort.quick_sort([9, 5, 3, 6, 7]))










