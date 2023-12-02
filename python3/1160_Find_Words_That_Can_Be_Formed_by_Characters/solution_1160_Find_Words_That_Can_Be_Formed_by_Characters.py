class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = collections.defaultdict(int)
        result = 0

        for c in chars: d[c] += 1

        for word in words:
            d_copy, can_be_formed  = d.copy(), True
            for char in word:
                if char in d_copy:
                    if d_copy[char] == 0:
                        can_be_formed = False
                        break
                    d_copy[char] -= 1
                else:
                    can_be_formed = False
                    break
            if can_be_formed: result += len(word)
        return result