# 是否能组成顺子，大小王为0，可以替代任何值

class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numbers.sort()
        king = numbers.count(0)
        while 0 in numbers:
            numbers.remove(0)
        temp = numbers[0]

        i = 0
        while i<len(numbers):
            if temp !=numbers[i]:
                if king!=0:
                    king -= 1
                    temp += 1
                else:
                    return False
            else:
                temp+=1
                i+=1
        return True


if __name__ == '__main__':
    print(Solution().IsContinuous([1,0,0,5,0]))