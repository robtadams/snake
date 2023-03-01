import pygame
import random

class Food:
    def __init__(self):

        """
        Create variables for color, position, windowWidth and windowHeight
                   Color = A pygame.Color that takes a string as input
                Position = A list that contains two integers X and Y
             windowWidth = The width of the window
            windowHeight = The height of the window
        """

    def spawnFood(self):
        
        """
        Create two variables for the new X and Y positions of the food
            randX = a random integer from 0 to the windowWidth minus 10, and then divided by 10
            randY = a random integer from 0 to the windowHeight minus 10, and then divided by 10
        """

        """
        Multiply randX and randY by 10
        """

        """
        Set food's position to be equal to a list containing randX and randY
        """

    def eatFood(self, snakePos):
        
        """
        Create an if statement checking if snakePos is equal to the food's position
            Then call spawnFood and return False
        Otherwise return True
        """
        
