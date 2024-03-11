class TrieNode:
	def __init__(self):
		self.children = {}
		self.isEnd = False

	def addWord(self, word:str):
		cur = self
		for c in word:
			if c not in cur.children:
				cur.children[c] = TrieNode()
			cur = cur.children[c]
		cur.isEnd = True

class Solution:
	def wordSearchII(self, board:list[list[str]], words:list[str]) -> list[str]:
		root = TrieNode()

		for w in words:
			root.addWord(w)

		ROWS, COLS = len(board), len(board[0])
		res, visit = set(), set()

		def dfs(r, c, node, word):
			if (r < 0 or c < 0 or 
				r == ROWS or c == COLS or 
				(r, c) in visit or board[r][c] not in node.children) :
				return

			visit.add((r, c))
			node = node.children[board[r][c]]
			word += board[r][c]
			if node.isEnd:
				res.add(word)

			dfs(r + 1, c, node, word)
			dfs(r - 1, c, node, word)
			dfs(r, c + 1, node, word)
			dfs(r, c - 1, node, word)


			for r in range(ROWS):
				for c in range(COLS):
					dfs(r, c, root, "")
			return list(res)

			visit.remove((r, c))