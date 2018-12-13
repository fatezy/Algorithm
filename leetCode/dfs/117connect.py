# 给定一个二叉树
#
# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
#
# 说明:
#
# 你只能使用额外常数空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
# 示例:
#
# 给定二叉树，
#
#      1
#    /  \
#   2    3
#  / \    \
# 4   5    7
# 调用你的函数后，该二叉树变为：
#
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \    \
# 4-> 5 -> 7 -> NULL


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root): # 广度优先遍历
        node_list = []
        if  root:
            node_list.append(root)
        while node_list:
            temp_list = node_list[::]
            node_list = []
            for i in range(len(temp_list)-1):
                temp_list[i].next = temp_list[i+1]
            for i in range(len(temp_list)):
                if temp_list[i].left:
                    node_list.append(temp_list[i].left)
                if temp_list[i].right:
                    node_list.append(temp_list[i].right)
