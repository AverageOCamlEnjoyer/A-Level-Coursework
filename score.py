import pygame
import shared

class Score():
    def __init__(self):
        #Initialises the high score as zero so that it can be updated
        self.highScore = 0
    def getHighScore(self):
        #Opens the text file in read mode
        self.file = open('highScore.txt','r')
        #Reads the high score from the text file
        self.highScore = int(self.file.readline())
        #Closes the file
        self.file.close()
        shared.highScore = self.highScore
    def updateScore(self, points):
        shared.currentScore = int(shared.currentScore) + int(points)
        #If the current score is more than the high score then
        #the high score is updated
        if shared.currentScore > self.highScore:
            #Opens the text file in write mode
            self.file = open('highScore.txt','w')
            #writes to the file
            self.file.write(str(shared.currentScore))
            #Closes the file
            self.file.close()
            #Updates the highscore vairable so the new value can be
            #written to the screen
            self.getHighScore()

Score = Score()


