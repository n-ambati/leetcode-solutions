# O(nlogn) time | O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    if fastest:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reverse=True)
    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
    total_speed = 0
    for i in range(len(redShirtSpeeds)):
        total_speed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return total_speed
