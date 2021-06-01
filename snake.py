import random
import time

import pygame

size = [600, 600]
gameDisplay = pygame.display.set_mode(size)

pygame.init()

speed = 150
block_size = 40

score_record = open('score.txt', 'r', encoding='utf-8')
score_record = score_record.read()
score_record = int(score_record)


pygame.display.set_caption('Snake')
font = pygame.font.SysFont(None, 25)
gameExit = False

display_width = 600
display_height = 600

lead_x = (display_width - block_size) / 2
lead_y = (display_height - block_size) / 2

lead_x_change = 0
lead_y_change = 0

snakeList = []
snakeLength = 1
score = 1

red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)


appleX = round(
    random.randrange(
        block_size, display_width - block_size * 2) / block_size) * block_size
appleY = round(
    random.randrange(
        block_size, display_height - block_size * 2) / block_size) * block_size
coinY = None
coinX = None
debug_coin = 1
coin_detector = 0


def snake(headname, bodyname, snakeList, snakeHead, lead_x, lead_y):
    for XnY in snakeList:
        gameDisplay.blit(pygame.image.load(bodyname), (XnY[0], XnY[1]))
        gameDisplay.blit(pygame.image.load(headname), (lead_x, lead_y))


def spawn_coin(coinY, coinX):
    gameDisplay.blit(pygame.image.load('coin.png'), (coinY, coinX))


def message_to_screen(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x, y])


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_RIGHT:
                lead_x_change = -block_size
                lead_y_change = 0
            if event.key == pygame.K_d or event.key == pygame.K_LEFT:
                lead_x_change = block_size
                lead_y_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                lead_x_change = 0
                lead_y_change = - block_size
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                lead_x_change = 0
                lead_y_change = block_size

    if (
        lead_x >= display_width - block_size or
        lead_x < 0 or
        lead_y >= display_height or
        lead_y < 0
    ):
        gameDisplay.blit(pygame.image.load('bg.jpg'), (0, 0))
        message_to_screen(
            ''.join(
                [
                    'Ты проиграл! Твоя змея врезалась в стену. Очки: ',
                    str(score)
                ]),
        white, 30, 30)
        if score >= score_record:
                score_r = open('score.txt','w')
                score_r.write(str(score))
                score_r.close()
        pygame.display.update()
        time.sleep(2)
        gameExit = True
        
    lead_x += lead_x_change
    lead_y += lead_y_change
    snakeHead = [lead_x, lead_y]
    snakeList.append(snakeHead)
    if (len(snakeList)) > snakeLength:
        del snakeList[0]

    for eachSegment in snakeList[:-1]:
        if eachSegment == snakeHead:
            gameDisplay.blit(pygame.image.load('bg.jpg'), (0, 0 ))
            message_to_screen(''.join(['Ты проиграл! Твоя змея врезалась в стену. Очки: ', str(score)]),white, 30, 30)
            if score >= score_record:
                score_r = open('score.txt','w')
                score_r.write(str(score))
                score_r.close()
            pygame.display.update()
            time.sleep(2)
            gameExit = True

    if lead_x == appleX and lead_y == appleY:
        appleX = round(random.randrange(block_size, display_width - block_size * 2) / block_size) * block_size
        appleY = round(random.randrange(block_size, display_height - block_size * 2) / block_size) * block_size
        print('яблоки',appleX, appleY)
        snakeLength += 1
        score += 1
        
    if score == 2 and coin_detector == 0 :
        coinX = round(random.randrange(block_size, display_width - block_size * 2) / block_size) * block_size
        coinY = round(random.randrange(block_size, display_height - block_size * 2) / block_size) * block_size
        print(coinX, coinY)
        coin_detector = 1
        gameDisplay.blit(pygame.image.load('coin.png'), (coinY, coinX))
        pygame.display.update()
        #spawn_coin(coinX, coinY)
        debug_coin = 0
        
    if lead_x == coinX and lead_y == coinY:
        snakeLength += 1
        score += 3
        CoinX = None
        CoinY = None
        coin_detector = 0
        debug_coin = 1
        
    gameDisplay.blit(pygame.image.load('bg.jpg'), (0, 0))
    gameDisplay.blit(pygame.image.load('apple.png'), (appleX, appleY))
    
    message_to_screen(''.join(['Score: ', str(score)]), white, 10, 10)
    if score_record <= score:
        message_to_screen(''.join(['Record: ', str(score)]), white, 10, 30)
    else:
        message_to_screen(''.join(['Record: ', str(score_record)]), white, 10, 30)
    snake('head.png', 'body.png', snakeList, snakeHead, lead_x, lead_y)
    
    pygame.display.update()
    
    pygame.time.delay(speed)
pygame.quit()


print('ssss')



