import collections
import copy
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        self.graph = collections.defaultdict(list)
        self.construct_graph(beginWord,wordList)
        self.q = []
        self.end_word_pos = []
        self.BFS_graph(beginWord, endWord, self.graph, self.q, self.end_word_pos)
        result = []

        for i in range(len(self.end_word_pos)):
            pos = self.end_word_pos[i]
            path = []
            while pos != -1:
                path.append(self.q[pos].node)
                pos = self.q[pos].parent_pos
            result.append([])
            temp = copy.deepcopy(path)

            for j in range(len(temp) - 1, -1, -1):
                result[i].append(path[j])
        return result

    def check_word(self,word1, word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
        return cnt == 1

    def construct_graph(self, beginWord, wordlist):

        has_begin_word = 0
        for word in wordlist:  # Because wordList may has beginWord, if we push the begin word, it will has duplicate result
            if word == beginWord:
                has_begin_word = 1
        for i in range(len(wordlist)):
            for j in range(i+1, len(wordlist)):
                if self.check_word(wordlist[i], wordlist[j]):
                    self.graph[wordlist[i]].append(wordlist[j])
                    self.graph[wordlist[j]].append(wordlist[i])
            if has_begin_word == 0 and self.check_word(beginWord, wordlist[i]): # If begin word not in wordList append it to graph
                self.graph[beginWord].append(wordlist[i])

    def BFS_graph(self, beginWord, endWord, graph, q, end_word_pos):
        visit = collections.defaultdict(int) # word and step
        min_step = 0 # min steps to the end
        self.q.append(Q_item(beginWord, -1, 1))
        visit[beginWord] = 1 # Start step is 1
        front = 0 # head pointer of queue

        while front != len(q):
            temp = self.q[front]
            node = temp.node
            step = temp.step

            if min_step != 0 and step > min_step:  # Each path to end have been finished
                break
            if node == endWord:
                min_step = step
                self.end_word_pos.append(front)  # mark index of endword

            neighbors = self.graph[node]

            for item in neighbors:
                if item not in visit or visit[item] == step+1:  # Node not be visited or another shortest path
                    self.q.append(Q_item(item, front, step+1))
                    visit[item] = step + 1  # Mark the min step to this neighbors

            front += 1  # Finish one node search




class Q_item:
    def __init__(self,node, parent_pos, step):
        self.node = node
        # self.pos = pos
        self.parent_pos = parent_pos
        self.step = step

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

so = Solution()
print(so.findLadders(beginWord,endWord,wordList))



