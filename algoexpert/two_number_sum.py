# Time Complexity: O(N)
# Space Complexity: O(N)
def twoNumberSum(array, targetSum):
    # Write your code here.
    diff = {}
    for elem in array:
        if elem in diff:
            return [diff[elem], elem]
        diff[targetSum - elem] = elem

    return []
