import pygame
# creating windows
pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# creating char.
x = 50
y = 50
width = 25
height = 25
vel = 10
start = True

# starting window
while start:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
# key binding
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((255, 255, 255))
        # creating window
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()