# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
import heapq
from offer.list_helper import *
class Solution:

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        n = len(lists)
        p = lists[0]
        i = 0
        res = []
        while i < n:
            p = lists[i]
            while p != None:
                res.append(p.val)
                p = p.next
            i += 1
        res.sort()
        head = ListNode(-1)
        p = head
        for i in res:
            p.next = ListNode(i)
            p = p.next
        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val

        heap = []
        for arr in lists:
            if arr:
                heap.append((arr.val, arr))
        heapq.heapify(heap)

        dummy = ListNode(None)
        cur = dummy
        while heap:
            value, popNode = heapq.heappop(heap)
            cur.next = popNode
            cur = cur.next
            if popNode.next:
                heapq.heappush(heap, (popNode.next.val, popNode.next))
        return dummy.next



if __name__ == '__main__':
    a = LinkList([1, 2, 3])
    b = LinkList([1, 3, 5])
    c = LinkList([1, 2, 4])
    lists = [a.get_head(),b.get_head(),c.get_head()]
    Solution().mergeKLists(lists)