class Solution:
	def maxProdsub(self, nums:list[int]) -> int:
		res = max(nums)
		curMin, curMax = 1, 1

		for n in nums:
			if n == 0:
				curMin, curMax = 1, 1
				continue
			tmpMax = curMax
			curMax = max(n * curMax, n * curMin, n)
			curMin = min(n * tmpMax, n * curMin, n)
			res = max(res, curMax, curMin)

		return res