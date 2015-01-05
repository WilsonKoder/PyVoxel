__author__ = 'WilsonKoder'

import pygame
import sys

pygame.init()

windowSize = (800, 600)
window = pygame.display.set_mode(windowSize)
windowCaption = "Voxel Game!"
pygame.display.set_caption(windowCaption)

#game vars

clock = pygame.time.Clock()
running = True

# player

class Player:
    position = [0, 0]
    image = ""

    gravity = -0.03

    moveUp = False
    moveDown = False
    moveLeft = False
    moveRight = False

    def __init__(self, pos, imagePath):
        self.position = pos
        self.image = pygame.image.load(imagePath)

    def draw(self):
        window.blit(self.image, self.pos)

player = Player([100, 100], "res/images/player.png")
bg = pygame.image.load("res/images/bg.png")
cloud = pygame.image.load("res/images/cloud.png")
fillColor = (0, 0, 0)
clouds = []
clouds.append([[0, 30], 0.7])
clouds.append([[300, 100], 1.2])
clouds.append([[500, 30], 1])

class Block():
    pos = []
    image = ""
    def __init__(self, position, image):
        self.pos = position
        self.image = image

blocks = []
grassBlockImage = pygame.image.load("res/images/dirt_block.png")
dirtBlockImage = pygame.image.load("res/images/dirt_bottom_block.png")

def gen_world():
    xpos = -32
    ypos = 200
    for x in range(0, 25):
        ypos = 345
        xpos += 32
        for y in range(0, 7):
            ypos += 32
            if y > 0:
                block = Block([xpos, ypos], dirtBlockImage)
            else:
                block = Block([xpos, ypos], grassBlockImage)
            blocks.append(block)

gen_world()

moveLeft = False
moveRight = False
onGround = False

while running:
    clock.tick(60)

    playerX = player.position[0]
    playerY = player.position[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.gravity = 0.1
            if event.key == pygame.K_a:
                moveLeft = True
            elif event.key == pygame.K_d:
                moveRight = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moveLeft = False
            elif event.key == pygame.K_d:
                moveRight = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            mouseX = mousePos[0]
            mouseY = mousePos[1]
            for block in blocks:
                blockX = block.pos[0]
                blockY = block.pos[1]
                if mouseX < blockX + 25 and mouseX + 25 > blockX and mouseY < blockY + 25 and mouseY + 25 > blockY:
                    # collision detected
                    blocks.remove(block)
            for block in blocks:
                blockX = block.pos[0]
                blockY = block.pos[1]

                if not blockX < playerX + 30 and blockX + 30 > playerX and blockY < playerY + 30 and blockY + 30 > playerX:
                    player.gravity = -0.03

    for block in blocks:
        blockX = block.pos[0]
        blockY = block.pos[1]

        if blockX < playerX + 33 and blockX + 33 > playerX and blockY < playerY + 33 and blockY + 33 > playerX:
            player.gravity = 0
            onGround = True
        else:
            onGround = False
            player.position[1] -= player.gravity

    if player.gravity > -0.03:
        if player.gravity != 0:
            player.gravity -= 0.015



    if moveLeft:
        player.position[0] -= 5
    elif moveRight:
        player.position[0] += 5

        #if playerX < blockX + 32 and playerX + 32 > blockX and playerY < blockY + 32 and blockY + 32 > playerY:

    window.fill(fillColor)
    window.blit(bg, (0, 0))
    window.blit(text, (400, 300))
    for cloudPos in clouds:
        cloudPos[0][0] += cloudPos[1]
        if cloudPos[0][0] > 1200:
            cloudPos[0][0] = -400
        window.blit(cloud, cloudPos[0])

    for block in blocks:
        window.blit(block.image, block.pos)

    window.blit(player.image, [playerX, playerY])

    pygame.display.flip()

pygame.quit()
sys.exit()