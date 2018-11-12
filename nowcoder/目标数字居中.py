# 给定一个数组arr，和一个数num，请把小于等于num的数放在数
# 组的左边，大于num的数放在数组的右边。

class NumCentre:
    @staticmethod
    def num_centre(arr,num):
        if not arr or num not in arr:
            return arr

        min_index = -1
        for i in range(len(arr)):
            if arr[i] <= num:
                min_index += 1
                arr[i],arr[min_index] = arr[min_index],arr[i]
        return arr

if __name__ == '__main__':
    print(NumCentre.num_centre([9, 5, 3, 6, 7], 6))




