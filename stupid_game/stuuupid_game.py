import pygame


def inter(x1, y1, x2, y2, db1, db2):
    if x2 - db1 < x1 < x2 + db2 and y1 > y2 - db1 and y2 < y2 + db2:
        return 1
    else:
        return 0


pygame.init()
window = pygame.display.set_mode((400, 400))
screen = pygame.Surface((400, 400))
player = pygame.Surface((40, 40))
zet = pygame.Surface((40, 40))
arrow = pygame.Surface((20, 40))
count = 0
player.set_colorkey((0, 0, 0))
zet.set_colorkey((0, 0, 0))
arrow.set_colorkey((0, 0, 0))
img_bullet = pygame.image.load('bullet.png')
img_player = pygame.image.load('player.png')
img_target = pygame.image.load('target.png')
img_bg = pygame.image.load('background.png')
myfont = pygame.font.SysFont('monospace', 30)
x_a = 1000
y_a = 1000
strike = False

x_z = 0
y_z = 0
x_p = 0
y_p = 360
right = True
done = False
while not done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
            y_p += 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            y_p -= 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            x_p -= 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            x_p += 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            if not strike:
                strike = True
                x_a = x_p
                y_a = y_p - 30

    if strike:
        y_a -= 3
        if y_a < 0:
            strike = False
            y_a = 1000
            x_a = 1000
    if inter(x_a, y_a, x_z, y_z, 20, 40):
        count += 1
        strike = False
        y_a = 1000
        x_a = 1000

    if right:
        x_z += 1
        if x_z > 400:
            x_z -= 1
            right = False
    else:
        x_z -= 1
        if x_z < 0:
            x_z += 1
            right = True
    string = myfont.render('Очки: ' + str(count), 0, (255, 0, 0))
    screen.blit(img_bg, (0, 0))
    arrow.blit(img_bullet, (0, 0))
    player.blit(img_player, (0, 0))
    zet.blit(img_target, (0, 0))
    screen.blit(string, (0, 50))
    screen.blit(arrow, (x_a, y_a))
    screen.blit(zet, (x_z, y_z))
    screen.blit(player, (x_p, y_p))
    window.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()
