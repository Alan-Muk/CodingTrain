class Node:
	def __init__(self, val=0, neighbours = None):
		self.val = val
		self.neighbours = neighbours if neighbours is not None else []

class Solution:
	def cloneGraph(self, node:'Node') -> 'Node':
		oldToNew = {}

		def dfs(node):
			if node in oldToNew:
				return oldToNew[node]

			copy = Node(node.val)
			oldToNew[node] = copy
			for nei in node.neighbours:
				copy.neighbours.append(dfs(nei))
			return copy

		return dfs(node) if node else None