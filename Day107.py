# Recover a Tree From Preorder Traversal


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def recoverFromPreorder(self, traversal):
        stack = []
        current = 0

        def get_value():
            val = 0
            nonlocal current
            while current < len(traversal) and traversal[current].isnumeric():
                val *= 10
                val += int(traversal[current])
                current += 1
            return val 

        root = TreeNode(get_value())
        stack.append(root)

        while current < len(traversal):
            dashes = 0
            # Count the Dashes
            while traversal[current] == "-":
                dashes += 1
                current += 1
            assert(dashes > 0)
            val = get_value()
            while dashes < len(stack):
                stack.pop()
            
            p = stack[-1]
            node = TreeNode(val)
            if p.left is None:
                p.left = node
            elif p.right is None:
                p.right = node
            else:
                assert(False)
            stack.append(node)
        return root