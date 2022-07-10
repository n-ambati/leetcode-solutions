# Iterative Solution
# O(N) time | O(H) space
def nodeDepthsIterative(root):
    # Write your code here.
    sum_of_depths = 0
    stack = [{'node': root, 'depth': 0}]
    while len(stack) > 0:
        node = stack.pop()
        parent_node, parent_depth = node['node'], node['depth']

        if parent_node is None:
            continue

        sum_of_depths += parent_depth
        stack.append({'node': parent_node.left, 'depth': parent_depth + 1})
        stack.append({'node': parent_node.right, 'depth': parent_depth + 1})
    return sum_of_depths


# Recursive Approach
# O(N) time | O(H) space
def nodeDepthsRecursive(root, depth=0):
    # Write your code here.
    if root is None:
        return 0
    return depth + nodeDepthsRecursive(root.left, depth+1) + nodeDepthsRecursive(root.right, depth+1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
