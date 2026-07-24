class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isvalid(nums):
            temp=[]
            for num in nums:
                if num.isdigit():
                    temp.append(num)
                
            if len(temp)!=len(set(temp)):
                return False
            else : return True
        def get_col(board,j):
            temp=[]
            for i in range(9):
                temp.append(board[i][j])
            return temp
        def matrtolist(board,br,bc):
            temp=[]
            for i in range(br*3,br*3+3):
                for j in range(bc*3,bc*3+3):
                    temp.append(board[i][j])
            return temp
        
        for i in range(9):
            temp=[]
            if not isvalid(board[i]):
                return False
            temp=get_col(board,i)
            if not isvalid(temp):
                return False
    
        for i in range(3):
            for j in range(3):
                temp=matrtolist(board,i,j)
                if not isvalid(temp):
                    return False
        return True

        



