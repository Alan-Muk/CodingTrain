class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def IsPalindrome(self, head:ListNode) -> bool:
		# nums = []

		# while head:
		# 	nums.append(head.val)
		# 	head = head.next

		# l, r = 0, len(nums) - 1

		# while l < r:
		# 	if nums[l] != nums[r]:
		# 		return False
		# 		l += 1
		# 		r -= 1

		# return True


		fast, slow = head, head

		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next

		prev = None
		while slow:
			tmp = slow.next
			slow.next = prev
			prev = slow
			slow = tmp

		left, right = head, prev
		while right:
			if left.val != right.val:
				return False
			left = left.next
			right = right.next

		return True