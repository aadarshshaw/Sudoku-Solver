from attr import mutable
import numpy as np
import os 
import cv2
import drawGrid

class SudokuSolver:
    board = np.array((9,9))
    mutable = np.copy(board)

    def __init__(self,board):
        self.board = board
        self.mutable = np.copy(board)

    def clear(self):
        os.system('cls')

    def checkRows(self,row,col,n):
        for i in range(9):
            if self.board[i][col] == n:
                return False
        return True

    def checkCols(self,row,col,n):
        for j in range(9):
            if self.board[row][j]==n:
                return False
        return True
    def checkBox(self,row,col,n):
        nums=[]
        for i in range((row//3)*3,(row//3)*3 + 3):
            for j in range((col//3)*3,(col//3)*3 +3):
                if self.board[i][j] == n:
                    return False
        return True

    def check(self,row,col,n):
        return self.checkBox(row,col,n) and self.checkRows(row,col,n) and self.checkCols(row,col,n)

    def findNext(self,col, row):
        for i in range(0,9):
            for j in range(0,9):
                if self.board[i][j] ==0 and self.mutable[i][j]==0:
                    return (j,i)
        return -1,-1

    def solve(self,col, row):
        col,row = self.findNext(col,row)
        if(row == -1):
            print("Solved")
            cv2.imshow("Sudoku",drawGrid.drawSudoku(self.board))
            cv2.waitKey(1)
            return True
        for i in range(1,10):
            if self.check(row,col,i):
                self.board[row][col] = i
                if(self.solve(col,row)):
                    return True
                cv2.imshow("Sudoku",drawGrid.drawSudoku(self.board))
                cv2.waitKey(1)
            self.board[row][col] = 0
        return False


