import pygame
from snakeClass import Snake
from foodClass import Food

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
    snake = Snake()
    food = Food()
    food.spawnFood()
    moveBuffer = 2
    pygame.draw.rect(window, "Black", [snake.headPos, (10,10)])
    

    while running:
        pygame.display.update()
        window.fill(windowColor)
        
        clock.tick(60)
        if moveBuffer == 0:
            snake.Move()
            moveBuffer = 2
        else:
            moveBuffer -= 1
        pygame.draw.rect(window, food.Color, [food.position, (10,10)])
        pygame.draw.rect(window, snake.headColor, [snake.headPos, (10,10)])
        for i in range(len(snake.tailQueue)):
            pygame.draw.rect(window, snake.tailColor, [snake.tailQueue[i], (10,10)])
            
        if moveBuffer == 0 and snake.tailPauseTimer <= 0 and food.eatFood(snake.headPos):
            snake.tailQueue.pop(0)
            
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_SPACE:
                    paused = True
                    while paused:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    paused= False

                elif event.key == pygame.K_w:
                    snake.direction = "North"
                    
                elif event.key == pygame.K_a:
                    snake.direction = "West"
                    
                elif event.key == pygame.K_s:
                    snake.direction = "South"
                    
                elif event.key == pygame.K_d:
                    snake.direction = "East"
                    
    pygame.quit()
    
if __name__ == "__main__":
    main()
