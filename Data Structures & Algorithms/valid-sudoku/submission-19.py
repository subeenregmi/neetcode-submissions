class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)] 
        colSets = [set() for _ in range(9)] 
        boxSets = [set() for _ in range(9)] 

        for i in range(9):
            for j in range(9):
                print(i, j, board[i][j])
                if board[i][j] == '.':
                    continue

                num = board[i][j]

                boxSetI = (j // 3) + (i // 3) * 3
                if (num in rowSets[i]) or (num in colSets[j]) or num in boxSets[boxSetI]:
                    return False
                
                rowSets[i].add(num)
                colSets[j].add(num)
                boxSets[boxSetI].add(num)
        
        return True