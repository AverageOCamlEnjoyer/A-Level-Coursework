import pygame, textwrap
import shared
#Import libraries

class Window():
    def __init__(self,width,height,bgColour):
        self.width = width      #Sets Attributes for window
        self.height = height
        self.bgColour = bgColour
        self.Screen = pygame.display.set_mode((width,height))
        #Import logo Image
        self.logo = pygame.image.load('background.png')
        pygame.display.set_caption('Recycle Rush') #Sets the caption for the display
        #Set display icon
        self.pygameIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(self.pygameIcon)

    #This code splits the string into sections of a set length whilst keeping the words together
    def textWrapper(self,message,maxLength,xStart,yStart,lineSpacing):
        #Initilising vairables
        self.lineSpacing = lineSpacing
        self.wrapMessage = message
        self.maxLenght = maxLength
        self.xStart = xStart
        self.yStart = yStart
        self.i = 0
        self.total = len(self.wrapMessage[0])
        self.splitMessage = []
        self.section = self.wrapMessage[self.i]
        
        while self.i < len(self.wrapMessage)-1:
            self.total += len(self.wrapMessage[self.i+1]) + 1
            #This determins thie line length
            if self.total <= maxLength:
                self.section += ' ' + self.wrapMessage[self.i+1]
                self.i += 1
            else:
                self.splitMessage.append(str(self.section))
                self.section = self.wrapMessage[self.i+1]
                self.total = len(self.wrapMessage[self.i+1])
                self.i += 1
        #Adds final line to the array
        self.splitMessage.append(str(self.section))

            
        self.line = 0
        for n in self.splitMessage:     
            self.wrappedText = shared.font.render(str(n),True,shared.BLACK)
            self.textRect = self.wrappedText.get_rect()
            #Writes the text to the screen moving down from the last line
            self.textRect = (self.xStart,self.yStart + (self.line*self.lineSpacing))
            self.Screen.blit(self.wrappedText,self.textRect)
            #Keeps track of the line number
            self.line += 1
        
    def drawHUD(self,currentScore,highScore,wasteType,wasteName,lives):

        #Draws the rectangle that will contain information about score, high score and lives
        pygame.draw.rect(self.Screen, shared.LightBlue, pygame.Rect((shared.WIDTH-410),10,400,250))
        pygame.draw.rect(self.Screen, shared.BLACK, pygame.Rect((shared.WIDTH-410),10,400,250), width = 1)
        #Draws the rectangle that will contain infromation about the waste selected
        pygame.draw.rect(self.Screen, shared.LightBlue, pygame.Rect((shared.WIDTH-410),270,400,(shared.HEIGHT-280)))
        pygame.draw.rect(self.Screen, shared.BLACK, pygame.Rect((shared.WIDTH-410),270,400,(shared.HEIGHT-280)), width = 1)
        #Draws the rectangle that will be the game area
        pygame.draw.rect(self.Screen, shared.LightBlue, pygame.Rect(10,10,870,780))
        pygame.draw.rect(self.Screen, shared.BLACK, pygame.Rect(10,10,870,780), width = 1)
        
        #Imports image measuring 88 by 72
        self.Heart = pygame.image.load('heart.png')
        #Scales it up to 132 by 108
        self.Heart = pygame.transform.scale(self.Heart, (132,108))

        #Importa image measuring 88 by 72
        self.Dead = pygame.image.load('dead.png')
        #Scales it up to 132 by 108
        self.Dead = pygame.transform.scale(self.Dead, (132,108))

        #Assigning attributes
        self.currentScore = str(currentScore)
        self.highScore = str(highScore)
        self.wasteType = str(wasteType)
        self.wasteName = str(wasteName)
        self.lives = lives

        #Validation
        if int(self.currentScore) < 0:
            shared.currentScore = 0
        if self.lives < 0:
            shared.lives = 0
        if self.lives > 3:
            shared.lives = 3

        #Writes the the current score to the screen
        #Text is created with the font defined in the shared file
        self.textCS = shared.font.render('Score: ' + self.currentScore,True,shared.BLACK)
        self.textRect = self.textCS.get_rect()
        self.textRect = (shared.WIDTH - 400,35)
        self.Screen.blit(self.textCS,self.textRect)

        #Writes the high score to the screen
        #Text is created with the font defined in the shared file
        self.textHS = shared.font.render('High Score: ' + self.highScore,True,shared.BLACK)
        self.textRect = self.textHS.get_rect()
        self.textRect = (shared.WIDTH - 400,80)
        self.Screen.blit(self.textHS,self.textRect)

        #Draws hearts to the screen to indicate the number of lives
        if self.lives >= 1:
            self.Screen.blit(self.Heart,(shared.WIDTH - 390,152))
        else:
            self.Screen.blit(self.Dead,(shared.WIDTH - 390,152))
            
        if self.lives >= 2:
            self.Screen.blit(self.Heart,(shared.WIDTH - 278,152))
        else:
            self.Screen.blit(self.Dead,(shared.WIDTH - 278,152))
            
        if self.lives >= 3:
            self.Screen.blit(self.Heart,(shared.WIDTH - 168,152))
        else:
            self.Screen.blit(self.Dead,(shared.WIDTH - 168,152))

        #This section writes information about the rubbish to the screen

        #Validation, only creates message if waste is selected
        if self.wasteType != 'None':
            self.message = self.wasteName.upper() + ' should be recycled in the ' + self.wasteType.upper() + ' bin.'
        else:
            self.message = 'No waste selected'
            
        #Splitting the message into individual words
        self.message = self.message.split()
        self.textWrapper(self.message,20,shared.WIDTH - 400,305,50)
        


    def update(self,currentScore,highScore,wasteType,wasteName,lives):
        self.Screen.fill(self.bgColour) #Fills the screen with the background colour

        self.drawHUD(currentScore,highScore,wasteType,wasteName,lives)

    def drawBins(self):
        #Draws bins
        #Brown
        pygame.draw.rect(self.Screen, shared.brownBinColour, pygame.Rect(10,670,218,120))
        pygame.draw.rect(self.Screen, shared.BLACK, pygame.Rect(10,670,218,120), width = 1)
        #Blue
        pygame.draw.rect(self.Screen, shared.blueBinColour, pygame.Rect(228,670,217,120))
        pygame.draw.rect(self.Screen, shared.BLACK, pygame.Rect(228,670,217,120), width = 1)
        #White
        pygame.draw.rect(self.Screen, shared.WHITE, pygame.Rect(445,670,217,120))
        pygame.draw.rect(self.Screen, shared.BLACK, pygame.Rect(445,670,217,120), width = 1)
        #Black
        pygame.draw.rect(self.Screen, shared.BLACK, pygame.Rect(662,670,218,120))
        pygame.draw.rect(self.Screen, shared.BLACK, pygame.Rect(662,670,218,120), width = 1)

    def gameOver(self,currentScore,highScore,mistakes):
        #Draw game over pop-up
        pygame.draw.rect(self.Screen, shared.LightBlue, pygame.Rect(315,115,650,550))
        pygame.draw.rect(self.Screen, shared.BLACK, pygame.Rect(315,115,650,550), width = 1)
        #Text is created with the font defined in the shared file
        #Writes score to screen
        self.textCS = shared.fontBig.render('Score: ' + self.currentScore,True,shared.BLACK)
        self.textRect = self.textCS.get_rect()
        self.textRect = (320,115)
        self.Screen.blit(self.textCS,self.textRect)
        #Writes high score to creen
        self.textCS = shared.fontBig.render('High Score: ' + self.highScore,True,shared.BLACK)
        self.textRect = self.textCS.get_rect()
        self.textRect = (320,162)
        self.Screen.blit(self.textCS,self.textRect)
        #Limits the number of mistakes that can be written to the screen to three
        mistakes = mistakes[:3]
        #Wrties mistakes to the screen
        for i in range(len(mistakes)):
            shared.splitMistakes = shared.mistakes[i].split()
            #Adds the mistakes to the game over pop up
            #35 is the number of chars per line, 320,235 is the start x,y, 73 is the space
            #between sentances and 30 is the line spacing.
            self.textWrapper(shared.splitMistakes,35,320,235 + (73*i),30)

    def mainMenu(self):
        self.Screen.fill(self.bgColour)
        self.Screen.blit(self.logo,(0,0))
#Initilises the screen object with approximate golden aspect ratio and the colour white
screen = Window(shared.WIDTH,shared.HEIGHT,shared.WHITE)

