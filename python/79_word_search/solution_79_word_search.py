class Solution(object):
    counter = 0
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.get_words(board, word, i, j, visited):
                    # counter += 1
                    return True
        return False

    def get_words(self, board, word, i, j, visited, pos = 0):
        if pos == len(word):
            return True

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i, j)) or word[pos] != board[i][j]:
            return False

        visited[(i, j)] = True
        res = self.get_words(board, word, i, j + 1, visited, pos + 1) \
              or self.get_words(board, word, i, j - 1, visited, pos + 1) \
              or self.get_words(board, word, i + 1, j, visited, pos + 1) \
              or self.get_words(board, word, i - 1, j, visited, pos + 1)
        visited[(i, j)] = False

        return res