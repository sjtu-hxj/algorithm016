# N叉树迭代方法
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        s = [root]
        # s.append(root)
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            # for child in node.children[::-1]:
            #     s.append(child)
#            s.extend(node.children[::-1])
            s.extend(reversed(node.children))    ## 实现倒顺的两种方式，[::-1] 或者 reversed
        return res