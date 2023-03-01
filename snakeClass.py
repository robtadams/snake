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
                self.tailQueue.append([self.headPos[0], self.headPos[1]])
                self.headPos[1] -= 10
                for segment in self.tailQueue:
                    if segment == self.headPos:
                        return True
                if self.headPos[1] < 0:
                    return True

            case "West":
                self.tailQueue.append([self.headPos[0], self.headPos[1]])
                self.headPos[0] -= 10
                for segment in self.tailQueue:
                    if segment == self.headPos:
                        return True
                if self.headPos[0] < 0:
                    return True

            case "South":
                self.tailQueue.append([self.headPos[0], self.headPos[1]])
                self.headPos[1] += 10
                for segment in self.tailQueue:
                    if segment == self.headPos:
                        return True
                if self.headPos[1] > self.windowHeight - 10:
                    return True

            case "East":
                self.tailQueue.append([self.headPos[0], self.headPos[1]])
                self.headPos[0] += 10
                for segment in self.tailQueue:
                    if segment == self.headPos:
                        return True
                if self.headPos[0] > self.windowWidth - 10:
                    return True

if __name__ == "__main__":
    print()
