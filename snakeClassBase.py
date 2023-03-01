import pygame

class Snake:
    def __init__(self):
        
        """
        Create variables for the position, tailQueue, direction, headColor, tailColor, windowWidth and windowHeight
            position = A list that contains two integers X and Y
           tailQueue = A list that starts empty and will contain the coordinates of the tail segments
           direction = A string that contains the direction the snake is facing
                North --> Up
                East  --> Right
                South --> Down
                West  --> Left
           headColor = A pygame.Color that takes a string as input
           tailColor = A pygame.Color that takes a string as input
         windowWidth = The width of the window
        windowHeight = The height of the window
        """

    def Move(self):
        
        """
        Setup a match/case where you're matching the direction to four different cases:
                North:
                    Append to the tailQueue a list containing the snake's X and Y coordinates
                    (Note: this should be a new list containing self.position[0] and self.position[1])
                    Subtract 10 from snake's Y coordinate
                    Check each tail segment in the tailQueue using a for loop
                        If the tail segment's coordinates equals the snake's coordinates:
                            Return True
                    If the snake's Y position is less than 0:
                        Return True

                East:
                    Append to the tailQueue a list containing the snake's X and Y coordinates
                    (Note: this should be a new list containing self.position[0] and self.position[1])
                    Add 10 to the snake's X position
                    Check each tail segment in the tailQueue using a for loop
                        If the tail segment's coordinates equals the snake's coordinates:
                            Return True
                    If the snake's X position is greater than the windowWidth - 10:
                        Return True

                South:
                    Append to the tailQueue a list containing the snake's X and Y coordinates
                    (Note: this should be a new list containing self.position[0] and self.position[1])
                    Add 10 to the snake's Y coordinate
                    Check each tail segment in the tailQueue using a for loop
                        If the tail segment's coordinates equals the snake's coordinates:
                            Return True
                    If the snake's Y position is greater than the windowHeight - 10:
                        Return True

                West:
                    Append to the tailQueue a list containing the snake's X and Y coordinates
                    (Note: this should be a new list containing self.position[0] and self.position[1])
                    Subtract 10 from snake's X coordinate
                    Check each tail segment in the tailQueue using a for loop
                        If the tail segment's coordinates equals the snake's coordinates:
                            Return True
                    If the snake's X position is less than 0:
                        Return True
        """

if __name__ == "__main__":
    print()
