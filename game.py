import pygame
import random
from pygame.locals import *
import pprint

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
snow_list=[]
image1 = 'corso.jpg'
image2 = 'corso2.jpg'


pygame.init()


# Set the width and height of the screen [width, height]
size = (500, 500)
screen = pygame.display.set_mode(size)


background = pygame.image.load(image1).convert()
mouse_cursor = pygame.image.load(image2).convert_alpha()

#ob = pygame.draw.rect(screen, RED, [0, 0, 100, 100],2)

# Starting position of the rectangle
rect_x = 50
rect_y = 50

# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5

square = pygame.Surface((rect_x,rect_x))

pygame.display.set_caption("My Game")
sprite = pygame.sprite.Sprite()

print(sprite)
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
myX=0
myY=0

#Generating Snow
for i in range(50):
 x = random.randrange(0, 500)
 y = random.randrange(0, 500)
 snow_list.append([x, y])
 
 
def napisz(text, x, y, size):
    cz = pygame.font.SysFont("Arial", size)
    rend = cz.render(text, 1, RED)
    screen.blit(rend, (x,y))

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
            
    # --- Game logic should go here
    
    # --- Drawing code should go here
    
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    screen.blit(background, (0,0))
   
    #square.fill(RED)
    #screen.blit(square,(rect_x,rect_x))
    #pygame.draw.rect(screen, GREEN, [10, 10, 50, 50])
   
    napisz("Hello World",150,100,20)
   
   
    #x-= mouse_cursor.get_width() / 2
    #y-= mouse_cursor.get_height() / 2
    
   
    if event.type == pygame.MOUSEBUTTONDOWN:
        x1,y2=pygame.mouse.get_pos()
        dogRec = mouse_cursor.get_rect()
        myX=x1 - (dogRec.width//2)
        myY=y2 - (dogRec.height//2)
        
    if x is not 0 and y is not 0:    
        screen.blit(mouse_cursor, (myX, myY))
        #screen.blit(mouse_cursor, (x, y))
    #x, y = pygame.mouse.get_pos()
    #x -= mouse_cursor.get_height() / 2
    #screen.blit(mouse_cursor, (x, y))
    pygame.draw.rect(screen,WHITE,[rect_x,rect_y,50,50])
   
   
   # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y
    
    coords = (rect_x, rect_y)
    
    if rect_y > 450:
        rect_change_y = rect_change_y * -1
        rect_change_x = rect_change_x * -1
    if rect_y < 0:
        rect_change_y = rect_change_y * -1
        rect_change_x = rect_change_x * -1
    
    for i in range(len(snow_list)):
    # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], random.randrange(0,4))
        snow_list[i][1] += 1
        if snow_list[i][1]>500:
            y=random.randrange(-50, -10)
            snow_list[i][1] = y
            x = random.randrange(0, 500)
            snow_list[i][0] = x
    
    
    #pygame.draw.rect(screen, RED, ob, 2)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    

    # --- Limit to 60 frames per second
    clock.tick(60)
print(snow_list)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

