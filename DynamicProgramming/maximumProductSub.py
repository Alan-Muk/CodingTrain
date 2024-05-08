class Solution:
	def maximumProduct(self, nums:list[int]) -> int:
		res = max(nums)
		curMin, curMax = 1, 1

		for n in nums:
			if n == 0:
				curMax, curMin = 1, 1
				continue
			tmp = curMax * n
			curMax = max(n * curMax, n * curMin, n)
			curMin = min(tmp, n * curMin, n)
			res = max(CurMax, curMin, res)

		return res
