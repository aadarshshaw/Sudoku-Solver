from turtle import back
import cv2
import numpy as np

def drawSudoku(grid):
    width = 450
    height = 450
    background = np.ones((9,9))
    background = cv2.resize(background,(width,height))
    for i in range(9):
        cv2.line(background,(0,height//9 *i),(width,height//9 *i),(0,0,0),3)
        cv2.line(background,(width//9 *i,0),(width//9 *i,height),(0,0,0),3)
    for i in range(9):
        for j in range(9):
            bottomLeftOrigin = (width//9 * j+10,height//9 *(i+1)-10)
            cv2.putText(background,str(int(grid[i][j])),bottomLeftOrigin,cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,0),2,cv2.LINE_AA)
    return background
