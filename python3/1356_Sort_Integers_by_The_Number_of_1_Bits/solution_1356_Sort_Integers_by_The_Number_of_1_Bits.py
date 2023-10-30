class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        tuple_arr = []
        while arr:
            curr_num = arr.pop()
            tuple_arr.append((curr_num, bin(curr_num).count('1')))
        tuple_arr.sort(key=lambda x: (x[1], x))
        return [ x[0] for x in tuple_arr]