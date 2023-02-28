import pygame

class snake:
    headPos = (240, 240)
    tailQueue = []
    

def main():
    pygame.display.init()
    clock = pygame.time.Clock()
    windowWidth = 500
    windowHeight = 500
    window = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption("Snake")
    windowColor = pygame.Color("White")
    window.fill(windowColor)
    pygame.display.update()
    running = True

    while running:
        pygame.draw.rect(window, "Black", [snake.headPos, (10,10)])
        for i in range(len(snake.tailQueue)):
            pygame.draw.rect(window, "Black", [snake.tailQueue[i], (10, 10)])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_w:
                    snake.tailQueue.append(snake.headPos)
                    snake.headPos = (snake.headPos[0], snake.headPos[1] - 10)
                    if snake.headPos[1] < 0:
                        snake.headPos = (snake.headPos[0], 0)
                    
                if event.key == pygame.K_a:
                    snake.tailQueue.append(snake.headPos)
                    snake.headPos = (snake.headPos[0] - 10, snake.headPos[1])
                    if snake.headPos[0] < 0:
                        snake.headPos = (0, snake.headPos[1])

                if event.key == pygame.K_s:
                    snake.tailQueue.append(snake.headPos)
                    snake.headPos = (snake.headPos[0], snake.headPos[1] + 10)
                    if snake.headPos[1] > windowHeight - 10:
                        snake.headPos = (snake.headPos[0], windowHeight - 10)

                if event.key == pygame.K_d:
                    snake.tailQueue.append(snake.headPos)
                    snake.headPos = (snake.headPos[0] + 10, snake.headPos[1])
                    if snake.headPos[0] > windowWidth - 10:
                        snake.headPos = (windowWidth - 10, snake.headPos[1])

                window.fill(windowColor)
                print(str(snake.headPos))
        pygame.display.update()
    pygame.quit()
    
if __name__ == "__main__":
    main()
