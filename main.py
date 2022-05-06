import cv2
import grid
import SudokuSolver

if __name__ == "__main__":
    sudokuimg = cv2.imread("SudokuImage.png",cv2.COLOR_BGR2GRAY)
    board = grid.find_grid(sudokuimg)
    print(board)
    obj = SudokuSolver.SudokuSolver(board)
    if(obj.solve(0,0)):
        obj.clear()
        print(board)
        print("Solved")
    else:
        print("No Solution")
cv2.waitKey(0)
cv2.destroyAllWindows()