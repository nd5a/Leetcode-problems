# Convert Binary number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head):
        current_number = 0
        current_node = head

        while current_node is not None:
            current_number *= 2
            current_number += current_node.val
            current_node = current_node.next
        return current_number