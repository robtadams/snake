import pygame
import random

class Food:
    def __init__(self):
        self.Color = pygame.Color("Orange")
        self.position = [-1, -1]
        self.windowWidth, self.windowHeight = pygame.display.get_surface().get_size()
        self.foodExists = False

    def spawnFood(self):
        randX = random.randint(0, (self.windowWidth - 10) // 10)
        randY = random.randint(0, (self.windowHeight - 10) // 10)

        randX *= 10
        randY *= 10

        self.position = [randX, randY]

    def eatFood(self, snakePos):
        if snakePos == self.position:
            self.foodExists = False
            self.spawnFood()

        else:
            self.foodExists = True

        return self.foodExists
