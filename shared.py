import pygame
pygame.init()

#Framerate
framerate = 30

#Gamestate (0 = Main menu 1 = Game, 2 = Game Over)
gameState = 0

#Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
brownBinColour = (150,75,0)
blueBinColour = (13,120,190)
LightBlue = (154,192,205)

#Dimensions
WIDTH = 1300
HEIGHT = 800


#Recycling rules dictionary and list of waste
wasteTypes = ('blue','white','brown','black')
wasteList = []
selectedIndex = 0
nextChange = framerate * 0.5

#Fonts
#This font is the main font used in the game
font = pygame.font.Font('PixeloidSans.ttf',32)
#Larger font used for menus and game over
fontBig = pygame.font.Font('PixeloidSans.ttf',52)

#Score, High Score, lives and mistakes
lives = 3
currentScore = 0
highScore = 0
mistakes = []

#Interarrival
previous = 200
nextArrival = 0 

#Movment
velocity = 4
gravity = 2
left = False
right = False

#Settings (with default values)
music = True
soundEffects = True
masterVolume = 100
disabledSound = False
