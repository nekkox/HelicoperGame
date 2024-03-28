import pygame
import random

class Helicopter():
    def __init__(self, x, y, screen):
        self.x=x
        self.y=y
        self.wys = 30
        self.szer = 50
        self.ksztalt = pygame.Rect(self.x, self.y, self.szer, self.wys)
        self.screen = screen
   
   
   
    def draw(self):
        pygame.draw.rect(self.screen, (255,0,0), self.ksztalt,1)
       
   
   
    def ruch(self, v):
        self.y=self.y+v
        self.ksztalt = pygame.Rect(self.x, self.y, self.szer, self.wys)
        
        
   
   
   

    
