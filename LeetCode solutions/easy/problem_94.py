# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        inorder_list = []
        stack = []
        pointer = root

        while pointer or stack:
            while pointer:
                stack.append(pointer)
                pointer = pointer.left
            pointer = stack.pop()
            inorder_list.append(pointer.val)
            pointer = pointer.right

        return inorder_list

# Recursive Solution:

#         def traverse_in_order(root):
#             if not root:
#                 return

#             traverse_in_order(root.left)

#             inorder_list.append(root.val)

#             traverse_in_order(root.right)

#         traverse_in_order(root)
#         return inorder_list
