import pygame
import sys
pygame.init()
bg_size = width, height = (600, 200)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("小恐龙")
dinosaur_image = pygame.image.load('./dinosaur.png').convert_alpha()
dinosaur_rect = dinosaur_image.get_rect()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_pressed = pygame.key.get_pressed()
    screen.fill(WHITE)
    screen.blit(dinosaur_image, (10, 100))
    pygame.display.flip()
    clock.tick(50)
