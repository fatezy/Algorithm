# 复杂链表的复制
import copy
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None



class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None

        listmap = {}
        temp = pHead
        newHead = RandomListNode(temp.label)
        newTemp = newHead
        listmap[temp] = newTemp
        while temp.next:
            newTemp.next = RandomListNode(temp.next.label)
            temp = temp.next
            newTemp =newTemp.next
            listmap[temp] = newTemp


        temp = pHead
        newTemp = newHead

        while temp:
            newTemp.random = listmap.get(temp.random)
            newTemp = newTemp.next
            temp = temp.next


        return newHead


    def Clone2(self, pHead):
        chead=copy.deepcopy(pHead)
        return chead


if __name__ == '__main__':
    head = RandomListNode(1)
    head.next = RandomListNode(2)
    head.next.next = RandomListNode(3)
    head.next.next.next = RandomListNode(4)
    head.next.next.next.next = RandomListNode(5)

    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next
    head.next.next.next.random = head
    head.next.next.next.next.random = head


    Solution().Clone(head)






