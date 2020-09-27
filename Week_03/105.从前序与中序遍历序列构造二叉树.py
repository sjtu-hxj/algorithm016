# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         def build(stop):
#             if not inorder or inorder[-1] == stop:
#                 return None
#             # if preorder:
#             root_val = preorder.pop()
#             root = TreeNode(root_val)
#             root.left = build(root_val)
#             inorder.pop()
#             root.right = build(stop)
#             return root

#         preorder.reverse()
#         inorder.reverse()
#         return build(None)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop):
            if not inorder or inorder[0] == stop:
                return None
            # if preorder:
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            root.left = build(root_val)
            inorder.pop(0)
            root.right = build(stop)
            return root

        # preorder.reverse()
        # inorder.reverse()
        return build(None)