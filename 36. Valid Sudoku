class Solution:
    def isValidSudoku(self, matrix: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            s = set()
            for j in matrix[i]:
                if j != ".":
                    if j in s:
                        return False
                    s.add(j)
        
        # Check columns
        for i in range(9):
            s = set()
            for j in range(9):
                if matrix[j][i] != ".":
                    if matrix[j][i] in s:
                        return False
                    s.add(matrix[j][i])
        
        # Check boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if matrix[k][l] != ".":
                            if matrix[k][l] in s:
                                return False
                            s.add(matrix[k][l])
        
        return True
