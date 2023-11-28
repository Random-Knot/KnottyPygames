import pygame as pg, sys, random
pg.init()

# colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# initVars
w, h = 400, 400
win = pg.display.set_mode((w, h))
snake = [(w // 2, h // 2), (w // 2 - 10, h // 2), (w // 2 - 10, h // 2)]
dir = (10, 0)
fx, fy = random.randrange(1, 40)*10, random.randrange(1, 40)*10
score = 0
clock = pg.time.Clock()
running = True
GameOver = True
font = pg.font.Font(None, 36)
# highScore
with open("highscore.txt", "r") as file:
    try: highscore = int(file.read())
    except ValueError: highscore = 0

while running:
    # events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        k = pg.key.get_pressed()
        if k[pg.K_RIGHT] and dir != (-10, 0): dir  = (10, 0)
        if k[pg.K_LEFT] and dir != (10, 0): dir = (-10, 0)
        if k[pg.K_UP] and dir != (0, 10): dir = (0, -10)
        if k[pg.K_DOWN] and dir != (0, -10): dir = (0, 10)

    # display
    pg.display.set_caption(f'This: {score} ||  High: {highscore}')
    win.fill(black)
    for i in snake:
        pg.draw.rect(win, white, pg.Rect(i[0], i[1], 10, 10))
    pg.draw.rect(win, red, pg.Rect(fx, fy, 10, 10))

    # collisions
    x, y = snake[0][0] + dir[0], snake[0][1] + dir[1]
    snake.insert(0, (x, y))
    if [x, y] == [fx, fy]:
        fx, fy = random.randrange(1, 40) * 10, random.randrange(1, 40) * 10
        score += 1
    else: snake.pop()

    if (x, y) in snake[2:] or x < 0 or x >= w or y < 0 or y >= h: GameOver = True

    # update
    while GameOver == True:
        with open("highscore.txt", "w") as file:
            if score > highscore:
                file.write(str(score))
            else:
                file.write(str(highscore))
            score = 0
            snake = [(w // 2, h // 2), (w // 2 - 10, h // 2), (w // 2 - 10, h // 2)]
            dir = (10, 0)
            fx, fy = random.randrange(1, 40) * 10, random.randrange(1, 40) * 10
            GameOver = False
    pg.display.flip()
    clock.tick(15)

pg.quit()
sys.exit()

