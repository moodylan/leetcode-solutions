from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Helper function to test the solution
def print_tree(root):
    if not root:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

# Example test case
# Tree before inversion:
#     1
#    / \
#   2   3

root = TreeNode(1, TreeNode(2), TreeNode(3))

print("Before inversion:")
print_tree(root)

sol = Solution()
inverted = sol.invertTree(root)

print("\nAfter inversion:")
print_tree(inverted)
