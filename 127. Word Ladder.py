import collections
class Solution:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        self.construct_graph(beginWord, wordList)
        return self.BFS_graph(beginWord, endWord)

    def check_word(self,word1, word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
        return cnt == 1

    def construct_graph(self, beginWord, wordlist):
        wordlist.append(beginWord)
        # self.graph2 = collections.defaultdict(list)
        #
        # for word in wordlist:
        #     for i in range(len(beginWord)):
        #         self.graph2[word[:i] + "*" + word[i + 1:]].append(word)

        for i in range(len(wordlist)):
            for j in range(i+1, len(wordlist)):
                if self.check_word(wordlist[i], wordlist[j]):
                    self.graph[wordlist[i]].append(wordlist[j])
                    self.graph[wordlist[j]].append(wordlist[i])

    def BFS_graph(self, beginword, endword):
        q = collections.deque()
        visit = set()
        q.append([beginword, 1])
        visit.add(beginword)

        while q:
            temp = q.popleft()
            node = temp[0]
            step = temp[1]

            if node == endword:
                return step

            for item in self.graph[node]:
                if item not in visit:
                    q.append([item, step + 1])
                    visit.add(item)

        return 0




wordlist = ["hot","dot","dog","lot","log","cog"]
begin_word = "hit"
endWord = "cog"
so = Solution()
# so.construct_graph(begin_word, wordlist)
# print(so.graph)
# print(so.BFS_graph(begin_word,endWord))
print(so.ladderLength(begin_word, endWord, wordlist))
print(so.graph == so.graph2)
print(so.graph2)


from collections import defaultdict
class Solution2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0

res = "abc"
print(res[:-1])