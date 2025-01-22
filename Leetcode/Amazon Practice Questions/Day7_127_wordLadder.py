from collections import deque,defaultdict
class Solution:
    def ladderLength(self, beginWord, endWord, wordList) -> int:
        if(endWord not in wordList):
            return 0
        graph=defaultdict(list)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                pattern=wordList[i][:j]+"*"+wordList[i][j+1:]
                graph[pattern].append(wordList[i])
        visited=set([beginWord])
        queue=deque([beginWord])
        res=1
        while(queue):
            for i in range(len(queue)):
                word=queue.popleft()
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for k in graph[pattern]:
                        if(k==endWord):
                            return res+1
                        if(k not in visited):
                            visited.add(k)
                            queue.append(k)
            res+=1
        return 0
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
sol=Solution()
print(sol.ladderLength(beginWord,endWord,wordList))

'''
Time Complexity:
    Graph Construction:For each word of length L in the wordList (including beginWord), the program generates L patterns by replacing each character with a *.
        For n words in wordList, the graph construction takes O(n⋅L).
    BFS Traversal: BFS explores each word (node) in the worst case.
        For each word, it generates L patterns, and for each pattern, it checks all connected words.
        Therefore, BFS traversal takes O(n⋅L) in the worst case.
    Overall Time Complexity: O(n⋅L).
'''