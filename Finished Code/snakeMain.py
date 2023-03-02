import pygame
from snakeClass import Snake
from foodClass import Food

def main():
    pygame.display.init()
    pygame.font.init()  
    clock = pygame.time.Clock()
    windowWidth = 500
    windowHeight = 500
    window = pygame.display.set_mode((windowWidth, windowHeight))
    score = 0
    pygame.display.set_caption("Snake -- Score: {0}".format(score))
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
            if snake.Move():
                endFont = pygame.font.Font(pygame.font.match_font('impact'), 50)
                endText = endFont.render("GAME OVER", True, (0, 0, 0), (255, 255, 255))
                endTextRect = endText.get_rect()
                endTextRect.center = (windowWidth // 2, windowHeight // 4)
                window.blit(endText, endTextRect)

                scoreFont = pygame.font.Font(pygame.font.match_font('impact'), 40)
                scoreText = scoreFont.render("Score: {0}".format(score), True, (0, 0, 0), (255, 255, 255))
                scoreTextRect = scoreText.get_rect()
                scoreTextRect.center = (windowWidth // 2, windowHeight // 2)
                window.blit(scoreText, scoreTextRect)

                menuFont = pygame.font.Font(pygame.font.match_font('impact'), 25)
                menuText = menuFont.render("Press ESC to Quit \\ Press R to restart", True, (0, 0, 0), (255, 255, 255))
                menuTextRect = menuText.get_rect()
                menuTextRect.center = (windowWidth // 2, (windowHeight // 2) + 100)
                window.blit(menuText, menuTextRect)
                
                pygame.display.update()

                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False

                            if event.key == pygame.K_r:
                                main()

            moveBuffer = 2
        else:
            moveBuffer -= 1
        pygame.draw.rect(window, food.Color, [food.position, (10,10)])
        pygame.draw.rect(window, snake.headColor, [snake.headPos, (10,10)])
        for i in range(len(snake.tailQueue)):
            pygame.draw.rect(window, snake.tailColor, [snake.tailQueue[i], (10,10)])
        
        if moveBuffer == 0 and snake.tailPauseTimer <= 0:
            foodTemp = food.eatFood(snake.headPos)
            if foodTemp:
                snake.tailQueue.pop(0)
            else:
                score += 1
                pygame.display.set_caption("Snake -- Score: {0}".format(score))
            
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
