class Solution:
	def asteroidCollision(self, asteroids:list[int]) -> list[int]:
		stack = []

		for a in asteroids:
			while  stack and a < 0 and stack[-1]:
				diff = a + stack[-1]
				if diff < 0:
					stack.pop()
				elif diff > 0:
					a = 0
				else:
					a = 0
					stack.pop()

			if a:
				stack.append(a)

		return stack