import pygame, random
import shared, window, score

#initialize pygame
pygame.init()
pygame.mixer.init()


def arrival(previous):
    #Changes interarrival time by a random value
    new = previous + random.randint(-20,5)
    #Limits the time between arrivals to between 60 and 300 frames
    if new < 60:
        new = 60
    if new > 300:
        new = 300
    return new

def generateWaste():
    #Adds to a counter to compar to interarrival time
    shared.previous += 1
    if shared.previous >= shared.nextArrival:
        #Creates a new waste object
        shared.wasteList.append(Rubbish(shared.wasteTypes[random.randint(0,(len(shared.wasteTypes)-1))]))
        #Generates a new interarrival time
        shared.nextArrival = arrival(shared.previous)
        #Sets counter to zero
        shared.previous = 0

class Rubbish():
    def __init__(self,wasteType):
        self.wasteType = wasteType
        #Sets the intial x position randomly
        self.x = random.randint(10,760)
        #Sets the y position to the top of the screen
        self.y = 10
        #Intilises the waste as unselected
        self.selected = False
        
        #Assigns an image based on the waste type
        if self.wasteType == 'blue':
            value = random.randint(1,2)
            #selects a sprite categry
            if value == 1:
                self.image = pygame.image.load('paper'+str(random.randint(1,2))+'.png')
                self.wasteName = 'paper'
            else:
                self.image = pygame.image.load('cardboard'+str(random.randint(1,2))+'.png')
                self.wasteName = 'cardboard'
            
        if self.wasteType == 'white':
            value = random.randint(1,4)
            #selects a sprite categry
            if value == 1:
                self.image = pygame.image.load('glass'+str(random.randint(1,3))+'.png')
                self.wasteName = 'glass'
            elif value == 2:
                self.image = pygame.image.load('can'+str(random.randint(1,3))+'.png')
                self.wasteName = 'cans'
            elif value == 3:
                self.image = pygame.image.load('plasticBottle'+str(random.randint(1,3))+'.png')
                self.wasteName = 'plastic bottles'
            else:
                self.image = pygame.image.load('aerosols.png')
                self.wasteName = 'aerosols'

        if self.wasteType == 'black':
            #selects a sprite categry
            value = random.randint(1,2)
            if value == 1:
                self.image = pygame.image.load('crispPacket.png')
                self.wasteName = 'crisp packet'
            else:
                self.image = pygame.image.load('polystyrene.png')
                self.wasteName = 'polystyrene'
        if self.wasteType == 'brown':
                self.image = pygame.image.load('banana.png')
                self.wasteName = 'bananas'
                
        self.image = pygame.transform.scale(self.image, (120,120))

    def move(self,left,right):
        #Used to move left and right the speed at which this
        #happens is defined by the velocity in the shared file
        if self.selected == True:
            if left:
                self.x -= shared.velocity
                #Validation makes sure doesn't go out of bounds
                if self.x <= 10:
                    self.x = 10
            if right:
                self.x += shared.velocity
                #Validation makes sure doesn't go out of bounds
                if self.x >= 760:
                    self.x = 760
        #Move the waste down the screen
        self.y += shared.gravity

    def draw(self):
        #Blits image to the screen
        window.screen.Screen.blit(self.image,(self.x,self.y))
        
        if self.selected:
            #Draws a red square if selected
            pygame.draw.rect(window.screen.Screen, shared.RED, pygame.Rect(self.x,self.y,120,120), width = 1)

    def delete(self):
        #Checks if the waste has been put in the right bin
        #and updates score accordingly
        if ((self.x+60) <= 228) and ((self.x+60) >= 10):
            self.putIn = 'brown'
        elif ((self.x+60) <= 445) and ((self.x+60) > 228):
            self.putIn = 'blue'
        elif ((self.x+60) <= 662) and ((self.x+60) > 445):
            self.putIn = 'white'
        elif ((self.x+60) <= 880) and ((self.x+60) > 662):
            self.putIn = 'black'
        if self.wasteType == self.putIn:
            #Plays correct recycling sound if sounds are SFX are on
            if shared.soundEffects:
                sound = pygame.mixer.Sound('correctRecycle.wav')
                sound.set_volume(shared.masterVolume / 100)
                sound.play()
            score.Score.updateScore(100)
        #If it gets to here it has not been recycled correctly
        #so a life is deducted from the shared vairable
        else:
            #Plays incorrect recycling sound if sounds are SFX are on
            if shared.soundEffects:
                sound = pygame.mixer.Sound('incorrectRecycle.wav')
                sound.set_volume(shared.masterVolume / 100)
                sound.play()
            shared.mistakes.append('- ' + self.wasteName.upper() + ' should be put in the ' + self.wasteType.upper() + ' bin. (Not ' + self.putIn + ')')
            shared.lives -= 1
            
        #Removes the waste from the array
        shared.wasteList[shared.selectedIndex].select(False)
        if shared.selectedIndex > 0:
            #Updates the index of the selected object
            shared.selectedIndex -= 1
        shared.wasteList.remove(self)
    
    def update(self,left,right):
        #Triggers the move and draw methods
        self.move(left,right)
        self.draw()
        #Deletes the object when it goes off the screen
        #and checks it has been recycled correctly
        if self.y > 660 + shared.velocity:
            self.delete()
            

    def select(self,selected):
        #Updates if the object is selected
        self.selected = selected
