# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 说明:
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

from offer.list_helper import *
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(-1)
        newHead.next = head
        pre = newHead
        while head and head.next:
            pre.next,pre.next.next,pre.next.next.next= pre.next.next,pre.next,pre.next.next.next
            # pre.next,pre.next.next= pre.next.next,pre.next
            pre = pre.next.next

            head = head.next

        return newHead.next

    def swapPairs2(self, head):
        p1 = guard = ListNode(0)
        guard.next = head

        try:
            while True:
                p0, p1, p2 = p1, p1.next, p1.next.next
                p0.next, p1.next, p2.next = p2, p2.next, p1
        except:
            return guard.next

    def swapPairs3(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


    def swapPairs4(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            # a = pre.next
            # b = a.next
            # pre.next, pre.next.next.next,  pre.next.next = pre.next.next, pre.next, pre.next.next.next
            pre.next, pre.next.next.next = pre.next.next, pre.next
            pre = pre.next
        return self.next

if __name__ == '__main__':
    a = LinkList([1,2,3])
    Solution().swapPairs(a.get_head())

