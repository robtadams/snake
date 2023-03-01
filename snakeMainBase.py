import pygame
from snakeClass import Snake
from foodClass import Food

def main():
    
    """
    Initialize pygame's display and font functions
    """
    

    """
    Create variables for:
        windowWidth = An integer that is the total width of the screen
        windowHeight = An integer that is the total height of the screen
        window = The pygame display set_mode that is passed a list containing windowWidth and windowHeight
        windowColor = A pygame Color that takes a string as input
        clock = The pygame time that contains the initialization for Clock()
        score = An integer that should be initialized to 0
        snake = A Snake() object
        food = A Food() object
        moveBuffer = An integer that should be initialized to 2
        running = A boolean that should be initialized to True
    """


    """
    Set the caption of the window to print the title of the program and the score
    Fill the window with windowColor
    Update the display
    Use food to call spawnFood()
    Draw a rectangle in the window at the snake's position with a width and length of 10
    """


    """
    Create a while running loop:
        Update the display
        Fill the window with windowColor
        Call tick(60) using clock
        If the move buffer equals 0:
            If snake.Move() returns True:
                !!! DO THIS LATER !!!
            Set moveBuffer to equal 2
        Otherwise:
            Subtract one from moveBuffer
        Draw a rectangle in the window at the food's position with a width and length of 10
        Draw a rectangle in the window at the snake's position with a width and length of 10
        For each segment in tailQueue:
            Draw a rectangle in the window at the segment's position with a width and length of 10
        If moveBuffer equals 0:
            Create a variable called foodNotEaten and make it equal to the result of food's eatFood()
            If foodNotEaten is False:
                pop() the first element in tailQueue
            Otherwise:
                Increase score by 1
                Update the display caption to reflect the new score
                (Note: Use 'Your Caption Here {0}'.format(score) to do this easily)
                (Note: The {0} will be replaced by whatever is inside format())
    """


    """
    Inside the while running loop:
        Create a for loop checking each pygame event:
            If the event is a keydown:
                If the key is Escape:
                    Set running equal to False
                If the key is W:
                    Set snake's direction to 'North'
                If the key is A:
                    Set snake's direction to 'West'
                If the key is S:
                    Set snake's direction to 'South'
                If the key is D:
                    Set snake's direction to 'East'

    Once the while loop is done, quit pygame
    """


    """
    Inside the !!! DO THIS LATER !!! part:
        Create an endFont, scoreFont, and menuFont variables
        ...
    """
    
if __name__ == "__main__":
    main()
