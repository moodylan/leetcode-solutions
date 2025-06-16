from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Helper function to run tests
def run_test(p: Optional[TreeNode], q: Optional[TreeNode], expected: bool, label: str = ""):
    solution = Solution()
    result = solution.isSameTree(p, q)
    print(f"{label}Result: {result} | Expected: {expected} | {'✅' if result == expected else '❌'}")
    
# TEST CASES

# Test 1: Same Tree
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
run_test(p1, q1, expected=True, label="Test 1 - Same structure & values: ")

# Test 2: Different structure
p2 = TreeNode(1, TreeNode(2))
q2 = TreeNode(1, None, TreeNode(2))
run_test(p2, q2, expected=False, label="Test 2 - Different structure: ")

# Test 3: Same structure, different values
p3 = TreeNode(1, TreeNode(2), TreeNode(1))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))
run_test(p3, q3, expected=False, label="Test 3 - Different values: ")

# Test 4: Both trees are empty
run_test(None, None, expected=True, label="Test 4 - Both trees empty: ")

# Test 5: One tree is empty
p5 = TreeNode(1)
run_test(p5, None, expected=False, label="Test 5 - One tree empty: ")
