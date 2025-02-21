# Find Elements in a Contaminated Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root):
        self.seen = set()

        def traverse(node, current):
            self.seen.add(current)

            if node.left is not None:
                traverse(node.left, current * 2 + 1)
            if node.right is not None:
                traverse(node.right, current * 2 + 2)
        traverse(root, 0)

    def find(self, target):
        return target in self.seen

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)