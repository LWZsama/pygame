import pygame
import random

def control(state):
    global player1_v, player2_v, player1_y, player2_y
    
    keys = pygame.key.get_pressed()
    if state == 2:
        if keys[pygame.K_w]:
            player1_v = -5
        elif keys[pygame.K_s]:
            player1_v = 5
        else:
            player1_v = 0
    elif state == 1:
        if ball_x < width // 2 and ball_vx < 0:
            if player1_y + player_height // 2 < ball_y:
                player1_v = 5
            elif player1_y + player_height // 2 > ball_y:
                player1_v = -5
            else:
                player1_v = 0
        else:
            player1_v = 0
        
    if keys[pygame.K_UP]:
        player2_v = -5
    elif keys[pygame.K_DOWN]:
        player2_v = 5
    else:
        player2_v = 0

    player1_y += player1_v
    player1_y = max(player1_y, 0)
    player1_y = min(player1_y, height - player_height)

    player2_y += player2_v
    player2_y = max(player2_y, 0)
    player2_y = min(player2_y, height - player_height)


def judge():
    global width, height,ball_v, ball_vx, ball_vy, ball_x, ball_y, ball_r, player1_v, player2_v, player1_y, player2_y, gap, player1_score, player2_score, mode, win, score
    
    if (ball_vx < 0) and (ball_x - gap - player_width - ball_r <= 0) and (ball_y >= player1_y and ball_y <= (player1_y + player_height)):
        ball_vx = - ball_vx
        sound = pygame.mixer.Sound('pong.wav')
        sound.play()
        if ball_v <= 6.4:
            ball_v *= random.randint(10,14) / 10
        else:
            ball_v *= random.randint(7,10) / 10
    
    elif (ball_vx > 0) and (width - gap - player_width - ball_r - ball_x <= 0) and (ball_y >= player2_y and ball_y <= (player2_y + player_height)):
        ball_vx = - ball_vx
        sound = pygame.mixer.Sound('pong.wav')
        sound.play()
        if ball_v <= 6.4:
            ball_v *= random.randint(10,14) / 10
        else:
            ball_v *= random.randint(7,10) / 10
        score += 1
    
    if player1_score == 5 or player2_score == 5:
        if player1_score == 5:
            x = 1
        elif player2_score == 5:
            x = 2
        font = pygame.font.Font("times.ttf", 45)
        screen.fill(WHITE)
        text = font.render(f"player {x} wins!", True, RED)
        text_rect = text.get_rect()
        text_rect.center = (width // 2, height // 2)
        screen.blit(text, text_rect)
        win.play()


def ball():
    global width, height, ball_v, ball_vx, ball_vy, ball_x, ball_y, ball_r, player1_v, player2_v, player1_y, player2_y, gap, player1_score, player2_score
    
    screen.fill(WHITE)
    pygame.draw.line(screen, RED, [width // 2, 0], [width // 2, height], 2)
    pygame.draw.circle(screen, BLACK, (ball_x, ball_y), ball_r)
    pygame.draw.rect(screen, GREEN, (gap, player1_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (width - gap - player_width, player2_y, player_width, player_height))
    
    if ball_x <= ball_r:
        reset_ball()
        player2_score += 1
    elif ball_x >= (width - ball_r):
        reset_ball()
        player1_score += 1
    
    if ball_y <= ball_r or ball_y >= (height - ball_r):
        ball_vy = - ball_vy
        sound = pygame.mixer.Sound('table.mp3')
        sound.play()

    ball_x += ball_vx
    ball_y += ball_vy


def reset_ball():
    global ball_x, ball_y, ball_vx, ball_vy, ball_r, player1_y, player2_y
    
    ball_x = width // 2
    ball_y = random.randint(height // 4, (height // 4) * 3)
    ball_v = 6
    ball_vx = random.randint(48,55) / 10
    player1_y = height // 2 - player_height // 2
    player2_y = height // 2 - player_height // 2
    if random.choice([True, False]):
        ball_vx = - ball_vx
    ball_vy = (ball_v ** 2 - ball_vx **2) ** 0.5
    pygame.time.wait(500)


def ui(state):
    global player1_score, player2_score, width, height, mode, score
    
    if state == 2:
        text = font.render(f"player 1:  {player1_score}   player 2:  {player2_score}", True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = (width // 2, height // 2)
        screen.blit(text, text_rect)

    elif state == 1:
        text = font.render(f"robot:  {player1_score}   you:  {score}", True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = (width // 2, height // 2)
        screen.blit(text, text_rect)

def get_highscore():
    highscore = 0
    highscore_name = ""

    with open("rank.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            name, score = line.strip().split(": ")
            score = int(score)
            if score > highscore:
                highscore = score
                highscore_name = name

    return highscore, highscore_name


def pvp():
    control(2)
    ball()
    ui(2)
    judge()


def pve():
    control(1)
    ball()
    ui(1)
    judge()
    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

width = 1200
height = 600
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pong")

done = False

clock = pygame.time.Clock()

player_width = 10
player_height = 80
player1_y = height // 2 - player_height // 2
player2_y = height // 2 - player_height // 2
player1_v = 0
player2_v = 0

player1_score = 0
player2_score = 0
score = 0

gap = 20

ball_x = width // 2
ball_y = random.randint(height // 4, (height // 4) * 3)
ball_r = 10
ball_v = 6
ball_vx = random.randint(48,55) / 10
if random.choice([True, False]):
    ball_vx = -ball_vx
ball_vy = (ball_v ** 2 - ball_vx **2) ** 0.5

font = pygame.font.Font("times.ttf", 36)
mode = 0
win = pygame.mixer.Sound('win.mp3')
x = 0

player_name = input("What's your name?\n")
print(f"Enjoy your game, {player_name}!")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                mode = 0
            elif event.key == pygame.K_1:
                mode = 1
            elif event.key == pygame.K_2:
                mode = 2
                
    if mode == 0:
        screen.fill(WHITE)
        text = font.render("PRESS 1 IF SINGLE-PLAYER; PRESS 2 IF MUTI-PLAYER", True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = (width // 2, height // 2)
        screen.blit(text, text_rect)
        player1_score = 0
        player2_score = 0
        score = 0
    
    elif mode == 1:
        if player1_score != 5 and player2_score !=5: 
            pve()
            highscore, highscore_name = get_highscore()
            text = font.render(f"highest score: {highscore}     player name: {highscore_name}", True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = (width // 2, height // 2 + 50)
            screen.blit(text, text_rect)
        else:
            pygame.time.wait(int(win.get_length() * 1000))
            with open("rank.txt", "a") as file:
                file.write(f"{player_name}: {score}\n")
            mode = 0

    elif mode == 2:
        if player1_score != 5 and player2_score !=5:
            pvp()
        else:
            pygame.time.wait(int(win.get_length() * 1000))
            mode = 0

    pygame.display.flip()

    clock.tick(120)

pygame.quit()