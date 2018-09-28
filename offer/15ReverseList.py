# 输入一个链表，反转链表后，输出新链表的表头。


from offer.list_helper import *


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        """
        双指针法
        :param pHead:
        :return:
        """

        if not pHead:
            return
        pre,curr = pHead,pHead.next
        while curr:
            temp = curr.next
            curr.next = pre
            if pre is pHead:
                pre.next = None
            pre = curr
            curr = temp

        return pre


if __name__ == '__main__':
    Solution().ReverseList(LinkList([1, 2, 3, 4, 5]).get_head())




