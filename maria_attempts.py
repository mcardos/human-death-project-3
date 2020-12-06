import pygame

# Step 1: Initialize Game Screen
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Healthfy')
# Add background
background = pygame.image.load("/home/mcardoso/project-3-healthfy/Images/background.jpg")
clock = pygame.time.Clock()
RUNNING = True
while RUNNING:
    # clock.tick(240)
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        # Add inactive 'buttons' 
    pygame.draw.rect(screen, (0, 0, 0), (300, 375, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (300, 315, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (200, 375, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (100, 315, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (100, 375, 50, 50))
    pygame.display.flip()
pygame.display.update()
pygame.quit()
