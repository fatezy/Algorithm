import random
class BubbleSort:
    def __init__(self):
        pass

    @staticmethod
    def bubble_sort(arr):
        if not arr or len(arr)< 2:
            return arr

        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]

        return arr

    @staticmethod
    def compareator(arr):
        arr.sort()

    @staticmethod
    def generate_random_arr(maxsize,maxval):
        """
        生成随机数组
        :param maxsize: 数组最大长度
        :param maxval: 数组最大值
        :return:
        """
        size = random.randint(1,maxsize+1)
        res = []
        for i in range(size):
            res.append(random.randint(1,maxval))
        return res

    @staticmethod
    def copy_arr(arr):
        if not arr:
            return None
        return arr.copy()

    @staticmethod
    def is_equal(arr1,arr2):
        if (not arr1 and arr2) or  (arr1 and not arr2):
            return False
        if not arr2 and not arr1:
            return True
        if len(arr1) != len(arr2):
            return False

        for val1, val2 in zip(arr1, arr2):
            if val1 != val2:
                return False


if __name__ == '__main__':
    test_time = 500000
    max_size = 100
    max_val = 100
    succeed = True
    for i in range(test_time):
        arr1 = BubbleSort.generate_random_arr(max_size,max_val)
        arr2 = BubbleSort.copy_arr(arr1)
        BubbleSort.bubble_sort(arr1)
        BubbleSort.compareator(arr2)
        if not BubbleSort.is_equal(arr1,arr2):
            succeed = False
            break

    print("nice") if succeed else print("facking")

    arr  = BubbleSort.generate_random_arr(max_size,max_val)
    print(arr)
    print(BubbleSort.bubble_sort(arr))


