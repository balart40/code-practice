class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = dict()
        phone["2"] = ["a","b","c"]
        phone["3"] = ["d","e","f"]
        phone["4"] = ["g","h","i"]
        phone["5"] = ["j","k","l"]
        phone["6"] = ["m","n","o"]
        phone["7"] = ["p","q","r","s"]
        phone["8"] = ["t","u","v"]
        phone["9"] = ["w","x","y","z"]

        result = []
        if not digits:
            return result
        def my_back_track(curr_combination, curr_digits):
            if not curr_digits:
                result.append(curr_combination)
                return
            else:
                for letter in phone[curr_digits[0]]:
                    my_back_track(curr_combination + letter, curr_digits[1:])

        my_back_track("", digits)
        return result