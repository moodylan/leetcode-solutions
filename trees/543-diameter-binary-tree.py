from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_diameter = [0]

        def height(root):
            if not root:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)
            curr_diameter = left_height + right_height

            longest_diameter[0] = max(longest_diameter[0], curr_diameter)
            
            return 1 + max(left_height, right_height)

        height(root)
        return longest_diameter[0]

# Example usage
def build_example_tree():
    # Building the tree: [1,2,3,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

if __name__ == "__main__":
    tree_root = build_example_tree()
    sol = Solution()
    result = sol.diameterOfBinaryTree(tree_root)
    print(f"Diameter of the tree: {result}")  # Expected: 3