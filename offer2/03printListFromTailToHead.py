class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []

        res =[]
        while listNode:
            res.append(listNode.val)
            listNode = listNode.next

        return res[::-1]