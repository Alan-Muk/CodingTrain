class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def removeElement(self, head:ListNode, val:int) -> ListNode:
		dummy = ListNode(next = head)
		prev, curr = dummy, head

		while curr:
			nxt = curr.next

			if curr.val == val:
				prev.next = nxt
			else:
				prev = curr

			curr = nxt

		return dummy.next
		