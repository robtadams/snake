import tkinter as tk
from cell import Cell
import random

global TEST
TEST = True

class minesweeper():
    def __init__(self):

        # rows: an integer that contains the number of rows in the game
        # This affects the number of cells in the Y dimension of the game
        self.rows = 9

        # cols: an integer that contains the number of columns in the game
        # This affects the number of cells in the X dimension of the game
        self.cols = 9

        # cellArray: a list that contains all of the cells in the game
        self.cellArray = []

        # buttonArray: a list that contains all of the buttons in the game
        self.buttonArray = []

        #bombsPrimed: checks if bombs have been primed yet
        self.bombsPrimed = False

        tempIndex = 0

        # For every row in the game...
        for y in range(self.rows):

            cellRow = []

            # ... and for every column in the game...
            for x in range(self.cols):

                # ... create a cell at its current coordinate...
                newCell = Cell(y, x, tempIndex)

                # ... and add it to the array
                cellRow.append(newCell)

                tempIndex += 1

            self.cellArray.append(cellRow)

                

        # If TEST is True...
        if TEST:

            # For every cell in cellArray...
            for i in self.cellArray:

                # ... print out the row (y coordinate) and column (x coordinate) of that cell
                print(i)
                
    def main(self):

        # Build the TKinter window
        self.buildWindow()

    def buildWindow(self):

        # Create the Tkinter window
        window = tk.Tk()

        # Prevent the window from being resized
        window.resizable(False, False)

        # Build a frame where the reset button will go
        statusFrame = tk.Frame(
            master = window,
            relief = tk.FLAT
        )

        # Place the statusFrame into the grid
        statusFrame.grid(row = 0, column = 0, columnspan = 10)

        # Build the reset button and place it onto the grid
        newGameButton = tk.Button(master = statusFrame, text = "Restart", command = self.reset)
        newGameButton.grid(row = 0, column = 0, pady = 10)

        # Build a buffer between the reset button and game field
        divLabel = tk.Label(master = statusFrame)
        divLabel.grid(row = 1, column = 0)

        tempIndex = 0

        for y in range(self.rows):
            for x in range(self.cols):
                self.buttonArray.append(tk.Button(
                    window,
                    width = 2,
                    height = 1,
                    relief = tk.RAISED,
                    command = lambda buttonIndex = tempIndex: self.dig(buttonIndex)
                ))
                self.buttonArray[tempIndex].grid(row = y + 1, column = x)
                tempIndex += 1

    def dig(self, buttonIndex):

        if not self.bombsPrimed:

            safeArray = []
            for rows in range(self.rows):
                for cols in range(self.cols):
                    safeArray.append([rows, cols])

            safeArray.pop(buttonIndex)
            
            self.prime(safeArray, buttonIndex)

        self.buttonArray[buttonIndex].config(relief = tk.SUNKEN)

    def reset(self):

        # Reset the array containing the valid bomb cells
        for y in range(self.cols):
            for x in range(self.rows):
                self.safe.append([y, x])

        # Reset the display for each button
        for row in self.buttonArray:
            for button in row:
                button.config(relief = tk.RAISED, bg = 'SystemButtonFace', text = "")
                self.cellArray = [ [0]*self.cols for _ in range(self.rows)]


        self.bombsPrimed = False

    def prime(self, safeArray, buttonIndex):

        # Prime the bombs
        self.bombsPrimed = True
 
        # Generate 10 bombs

        for i in range(10):

            # Get a random cell within the array
            randCel = random.randint(0, len(safeArray) - 1)
            print("Random Cell:", randCel)

            # Remove that cell from the safe array, and get it's coordinates
            bombCoordinate = safeArray.pop(randCel)
            bombX = bombCoordinate[0]
            bombY = bombCoordinate[1]
            self.cellArray[bombX][bombY].isBomb = True
            
            if TEST:
                #print("Cell Index:", bombIndex)
                #print("Length of cellArray:", len(self.cellArray))
                #self.buttonArray[bombIndex].config(bg = "red")
                6

            # Set that cell to -1, indicating that it is a bomb
            self.cellArray[bombIndex].numAdjacentBombs = -1
            self.buttonArray[bombIndex].config(text = -1)

            # Settle for hardcoded here (for now)
            for modifier in [-10, -9, -8, -1, 1, 8, 9, 10]:
                self.cellArray[bombIndex + modifier].numAdjacentBombs += 1
                self.buttonArray[bombIndex + modifier].config(text = self.cellArray[bombIndex + modifier].numAdjacentBombs)

            """
            # Check each adjacent cell
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:

                    # Get an adjacent cell
                    

                    # Check if that cell is in bounds...
                    if tempX >= 0 and tempX <= 8:
                        if tempY >= 0 and tempY <= 8:

                            # Do math to that cell
                            if self.cellArray[tempX][tempY] >= 0:
                                self.cellArray[tempX][tempY] += 1
                                self.buttonArray[tempX][tempY].config(text = self.cellArray[tempX][tempY])
            """

app = minesweeper()
app.main()
