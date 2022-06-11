# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        preorder_list = []
        nodes = []
        
        nodes.append(root)
                
        while nodes:
            
            node = nodes.pop()
            preorder_list.append(node.val)
           
            if node.right:
                nodes.append(node.right)
            
            if node.left:
                nodes.append(node.left)
                
        return preorder_list
        # Revursive solution:
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)