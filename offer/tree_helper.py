class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class biTree:
    def __init__(self,list):
        self.list = list


    def creatTree(self,root,i):
        if i<len(self.list):
            if self.list[i] =='#':
                return None
            else:
                root = TreeNode(self.list[i])
                root.left = self.creatTree(root.left,2*i+1)
                root.right = self.creatTree(root.left,2*i+2)
                return root
        return root

    def levelOrder(self, root):
        if not root:
            return []

        queue = [root]
        results = []
        while queue:
            next_queue = []
            results.append([node.val for node in queue])
            for node in queue:

                # 加一层检验是否为最后一层
                flag = True   # 为True时，不是最后一层
                for node2 in queue:
                    if node2.left or node2.right:
                        flag = False
                if flag:       # 是最后一层即结束
                    break

                if node.left:
                    next_queue.append(node.left)
                if not node.left:
                    next_queue.append(TreeNode('#'))

                if node.right:
                    next_queue.append(node.right)
                if not node.right:
                    next_queue.append(TreeNode('#'))

            queue = next_queue

        return results






    def creat(self):
        return self.creatTree(None,0)

if __name__ == '__main__':
    tree = biTree([1,2,3,'#',4,5,6])
    root = tree.creat()
    print(tree.levelOrder(root))





