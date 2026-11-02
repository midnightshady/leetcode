# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        current = head
        last = dummy
        count = 1
        prevDest = 0

        while current:
            dest = count
            temp = current

            # Actual group length count karo
            while dest > 0 and temp:
                temp = temp.next
                dest -= 1

            actual = count - dest

            if actual % 2 == 0:
                prev = None
                remb = current
                temp = 0

                while temp < actual:
                    nextNode = current.next
                    current.next = prev
                    prev = current
                    current = nextNode
                    temp += 1

                last.next = prev
                remb.next = current
                last = remb

            else:
                while current != temp:
                    last = current
                    current = current.next

            prevDest += actual
            count += 1

        return dummy.next