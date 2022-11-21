import pygame
import random
from sys import exit

pygame.init()

width, height = 900, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Game")
clock = pygame.time.Clock()
FPS = 60
game_active = True
score = 0

xVel, yVel = 5, -5

def draw(paddle, ball, scoreText):
    screen.fill('black')
    pygame.draw.rect(screen, 'white', paddle)
    pygame.draw.ellipse(screen, 'white', ball)

    screen.blit(scoreText, scoreText.get_rect(center = (width//2, height//2)))

def moveBall(ball, paddle):
    global xVel, yVel, game_active, score

    ball.x += xVel
    ball.y += yVel

    if ball.top <= 0: yVel = -(yVel)
    if ball.right >= width: xVel = -(xVel)
    if ball.bottom >= height: game_active = False
    if ball.left <= 0: xVel = -(xVel)

    if ball.colliderect(paddle):
        score += 1
        yVel = -(yVel)
        xVel = random.choice([4, -4, 5, -5, 6, -6, 7, -7, 8, -8])

def main():
    global game_active, xVel, yVel, score
    paddle = pygame.Rect(0, 0, 100, 8)
    paddle.center = (width/2, height-20)
    paddleVel = 10

    ball = pygame.Rect(0, 0, 20, 20)
    ball.center = (width/2, height/2)

    font = pygame.font.SysFont('DS-DIGITAL', 100)
    gameOverFont = pygame.font.SysFont('Comic Sans MS', 70)
    scoreFont = pygame.font.SysFont('Comic Sans MS', 40)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if not(game_active):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_active = True
                        score = 0
                        ball.center = (width/2, height/2)
                        xVel, yVel = 5, -5

        if game_active:
            scoreText = font.render(f'{score}', True, 'white')
            draw(paddle, ball, scoreText)

            # move the paddle

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and not(paddle.left <= 0): paddle.left -= paddleVel
            if keys[pygame.K_RIGHT] and not(paddle.right >= width): paddle.right += paddleVel
            moveBall(ball, paddle)
        else:
            screen.fill('black')
            gamerOverText = gameOverFont.render('Gamer Over !', True, 'white')
            endScoreText = scoreFont.render(f'Score - {score}', True, 'pink')

            screen.blit(gamerOverText, gamerOverText.get_rect(center=(width/2, height/2-100)))
            screen.blit(endScoreText, endScoreText.get_rect(center=(width/2, height/2)))


        clock.tick(FPS)
        pygame.display.update()

if __name__ == '__main__':
    main()
