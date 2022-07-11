# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    trav = linkedList
    while trav is not None and trav.next is not None:
        if trav.value == trav.next.value:
            trav.next = trav.next.next
            continue
        trav = trav.next
    return linkedList
