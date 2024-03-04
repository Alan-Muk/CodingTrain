class Solution:
	def searchinsert(self, nums:list[int], target:int) -> int:
		l, r = 0, len(nums) -1

		while l <= r:
			m = (l + r) // 2

			if nums[m] == target:
				return m
			if target > nums[m]:
				l = m + 1
			else:
				r = m - 1

		return l