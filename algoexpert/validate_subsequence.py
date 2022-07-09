# Time Complexity: O(N)
# Space Complexity: O(1)
def isValidSubsequence(array, sequence):
    # Write your code here.
    i = 0
    for elem in array:
        if i == len(sequence):
            break

        if sequence[i] == elem:
            i += 1
    return i == len(sequence)
