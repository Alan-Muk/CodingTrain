class Solution:
	def dailyTemperatures(self, temperatures:list[int]) -> list[int]:
		res = [0] * len(temperatures)
		stack = []

		for i, t in enumerate(temperatures):
			while stack and t > stack[-1][0]:
				stackT, stackInd = stack.pop()
				res[stackInd] = (i - stackInd)
			stack.append([t, i])

		return res