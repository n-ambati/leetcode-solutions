# Time Complexity: O(N)
# Space Complexity: O(1)
def sortedSquaredArray(array):
    # Write your code here.
    sorted_squared_array = []
    l, r = 0, len(array) - 1

    while l <= r:
        left = abs(array[l])
        right = abs(array[r])
        if left > right:
            sorted_squared_array.append(left * left)
            l += 1
        else:
            sorted_squared_array.append(right * right)
            r -= 1
    sorted_squared_array.reverse()
    return sorted_squared_array
