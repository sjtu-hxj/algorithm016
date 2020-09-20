"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        ret = []
        q = [root]
        while q:
            l = []
            v = []
            for x in q:
                l += x.children
                v.append(x.val)
            ret.append(v)
            q = l
        return ret