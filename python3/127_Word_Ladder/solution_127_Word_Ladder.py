class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        letters_to_choose_from = set(''.join(wordList))
        steps = 1
        queue = collections.deque()
        queue.append((beginWord, steps))

        while queue:
            word, steps = queue.popleft()
            for i in range(len(beginWord)):
                for char in letters_to_choose_from:
                    new_word = word[:i] + char + word[i+1:]
                    if new_word == endWord:
                        return steps + 1
                    if new_word in wordList:
                        queue.append((new_word, steps + 1))
                        wordList.remove(new_word)
        return 0