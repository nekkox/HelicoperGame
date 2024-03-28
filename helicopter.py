import pygame
from pygame.locals import *
from obstacle import Obstactle
from heli import Helicopter
import datetime
import math

pygame.init()

# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Game")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def napisz(text, x, y, size):
    cz = pygame.font.SysFont("Arial", size)
    rend = cz.render(text, 1, RED)
    screen.blit(rend, (x,y))

points = 0
last_increment_time = datetime.datetime.now()

def increment_points():
    global points, last_increment_time
    current_time = datetime.datetime.now()
    elapsed_seconds = (current_time - last_increment_time).total_seconds()
    if elapsed_seconds >= 10:
        points += 1
        print("Points:", points)
        last_increment_time = current_time
        
#co_pokazuje = "gra"
co_pokazuje = "menu"


Przeszkody=[]
for i in range(35):
    Przeszkody.append(Obstactle(i*500/20, 500/20, screen))


# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
Scores = []

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                dy =- 1
            if event.key == pygame.K_DOWN:
                dy = 1
            if event.key == pygame.K_SPACE:
                if co_pokazuje !="gra":
                    helicoper = Helicopter(250,275,screen)
                    dy = 0
                    co_pokazuje = "gra"
                    punkty = 0

            
            
    # --- Game logic should go here
    screen.fill((0,0,0))
    if(co_pokazuje == "menu"):
        napisz("Naciśnij spację aby zacząć", 80, 150,20)

    
    # --- Drawing code should go here
    
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    
    elif(co_pokazuje == "gra"):
        
        obstacles_to_remove = []

        for p in Przeszkody:
            p.draw()
            p.ruch(1) 
            if p.kolizja(helicoper.ksztalt):
                print("BANG")
                Scores.append(punkty)
                co_pokazuje = "koniec"
                #sys.exit(0)
                
            if(p.x <= -p.szerokosc):
                obstacles_to_remove.append(p)
                
        for obstacle in obstacles_to_remove:
            Przeszkody.remove(obstacle)
            Przeszkody.append(Obstactle(500, 500 / 20, screen))
            punkty = punkty + math.fabs(dy)
            print(f"Points:{punkty}" )
        
        
        helicoper.draw()
        helicoper.ruch(dy)
        napisz(str(punkty), 0, 0,20)
    
    elif co_pokazuje == "koniec":
        napisz("Niestety Przegrywasz", 100, 150,20)
        napisz("Naciśnij spację aby zacząć", 80, 250,20)
        napisz(f"Your Score is {Scores[-1]}", 80, 300,20)
        
    # --- Update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)


# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

