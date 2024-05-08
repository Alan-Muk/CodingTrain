class Solution:
	def findBinaryString(self, nums:list[str]) -> str:
		strSet = {s for s in nums}

		def backtrack(i, cur):
			if i == len(nums):
				res = "".join(cur)
				return None if res in strSet else res

			backtrack(i + 1, cur)
			if res: return res

			cur[i] = "1"
			backtrack(i +  1, cur)
			if res: return res


		return backtrack(0,["0" for s in nums])