class Solution:
	def validParenth(self, s:str) -> bool:
		stack = []
		closeToOpen = { ")":"(", "]":"[", "}":"{" }

		for c in s:
			if c in closeToOpen:
				if stack and stack[-1] == closeToOpen[c]:
					stack.pop(c)
				else:
					return False
			else:
				stack.append(c)
				
		return True if not stack else False
