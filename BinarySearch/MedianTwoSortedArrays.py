class Solution:
	def median(self, nums1:list[int], nums2:list[int]) -> float:
		
		A,B = nums1, nums2
		total = len(A) + len(B)
		half = total // 2

		if len(B) < len(A):
			A, B = B, A

		l, r = 0, len(A) - 1
		while True:
			i = (l + r) // 2 #A
			j = half - i - 2 #B

			Aleft = A[i] if i >= 0 else ("-inf")
			Aright = A[i + 1] if (i + 1) < len(A) else ("inf")
			Bleft = B[j] if j >= 0 else ("-inf")
			Bright = B[j + 1] if (j + 1) < len(B) else ("inf")

			if Aleft <= Bright and Bleft <= Aright:
				#odd
				if total % 2:
					return min(Aright, Bright)
				#even
				return max(Aleft, Bleft) + min(Aright, Bright) // 2
			elif Aleft > Bright:
				r = i - 1
			else:
				l = i + 1