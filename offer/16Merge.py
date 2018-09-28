# 输入两个单调递增的链表，输出两个链表合成后的链表，
# 当然我们需要合成后的链表满足单调不减规则。
from offer.list_helper import *
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):

        h1Pre, h1, h2 = pHead1,pHead1, pHead2

        if not h1 :
            return h2
        if not h2:
            return h1

        if h1.val >= h2.val:  # 保证链表一的首值更小
            h1,h2 = h2,h1

        while h1 and h2:
            if h1.val > h2.val:
                temp = h2.next
                h1Pre.next,h1Pre, h2.next = h2, h2, h1
                h2 = temp
            else:
                h1Pre, h1 = h1, h1.next

        if h1 is None:
            h1Pre.next = h2

        if pHead1.val >= pHead2.val:
            return pHead2
        else:
            return pHead1


if __name__ == '__main__':
    a = LinkList([1,2,4]).get_head()
    b = LinkList([1,3,4]).get_head()
    Solution().Merge(a,b)








