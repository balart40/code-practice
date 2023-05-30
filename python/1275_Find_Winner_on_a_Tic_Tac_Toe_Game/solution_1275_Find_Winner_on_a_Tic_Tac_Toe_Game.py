class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        movess = [ [""]*3 for i in range(3)]
        boolean = True
        for i,j in moves:
            if boolean:
                movess[i][j] = "X"
            else:
                movess[i][j] = "O"
            boolean = not boolean
        # check diagonals
        # X
        if movess[0][0] == "X" and  movess[1][1] == "X" and  movess[2][2] == "X":
            return "A"
        if movess[2][0] == "X" and  movess[1][1] == "X" and  movess[0][2] == "X":
            return "A"
        # O
        if movess[0][0] == "O" and  movess[1][1] == "O" and  movess[2][2] == "O":
            return "B"
        if movess[2][0] == "O" and  movess[1][1] == "O" and  movess[0][2] == "O":
            return "B"

        for rowColumn in range(3):
            # check rows
            if movess[rowColumn][0] == "X" and movess[rowColumn][1] == "X" and  movess[rowColumn][2] == "X":
                return "A"
            elif movess[rowColumn][0] == "O" and movess[rowColumn][1] == "O" and  movess[rowColumn][2] == "O":
                return "B"
            # check columns
            elif movess[0][rowColumn] == "X" and movess[1][rowColumn] == "X" and movess[2][rowColumn] == "X":
                return "A"
            elif movess[0][rowColumn] == "O" and movess[1][rowColumn] == "O" and movess[2][rowColumn] == "O":
                return "B"
        return "Draw" if len(moves) == 9 else "Pending"