import pygame
import random

class Obstactle:
    def __init__(self, x, szerokosc, screen):
        self.screen=screen
        self.x=x
        self.szerokosc = szerokosc
        self.y_gora = 0
        self.wys_gora = random.randint(150,250)
        self.odstep = 200
        self.y_dol = self.wys_gora + self.odstep
        self.wys_dol = self.screen.get_height() - self.y_dol
        self.color = (160,140,190)
        self.ksztalty_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.wys_gora)
        self.ksztalty_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.wys_dol)

        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.ksztalty_gora,0)
        pygame.draw.rect(self.screen, self.color, self.ksztalty_dol,0)
    
    def ruch(self,v):
        
        self.x = self.x -v
        self.ksztalty_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.wys_gora)
        self.ksztalty_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.wys_dol)
    
    def kolizja(self, helicopter):
        if self.ksztalty_gora.colliderect(helicopter) or self.ksztalty_dol.colliderect(helicopter):
            return True
        else:
            return False
        