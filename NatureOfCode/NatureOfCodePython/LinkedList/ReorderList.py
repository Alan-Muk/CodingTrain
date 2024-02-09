class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def reorder(self, head:ListNode) -> None:
		slow, fast = head, head.next

		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		second = slow.next
		prev = slow.next = None

		while second:
			tmp = second.next
			second.next = prev
			second = tmp
		
		first, second = head, prev
		
		while second:
			tmp1, tmp2 = first.next, second.next
			first.next = second
			second.next = tmp1
			first, second = tmp1, tmp2