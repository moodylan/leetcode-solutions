from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Example usage
def print_tree(root):
    if not root:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

# Example test cases
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

print("Tree 1:")
print_tree(root1)
print("\nTree 2:")
print_tree(root2)

sol = Solution()
print("\nMaximum depth of Tree 1:", sol.maxDepth(root1))
print("Maximum depth of Tree 2:", sol.maxDepth(root2))
