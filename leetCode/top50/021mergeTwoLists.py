# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
from offer.list_helper import *

class Solution:
    def mergeTwoLists(self, pHead1, pHead2):

        newHead,p1,p2 = ListNode(-1),pHead1,pHead2
        newHead_temp = newHead
        while p1 and p2:
            if p1.val < p2.val:
                newHead.next = p1
                p1 = p1.next
                newHead = newHead.next
            else:
                newHead.next = p2
                p2 = p2.next
                newHead =newHead.next

        while p1:
            newHead.next = p1
            p1 = p1.next
            newHead = newHead.next


        while p2:
            newHead.next = p2
            p2 = p2.next
            newHead = newHead.next

        return newHead_temp.next






