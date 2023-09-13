class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        def word_break_rec(s, start, current_word):
            nonlocal result
            nonlocal wordDict
            if start == len(s) and current_word:
                result.append(' '.join(current_word))
            for i in range(start, len(s)):
                word = s[start: i + 1]
                if word in wordDict:
                    current_word.append(word)
                    word_break_rec(s, i + 1, current_word)
                    current_word.pop()

        word_break_rec(s, 0, [])
        return result