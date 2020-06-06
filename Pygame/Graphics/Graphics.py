#The goal of this file is to generate a pygame from
#Then within that pygram frame, loop through an animation
#Which we dynamically retrieve from the Sprites folder
from PIL import Image
import os, pygame, pathlib, glob
from os import path

pygame.init()

displayW = 600
displayH = 400
black = (0,0,0)
white = (255,255,255)
crashed = False
images = []
userX = 0
userY = 0
frame = 0

filePath = str(pathlib.Path().absolute())
spritePath = os.fsencode(filePath +  '\\Pygame\\Graphics\\Sprites\\')
gameDisplay = pygame.display.set_mode((displayW,displayH))
pygame.display.set_caption('Animation Testing')
clock = pygame.time.Clock()
runImg = pygame.image.load('Pygame\\Graphics\\Sprites\\tile0.png')

for image in os.listdir(spritePath):
    name = os.fsdecode(image)
    if name.endswith(".png"):
        images.append(name)

def runner(x, y, Img):
    gameDisplay.blit(Img, (x,y))

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    if(frame != len(images) -1):
        frame += 1
    else:
        frame = 0
    runImg = pygame.image.load('Pygame\\Graphics\\Sprites\\' + images[frame])
    gameDisplay.fill(white)
    runner(userX, userY, runImg)
    pygame.draw.rect(gameDisplay,(0,0,255),(displayW - 10, displayH - 10, 10,10))
    pygame.display.update()
    clock.tick(10)

pygame.quit()
quit()

