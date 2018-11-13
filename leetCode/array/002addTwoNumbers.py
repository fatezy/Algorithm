# 给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
from leetCode.linklist.list_helper import *
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)  # 头结点
        curr = res
        add = 0 # 进位数
        while l1 and l2:
            if l1.val+l2.val+add>9:
                curr.next = ListNode(l1.val+l2.val+add-10)
                add = 1
            else:
                curr.next = ListNode(l1.val + l2.val + add)
                add = 0
            curr,l1,l2 = curr.next,l1.next,l2.next

        while l1:
            if add+l1.val>9:
                curr.next = ListNode(l1.val+add-10)
                add = 1
            else:
                curr.next = ListNode(l1.val+add)
                add = 0
            curr = curr.next
            l1 = l1.next

        while l2:
            if add+l2.val>9:
                curr.next = ListNode(l2.val+add-10)
                add = 1
            else:
                curr.next = ListNode(l2.val+add)
                add = 0
            curr = curr.next
            l2 = l2.next

        if add == 1:
            curr.next = ListNode(1)
            curr = curr.next

        return res.next



if __name__ == '__main__':
    a = LinkList([2,4, 3])
    b = LinkList([5,6,4])
    Solution().addTwoNumbers(a.head,b.head)






