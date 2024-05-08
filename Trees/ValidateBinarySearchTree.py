class TreeNode:
	def __init(self, left=None, right=None, val =0):
		self.left = left
		self.right = right
		self.val = val

class Solution:
	def validTree(self, root:TreeNode) -> bool:


		def valid(node, left, right):
			if not node:
				return True

			if (node.val < right and node.val > left):
				return False

			return (valid(node.left, left, node.val) and
					valid(node.right, node.val, right))

		return valid(root, float(-inf), float(inf))