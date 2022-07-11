# Time Complexity: O(NlogN)
# Space Complexity: O(1)
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if blueShirtHeights[0] < redShirtHeights[0]:
        front = blueShirtHeights
        back = redShirtHeights
    elif redShirtHeights[0] < blueShirtHeights[0]:
        front = redShirtHeights
        back = blueShirtHeights
    else:
        return False
    for i in range(1, len(front)):
        if back[i] <= front[i]:
            return False
    return True
