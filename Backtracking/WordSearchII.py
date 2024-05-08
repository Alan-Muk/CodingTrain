class TrieNode:
	def __init__(self):
		self.children = {}
		self.isWord = False

	def addWord(self, word):
		cur = self
		for c in word:
			if c not in cur.children:
				cur.children[c] = TrieNode()
			cur.children[c]
		cur.isWord = True

class Solution:
	def findWords(self, board:list[list[str]], words:list[str]) -> list[str]:
		root = TrieNode()

		for w in words:
			root.addWord(w)

		Rows, Cols = len(board), len(board[0])
		res, visit = set(), set()

		def dfs(r, c, node, word):
			if (r < 0 or c < 0 or r == Rows or c == Cols or (r,c) in visit or board[r][c] not in node.children):
				return

			visit.add((r,c))
			node = node.children[board[r][c]]
			word += board[r][c]
			if node.isWord:
				res.add(word)

			dfs(r - 1, c, word)
			dfs(r + 1, c, word)
			dfs(r, c + 1, word)
			dfs(r, c - 1, word)	

			visit.remove((r, c))

		for r in range(Rows):
			for c in range(Cols):
				dfs(r, c, root, "")

		return list(res)

