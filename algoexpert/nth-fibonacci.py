# O(n) time | O(1) space
def getNthFib(n):
    # Write your code here.
    if n == 1:
        return 0
    if n == 2:
        return 1
    prev, current = 0, 1
    for i in range(3, n+1):
        new_value = prev + current
        prev = current
        current = new_value
    return current
