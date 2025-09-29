import pygame, tkinter
import shared, window
#Initilises pygame
pygame.init()

class Button:
    def __init__(self,height,width,x,y,text,function):
        #Set up the position
        self.x = x
        self.y = y
        #Set up the dimensions
        self.width = width
        self.height = height
        #Text for the button
        self.text = text
        self.function = function

        #Starting colour
        self.mainColour = '#87B5C4'
        self.hoverColour = '#4C869A'

        #Creates button rectangle
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
        #Creates text rectangle 
        self.textCS = shared.fontBig.render(self.text,True,shared.BLACK)
        self.textRect = self.textCS.get_rect(center=(self.x + (self.width/2),self.y + (self.height/2)))

    def update(self):
        #Gets the position of the mouse
        mousePosition = pygame.mouse.get_pos()
        #Draws box
        pygame.draw.rect(window.screen.Screen, self.mainColour, pygame.Rect(self.x,self.y,self.width,self.height))
         
        #Use pygame collision function to change colour if the mouse hovers over button
        if self.rect.collidepoint(mousePosition):
            pygame.draw.rect(window.screen.Screen, self.hoverColour, pygame.Rect(self.x,self.y,self.width,self.height))
            #Detects if button clicked
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.function()
        #Draws box around button
        pygame.draw.rect(window.screen.Screen, shared.BLACK, pygame.Rect(self.x,self.y,self.width,self.height), width = 1)
        
        #writes text to the screen
        window.screen.Screen.blit(self.textCS,self.textRect)

def restart():
    
    #Displays tutorial if coming from main menu
    if shared.gameState == 0:
        
        #Enables the tutorial image
        displayTutorial = True
        #Loads tutorial image
        tutorial = pygame.image.load('tutorial.png')
        
        while displayTutorial:
            
            #Displays tutorial image
            window.screen.Screen.blit(tutorial,(250,100))
            pygame.display.flip()

            #USER INPUT
            keys = pygame.key.get_pressed()
            
            #Stops displaying tutorial when spacebar is clicked
            if keys[pygame.K_SPACE]:
                displayTutorial = False

            #Plays music if none is playing
            if pygame.mixer.music.get_busy() == False and shared.music:
                pygame.mixer.music.load('mainMenuMusic.mp3')
                pygame.mixer.music.play()

            #Quits the game if the x is pressed on the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
    #Plays Click Sound effect
    if shared.soundEffects:
        sound = pygame.mixer.Sound('clickSound.wav')
        sound.set_volume(shared.masterVolume / 100)
        sound.play()
    #Stops music
    pygame.mixer.music.stop()
    #Resets vairables so game can be played again
    shared.currentScore = 0
    shared.lives = 3
    shared.gameState = 1
    shared.wasteList = []
    shared.mistakes = []
    shared.selectedIndex = 0
    shared.previous = 200
    shared.nextArrival = 0

def mainMenu():
    #Plays Click Sound effect
    if shared.soundEffects:
        sound = pygame.mixer.Sound('clickSound.wav')
        sound.set_volume(shared.masterVolume / 100)
        sound.play()
    #Stops Music
    pygame.mixer.music.stop()
    #Sets the game state to the main menu game state
    shared.gameState = 0


def settings():
    #Plays Click Sound effect
    if shared.soundEffects:
        sound = pygame.mixer.Sound('clickSound.wav')
        sound.set_volume(shared.masterVolume / 100)
        sound.play()
    #Set up new tkinter window
    settingsWindow = tkinter.Tk()
    settingsWindow.title('Settings')
    settingsWindow.geometry('300x220')
    settingsWindow.iconbitmap("settingsImage.ico")
    
    def closeMenu():
        #Plays Click Sound effect
        if shared.soundEffects:
            sound = pygame.mixer.Sound('clickSound.wav')
            sound.set_volume(shared.masterVolume / 100)
            sound.play()
        #Sets new volume for music
        pygame.mixer.music.set_volume(var3.get() / 100)
        #Updates settings
        shared.music = var1.get()
        if var1.get() == False:
            pygame.mixer.music.stop()
        shared.soundEffects = var2.get()
        shared.masterVolume = var3.get()
        #Closes window
        settingsWindow.destroy()
        
    #Setting up tkinter vairables
    var1 = tkinter.BooleanVar(value = shared.music) #Checkbox1
    var2 = tkinter.BooleanVar(value = shared.soundEffects) #Checkbox2
    var3 = tkinter.IntVar(value = shared.masterVolume) #Slider


    #Title for the GUI
    title = tkinter.Label(text="Settings",font = 40)
    
    
    #Back button
    button = tkinter.Button(
        text = 'Back',
        width = 40,
        height = 2,
        bg = '#87B5C4',
        fg = 'black',
        command = closeMenu
    )

    if shared.disabledSound == False:
        #Label for volume slider
        volumeLabel = tkinter.Label(text="Master Volume",font = 20)
        
        #Checkboxes
        c1 = tkinter.Checkbutton(
            settingsWindow,
            text = 'Music',
            variable = var1,
            onvalue = True,
            offvalue = False,
            font = 20
        )

        c2 = tkinter.Checkbutton(
            settingsWindow,
            text = 'Sound Effects',
            variable = var2,
            onvalue = True,
            offvalue = False,
            font = 20,
        )

        #Sliders
        slider1 = tkinter.Scale(
            settingsWindow,
            variable = var3,
            from_ = 0,
            to = 100,
            orient = tkinter.HORIZONTAL
        )

        #Packing Widgets
        title.pack(pady = 10)
        c1.pack()
        c2.pack()
        volumeLabel.pack()
        slider1.pack()
        button.pack()

    else:
        #Displays error message in the settigns window if sounds are disabled
        message = tkinter.Label(text="Sounds are not available on this device.",font = 40)
        
        title.pack(pady = 10)
        message.pack(pady = 50)
        button.pack()

    #Begins main loop
    settingsWindow.mainloop()



gameOverButtons = [Button(90,620,330,460,'Play Again',restart),Button(90,620,330,563,'Main Menu',mainMenu)]
mainMenuButtons = [Button(180,620,330,270,'Play Game',restart),Button(90,560,360,480,'Settings',settings)]
gameScreenButtons = [Button(90,380,900,690,'Settings',settings),Button(90,380,900,590,'Main Menu',mainMenu)]
