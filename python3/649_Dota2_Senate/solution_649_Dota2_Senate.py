class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        idx_d_arr = []
        idx_r_arr = []

        for i in range(n):
            if senate[i] == 'R':
                idx_r_arr.append(i)
            elif senate[i] == 'D':
                idx_d_arr.append(i)

        while idx_r_arr and idx_d_arr:
            idx_r = idx_r_arr.pop(0)
            idx_d = idx_d_arr.pop(0)
            if idx_r < idx_d:
                idx_r_arr.append(n + idx_r)
            else:
                idx_d_arr.append(n + idx_d)
        return 'Radiant' if idx_r_arr else 'Dire'