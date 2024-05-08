class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def removeNthNode(self, head:ListNode, n:int) -> ListNode:
		dummy = ListNode(0, head)
		left = dummy
		right = head

		while n > o and right:
			rigit = right.next
			n -= 1

		while right:
			left = left.next
			right = right.next

		left.next = left.next.next
		return dummy.next