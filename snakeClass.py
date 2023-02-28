import pygame

class Snake:
    def __init__(self):
        self.headPos = [240, 240]
        self.tailQueue = []
        self.tailPauseTimer = 1
        self.direction = "East"
        self.headColor = pygame.Color("Red")
        self.tailColor = pygame.Color("Dark Green")
        self.windowWidth, self.windowHeight = pygame.display.get_surface().get_size()

    def Move(self):
        self.tailPauseTimer -= 1
        match self.direction:
            case "North":
                temp = [0, 0]
                temp[0] = self.headPos[0]
                temp[1] = self.headPos[1]
                self.tailQueue.append(temp)
                self.headPos[1] -= 10
                if self.headPos[1] < 0:
                    self.headPos[1] = 0

            case "West":
                temp = [0, 0]
                temp[0] = self.headPos[0]
                temp[1] = self.headPos[1]
                self.tailQueue.append(temp)
                self.headPos[0] -= 10
                if self.headPos[0] < 0:
                    self.headPos[0] = 0

            case "South":
                temp = [0, 0]
                temp[0] = self.headPos[0]
                temp[1] = self.headPos[1]
                self.tailQueue.append(temp)
                self.headPos[1] += 10
                if self.headPos[1] > self.windowHeight - 10:
                    self.headPos[1] = self.windowHeight - 10

            case "East":
                temp = [0, 0]
                temp[0] = self.headPos[0]
                temp[1] = self.headPos[1]
                self.tailQueue.append(temp)
                self.headPos[0] += 10
                if self.headPos[0] > self.windowWidth - 10:
                    self.headPos[0] = self.windowWidth - 10

if __name__ == "__main__":
    print()
