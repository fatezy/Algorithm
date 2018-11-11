class MergeSort:
    @staticmethod
    def merge_sort(arr):
        if not arr or len(arr)<2:
            return
        MergeSort.merge_sort1(arr,0,len(arr)-1)
        return arr

    @staticmethod
    def merge_sort1(arr,l,r):
        """
        :param arr: 待排序数组
        :param l: 起始位置
        :param r: 终止位置
        :return: 结果
        """
        if l == r:
            return
        mid = int((l+r)/2)
        MergeSort.merge_sort1(arr,l,mid)
        MergeSort.merge_sort1(arr,mid+1,r)
        MergeSort.merge(arr,l,mid,r)


    @staticmethod
    def merge(arr,l,m,r):
        help = [0 for i in range(r-l+1)]
        i,p1,p2 = 0,l,m+1
        while p1 <= m and p2 <=r:
            help[i] = arr[p1] if arr[p1] < arr[p2] else arr[p2]
            i += 1
            if arr[p1]<arr[p2]:
                p1+=1
            else:
                p2 += 1
        while p1<=m:
            help[i] = arr[p1]
            i,p1 = i+1,p1+1
        while p2 <= r:
            help[i] = arr[p2]
            i,p2 = i+1,p2+1

        arr[l:l+len(help)] = help[::]



if __name__ == '__main__':
    a = [212,22,3,643]
    print(MergeSort.merge_sort(a))