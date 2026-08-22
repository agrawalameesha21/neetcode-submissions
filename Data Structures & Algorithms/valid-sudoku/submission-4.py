class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        rows = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == '.': continue
                if value in rows[i] or value in columns[j] or value in squares[(i//3, j//3)]:
                    return False

                rows[i].add(value)
                columns[j].add(value)
                squares[(i//3, j//3)].add(value)    
        return True 