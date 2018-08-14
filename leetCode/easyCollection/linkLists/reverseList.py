from leetCode.easyCollection.linkLists.linklist_helper import ListNode
from leetCode.easyCollection.linkLists.linklist_helper import LinkList
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


if __name__ == '__main__':
    a = LinkList([1, 2, 3, 4, 5])
    head = Solution().reverseList(a.get_head())
