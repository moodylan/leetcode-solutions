from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot): 
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p and not q: 
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
      
# Optional helper to build tree from list (leetcode-like format)
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

# TEST CASES

solution = Solution()

# Example 1
root1 = build_tree([3,4,5,1,2])
subRoot1 = build_tree([4,1,2])
print(f"Test 1: {solution.isSubtree(root1, subRoot1)}  # Expected: True")

# Example 2
root2 = build_tree([3,4,5,1,2,None,None,None,None,0])
subRoot2 = build_tree([4,1,2])
print(f"Test 2: {solution.isSubtree(root2, subRoot2)}  # Expected: False")

# Example 3
root3 = build_tree([1,1])
subRoot3 = build_tree([1])
print(f"Test 3: {solution.isSubtree(root3, subRoot3)}  # Expected: True")