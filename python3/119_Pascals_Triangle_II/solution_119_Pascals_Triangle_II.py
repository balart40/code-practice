class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            curr_lst = [1, 1]
            for j in range(1, rowIndex):
                result = []
                n = len(curr_lst)
                for i in range(n):
                    if i == 0:
                        result.insert(0, 1)
                    if i + 1 < n:
                        result.append(curr_lst[i]+ curr_lst[i +1])
                    else:
                        result.append(1)
                curr_lst = result
            return curr_lst
