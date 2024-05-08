class Solution:
	def permute(self, nums:list[int]) -> list[list[int]]:
		res = []
		perm = []

		count = { n:0 for n in mums }
		for n in nums:
			count[n] += 1

		def dfs():
			if len(perm) == len(nums):
				res.append(perm[:])
				return

			for n in count:
				if count[n] > 0:
					perm.append(n)
					count[n] -= 1

					dfs()

					count[n] += 1
					perm.pop()

		dfs()
		return res
