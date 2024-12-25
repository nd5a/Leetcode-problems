# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root):
        INF = 10 ** 20
        best = []
        def traverse(node, level):
            if node is None:
                return
            if level >= len(best):
                best.append(-INF)
            
            best[level] = max(best[level], node.val)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
        
        traverse(root, 0)
        return best