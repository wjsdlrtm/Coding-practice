class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(0,9):
            if len(board[i].replace('.','')) > len(set(board[i].replace('.',''))):
                return False

            for j in range(0,9):
                board2 = []
                board2.append(board[i][j])
            if len(board2.replace('.','')) > len(set(board2.replace('.',''))):
                return False
        for x in range(0,3):
            for y in range(0,3):
                board3 = []
                for z in range(0,3):
                    for w in range(0,3):

                        board3.append(board[3*x+z][3*y+w])
                if len(board3.replace('.','')) > len(set(board3.replace('.',''))):
                    return False
        return True