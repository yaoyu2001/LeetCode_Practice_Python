# Hint 1 You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
# Hint 2 If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie?
# If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

class Solution:
    def findWords(self, board: [[str]], words: [str]) -> [str]:

        # 1 Build a trie construction
        # Mark end
        WORD_KEY = '$'

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                    node = node[letter]
                else:

                    node = node[letter]

            node[WORD_KEY] = word

        print(trie)

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):

            letter = board[row][col]
            cur_node = parent[letter]

            # check if we find a match word
            word_match = cur_node.pop(WORD_KEY, False)
            if word_match:
                # Find word also pop it to avoid duplicates
                matchedWords.append(word_match)

            # Set the cell as visited
            board[row][col] = "#"

            for (row_offset, col_offset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row, new_col = row + row_offset, col + col_offset
                if new_row < 0 or new_row >= rowNum or new_col < 0 or new_col >= colNum:
                    continue
                if not board[new_row][new_col] in cur_node:
                    continue
                backtracking(new_row, new_col, cur_node)

            # BackTracking
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not cur_node:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords



board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
words2 = ["oath","dig","dog","dogs"]

so = Solution()
print(so.findWords(board, words))
# Hint 1 You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
# Hint 2 If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie?
# If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

class Solution:
    def findWords(self, board: [[str]], words: [str]) -> [str]:

        # 1 Build a trie construction
        # Mark end
        WORD_KEY = '$'

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                    node = node[letter]
                else:

                    node = node[letter]

            node[WORD_KEY] = word

        print(trie)

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):

            letter = board[row][col]
            cur_node = parent[letter]

            # check if we find a match word
            word_match = cur_node.pop(WORD_KEY, False)
            if word_match:
                # Find word also pop it to avoid duplicates
                matchedWords.append(word_match)

            # Set the cell as visited
            board[row][col] = "#"

            for (row_offset, col_offset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row, new_col = row + row_offset, col + col_offset
                if new_row < 0 or new_row >= rowNum or new_col < 0 or new_col >= colNum:
                    continue
                if not board[new_row][new_col] in cur_node:
                    continue
                backtracking(new_row, new_col, cur_node)

            # BackTracking
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not cur_node:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords



board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
words2 = ["oath","dig","dog","dogs"]

so = Solution()
print(so.findWords(board, words))
