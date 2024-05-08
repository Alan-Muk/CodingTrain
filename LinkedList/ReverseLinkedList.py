class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def reverseList(self, head:ListNode) -> ListNode:
		prev, curr = None, head

		while curr:
			nxt = curr.next
			curr.next = prev
			prev = curr
			cur = nxt
		return prev