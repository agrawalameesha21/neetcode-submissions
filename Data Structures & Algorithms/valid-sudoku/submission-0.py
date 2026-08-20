class Solution:
    rows = [[]]
    columns = [[]]
    squares = [[]]

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.columns = [[] for _ in range(9)]
        self.squares = [[] for _ in range(9)]
        self.rows = [[] for _ in range(9)]

        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value != '.':
                    self.rows[i].append(value)

        for i in self.rows:
            map = set()
            for j in i:
                if j in map: 
                    print(j, map)
                    return False
                map.add(j)

        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value != '.':
                    self.columns[j].append(value)

        for i in self.columns:
            map = set()
            for j in i:
                if j in map: 
                    print(j, map)
                    return False
                map.add(j)

        sq_index = 0
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value != '.':
                    self.squares[sq_index].append(value)
                if j == 2 or j == 5:
                    sq_index = sq_index + 1
            if i < 2:
                sq_index = 0
            elif i < 5:
                sq_index = 3
            else:
                sq_index = 6

        for i in self.squares:
            map = set()
            for j in i:
                if j in map: 
                    print(j, map)
                    return False
                map.add(j)

        return True 