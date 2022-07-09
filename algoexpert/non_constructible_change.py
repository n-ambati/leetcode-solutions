# Time Complexity: O(NlogN)
# Space Complexity: O(1)
def nonConstructibleChange(coins):
    # Write your code here.
    change = 0
    coins.sort()

    for coin in coins:
        if coin > change + 1:
            break
        change += coin

    return change + 1
