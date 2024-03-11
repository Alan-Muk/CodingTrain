class ListNode:
	def __init__(self, val=0, next=None, random = None):
		self.val = val
		self.next = next
		self.random = random


class Solution:
	def copyListRandom(self, head:ListNode) -> ListNode:
		oldToCopy = { None : None}

		cur = head
		while cur:
			copy = ListNode(cur.val)
			oldToCopy[cur] = copy
			cur = cur.next

		cur = head
		while cur:
			copy = oldToCopy[cur]
			copy.next = oldToCopy[cur.next]
			copy.random = oldToCopy[cur.random]
			cur = cur.next

		return oldToCopy[head]