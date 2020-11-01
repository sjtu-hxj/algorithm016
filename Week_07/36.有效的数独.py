class Solution:
    def isValidSudoku(self, board):
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxs = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    boxIndex = (i // 3) * 3 + j // 3
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] =columns[j].get(num, 0) + 1
                    boxs[boxIndex][num] =boxs[boxIndex].get(num, 0) + 1
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxs[boxIndex][num] > 1:
                        return False
        return True
