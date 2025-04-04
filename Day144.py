# Lowest Common Ancestor of Deepest Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root):
        max_depth = 0
        deepest = set()

        def traverse(node, depth):
            if node is None:
                return
            
            if node.left is None and node.right is None:
                nonlocal deepest
                nonlocal max_depth
                if depth > max_depth:
                    deepest = set()
                    max_depth = depth
                if depth == max_depth:
                    deepest.add(node.val)

            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)
        traverse(root, 0)
        found = None
        def find(node):
            if node is None:
                return 0
            
            nonlocal found
            if node.val in deepest:
                if len(deepest) == 1 and found is None:
                    found = node
                return 1
            left_count = find(node.left)
            right_count = find(node.right)

            if left_count + right_count == len(deepest) and found is None:
                found = node
            return left_count + right_count
        find(root)
        return found
