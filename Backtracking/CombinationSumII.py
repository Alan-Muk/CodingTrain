class Solution:
	def combination(self, candidates:list[int], target:int) -> list[list[int]]:
		candidates.sort()

		res = []

		def backtrack(cur, pos, target):
			if target == 0:
				res.append(cur.copy())
			if target <=0:
				return

			prev = -1
			for i in range(pos,len(candidates)):
				if candidates[i] == prev:
					continue

				cur.append(candidates[i])
				backtrack(cur, i + 1, target- candidates[i])
				cur.pop()

				prev = candidates[i]

		backtrack([], 0, target)
		return res