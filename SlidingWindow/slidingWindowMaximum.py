class Solution:
	def maxWindow(self, nums:list[int], k:int) -> list[int]:
		output = []
		l = r = 0
		q = collections.deque()

		while r < len(nums):
			while q and q[-1] < nums[r]:
				q.pop()
			q.append(r)

			if l > q[0]:
				q.popleft()

			if (r + l) >= k:
				output.append(nums[q[0]])
				l += 1
			r += 1

		return output