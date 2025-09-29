#Importing external modules and libraries
import pygame
import window, shared, waste, score, button

#Initialise pygame
pygame.init()

#Sets up the clock
clock = pygame.time.Clock()
#Gets the previous high score
Score = score.Score
Score.getHighScore()

#Sound used to test if sounds are enabled
try:
    sound = pygame.mixer.Sound('startUpSound.wav')
    sound.set_volume(shared.masterVolume / 100)
    sound.play()
except:
    #Will disable sounds if an error occurs when trying to
    #play the start up sound
    shared.music = False
    shared.soundEffects = False
    shared.disabledSound = True

#Main game loop
def playGame():
    #generates first bit of waste
    waste.generateWaste()
    #Updates the screen
    window.screen.update(shared.currentScore,shared.highScore,shared.wasteList[shared.selectedIndex].wasteType,shared.wasteList[shared.selectedIndex].wasteName,shared.lives)

    #USER INPUT
    keys = pygame.key.get_pressed()

    #Listens for space bar input
    if keys[pygame.K_SPACE]:
        #If space is pressed it changes the item of waste that is selected
        shared.wasteList[shared.selectedIndex].select(False)
        #This code limits the amount of times the waste selected can be changed
        #Now the selected waste can only be changed every half a second
        if shared.nextChange <= 0:
            shared.nextChange = shared.framerate * 0.5
            if shared.selectedIndex < len(shared.wasteList) - 1:
                shared.selectedIndex += 1
            else:
                shared.selectedIndex = 0

    #Listens for left right input
    if keys[pygame.K_LEFT]:
        #If pressed left vairable set to True and right to False
        shared.left = True
        shared.right = False
    elif keys[pygame.K_RIGHT]:
        #If right is pressed right vairable set to True and left to False
        shared.right = True
        shared.left = False
    else:
        #If no key is pressed both left and right are set to false
        shared.left = False
        shared.right = False

    #Sets the attribute selected for the selected rubbish object to true
    shared.wasteList[shared.selectedIndex].select(True)

    shared.nextChange -= 1
    
    for i in range(0,len(shared.wasteList)):
        #Updates all of the objects in the waste list
        shared.wasteList[i-1].update(shared.left,shared.right)
        
    #Game over sequence
    if shared.lives <= 0:
        #Plays game over sound effect
        if shared.soundEffects:
            sound = pygame.mixer.Sound('gameOver.wav')
            sound.set_volume(shared.masterVolume / 100)
            sound.play()
        #Update screen one final time
        window.screen.update(shared.currentScore,shared.highScore,shared.wasteList[shared.selectedIndex].wasteType,shared.wasteList[shared.selectedIndex].wasteName,shared.lives)
        window.screen.gameOver(shared.currentScore,shared.highScore,shared.mistakes)
        #Updates gameState to game over state
        shared.gameState = 2
    
    #Draws the bins to the screen
    window.screen.drawBins()


#Main loop
while True:
    #Maintains Frame Rate
    clock.tick(shared.framerate)
    if shared.gameState == 0:
        #Plays music if none is playing
        if pygame.mixer.music.get_busy() == False and shared.music:
            pygame.mixer.music.load('mainMenuMusic.mp3')
            pygame.mixer.music.play()
        #Main menu
        window.screen.mainMenu()
        #Draws all main menu buttons to screen
        for buttons in button.mainMenuButtons:
            buttons.update()
            
    elif shared.gameState == 1:
        if pygame.mixer.music.get_busy() == False and shared.music:
            pygame.mixer.music.load('gameMusicSlow.mp3')
            pygame.mixer.music.play()
        #Main game function
        playGame()
        #Draws all game screen buttons to screen
        for buttons in button.gameScreenButtons:
            buttons.update()
        
    elif shared.gameState == 2:
        if pygame.mixer.music.get_busy() == False and shared.music:
            pygame.mixer.music.load('gameMusicSlow.mp3')
            pygame.mixer.music.play()
        #Updateds screen
        window.screen.update(shared.currentScore,shared.highScore,shared.wasteList[shared.selectedIndex].wasteType,shared.wasteList[shared.selectedIndex].wasteName,shared.lives)
        #Draws game over screen
        window.screen.gameOver(shared.currentScore,shared.highScore,shared.mistakes)
        #Draws bins
        window.screen.drawBins()
        #Draws all the buttons to screen
        for buttons in button.gameOverButtons:
            buttons.update()
            
    #Quits the game if the x is pressed on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Updates the screen
    pygame.display.flip()
    

