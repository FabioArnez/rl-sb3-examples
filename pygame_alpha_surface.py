import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Transparency Example')

# Create a surface with transparency
surface_with_transparency = pygame.Surface((200, 200), pygame.SRCALPHA)
surface_with_transparency.fill((0, 0, 255, 128))  # Fill with blue color and 50% transparency

# Create a surface without transparency
surface_without_transparency = pygame.Surface((200, 200))
surface_without_transparency.fill((255, 0, 0))  # Fill with red color

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the surface with transparency
    screen.blit(surface_with_transparency, (50, 50))

    # Draw the surface without transparency
    screen.blit(surface_without_transparency, (300, 300))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()