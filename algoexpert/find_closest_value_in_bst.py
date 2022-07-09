# Time Complexity: O(H) where H is the height of the tree
# Space Complexity: O(1)
def findClosestValueInBst(tree, target):
    # Write your code here.
    trav = tree

    if trav is None:
        return None

    delta = abs(trav.value - target)
    closest_value = trav.value
    while trav is not None:
        if abs(trav.value - target) < delta:
            closest_value = trav.value
            delta = abs(trav.value - target)
        if trav.value == target:
            break
        elif trav.value > target:
            trav = trav.left
        else:
            trav = trav.right
    return closest_value


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
