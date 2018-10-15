class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead:
            return None

        pre,curr = pHead,pHead.next
        while curr:
            temp = curr.next
            curr.next = pre
            if pre is pHead:
                pre.next = None
            pre = curr
            curr = temp

        return pre


    def ReverseList2(self,pHead):
        if not pHead:
            return None

        pre,curr = pHead,pHead.next
        pre.next = None
        while curr:
            temp = curr.next
            curr.next = pre
            pre,curr = curr,temp

        return pre


