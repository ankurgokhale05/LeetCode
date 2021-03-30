class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # Error Checking
        if board == None or len(board) == 0 or len(board[0]) == 0:
            return board
        done = True
        
        # Crushing rows using 3 slider window
        for i in range(len(board)):
            for j in range(len(board[0]) - 2):
                nums1 = abs(board[i][j])
                nums2 = abs(board[i][j+1])
                nums3 = abs(board[i][j+2])
                
                if nums1 == nums2 and nums2 == nums3 and nums1 != 0:
                    board[i][j] = -nums1
                    board[i][j+1] = -nums2
                    board[i][j+2] = -nums3
                    done = False
        
        # Crushing cols using 3 slider col window
        for j in range(len(board[0])):
            for i in range(len(board) - 2):
                nums1 = abs(board[i][j])
                nums2 = abs(board[i+1][j])
                nums3 = abs(board[i+2][j])
                
                if nums1 == nums2 and nums2 == nums3 and nums1 != 0:
                    board[i][j] = -nums1
                    board[i+1][j] = -nums2
                    board[i+2][j] = -nums3
                    done = False
                    
        # Gravity Logic (Similar to moving zeroes in column)
        if not done:
            for j in range(len(board[0])):
                idx = len(board) - 1
                for i in range(len(board) - 1, -1, -1):
                    if board[i][j] > 0:
                        board[idx][j] = board[i][j]
                        idx -= 1
                for i in range(idx,-1,-1):
                    board[i][j] = 0
        return board if done else self.candyCrush(board)