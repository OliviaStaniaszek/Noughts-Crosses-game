import pygame
SCREENWIDTH = 640
SCREENHEIGHT = 640
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
pygame.font.init()

# ---------------------colours-----------------
# light mode
BRASS = (203, 153, 126)
SAND = (221, 190, 169)
CHAMPAGNE = (255, 232, 214)
ARTICHOKE = (165, 165, 141)
EBONY = (107, 112, 92)

# dark mode
PRUSSIAN = (39, 59, 83)
VIOLET = (84, 69, 95)
MAGENTA = (151, 73, 90)
FUZZY = (227, 99, 103)
TAN = (230, 157, 117)

# ---------------------fonts-----------------
TITLEF = pygame.font.Font('fonts/Kreon-Medium.ttf', 60)
SUBF = pygame.font.Font('fonts/Marmelad-Regular.ttf', 40)
TEXTF = pygame.font.Font('fonts/Numans-Regular.ttf', 30)
XO = pygame.font.Font('fonts/Kreon-Medium.ttf', 150)

# ---------------------backgrounds-----------------
DARKBKG = pygame.image.load("imgs/darkbkg.png")
LIGHTBKG = pygame.image.load("imgs/lightbkg.png")
