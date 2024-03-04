class Solution:
	def findElement(self, nums:list[int], target:int) -> list[int]:
		left = self.binarySearch(nums, target, True)
		right = self.binarySearch(nums, target, False)
		return [left, right]

		def binarySearch(nums, target, leftBias):
			l, r = 0, len(nums - 1)
			i = -1
			while l <= r:
				m = (l + r) // 2
				if target > nums[m]:
					l = m + 1
				elif target < nums[m]:
					r = m - 1
				else:
					i = m

					if leftBias:
						r = m - 1
					else:
						l = m + 1

			return i
