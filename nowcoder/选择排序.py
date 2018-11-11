class SelectSort:
    @staticmethod
    def select_sort(arr):
        if not arr:
            return []
        for i in range(len(arr)-1):
            min_index = i
            for j in range(i,len(arr)):
                min_index = j if arr[j] < arr[min_index] else min_index
            arr[i],arr[min_index] = arr[min_index],arr[i]
        return arr



if __name__ == '__main__':
    print(SelectSort.select_sort([212, 3, 11, 1244]))