# Time Complexity: O(N) where N is the total nodes in the tree
# Space Complexity: O(H) where H is the height of the tree.
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    branch_sums = []
    preorder_traversal(root, branch_sums, 0)
    return branch_sums


def preorder_traversal(root, branch_sums, current_sum):
    if root is None:
        return
    if root.left is None and root.right is None:
        current_sum += root.value
        branch_sums.append(current_sum)
        return

    current_sum += root.value
    preorder_traversal(root.left, branch_sums, current_sum)
    preorder_traversal(root.right, branch_sums, current_sum)
