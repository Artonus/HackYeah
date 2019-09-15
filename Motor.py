import math
import ConectionManager


class Motor():
    def getPosition(self):
        return self.position

    def update(self, x):
        #apply x to motor
        #read state of motore
        return self.position
    
    def __init__(self, x):
        self.position = x
        