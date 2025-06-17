"""
LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a BST, find the lowest common ancestor (LCA) of two given nodes in the BST.
"""
# note: other correct solutions like iterative or using parent pointers can be considered

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p and q are in the left subtree, go left
          if p.val < root.val and q.val < root.val:
              return self.lowestCommonAncestor(root.left, p, q)
          # if p and q are in the right subtree go right 
          if p.val > root.val and q.val > root.val:
              return self.lowestCommonAncestor(root.right, p, q)
          return root

if __name__ == "__main__":
    # Construct BST from example 1 leetcode
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    p = root.left              # Node with val 2
    q = root.right             # Node with val 8

    sol = Solution()
    lca = sol.lowestCommonAncestor(root, p, q)
    print("LCA:", lca.val)     # Output should be 6
