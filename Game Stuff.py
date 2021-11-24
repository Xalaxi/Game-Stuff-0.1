# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:40:38 2021

@author: armaan21
"""
import pygame
import numpy as np


pygame.init()

step = 25
wobble = 10

Hasan = ['Hasan', 11, 8, 9, 8, 9]
Armaan = ['Armaan', 10, 8, 6, 7, 4]
Ani = ['Ani', 17, 9, 3, 7, 4]

fps = 30
fpsclock = pygame.time.Clock()

EVENTS = pygame.event.get()
key_input = pygame.key.get_pressed()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,255,0)
green = (0,0,255)
grey = (200,220,220)
yellow = (255,211,0)

background_colour = white
speed = [0,0]
size = width, height = 1000, 800
imgsize = (200,200)

leftinitial = [100, 150]
rightinitial = [700, 150]

font = pygame.font.Font("freesansbold.ttf", 100)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('Testing')

Armaanimg = pygame.image.load("Armaan Icon.png")
Armaanimg = pygame.transform.scale(Armaanimg, imgsize)
Armaanrect = Armaanimg.get_rect()

Aniimg = pygame.image.load("Ani Icon.jfif")
Aniimg = pygame.transform.scale(Aniimg, imgsize)
Anirect = leftinitial

Hasanimg = pygame.image.load("Hasan Icon.jfif")
Hasanimg = pygame.transform.scale(Hasanimg, imgsize)
Hasanrect = rightinitial

fireimg = pygame.image.load("fireball.png")
fireimg = pygame.transform.scale(fireimg, (50,50))
firerect = [150,250]

# pygame.mouse.set_cursor(*pygame.cursors.broken_x)

text = font.render("Ani used Fireball!",True,black,grey)
text2 = font.render("Hasan used Smite!",True,black,grey)

running = True

while running:
    screen.fill(background_colour)
    
    pygame.draw.rect(screen, grey, (0, 400,1000,600))
    
    screen.blit(Aniimg, Anirect)
    screen.blit(Hasanimg, Hasanrect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()

    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_a]:
        for x in range(500):
            screen.fill(background_colour)
            pygame.font.init()
            
            pygame.draw.rect(screen, (200,220,220), (0, 400,1000,600))
            screen.blit(Aniimg, leftinitial)
            screen.blit(Hasanimg, [700,150])
            screen.blit(text, (50,500))
            
            firerect[0] += 1.1
            screen.blit(fireimg,firerect)
            pygame.display.update()
        pygame.font.quit()
        firerect = [150,250]
    
    if key_input[pygame.K_j]:
        for x in range(300):
            screen.fill(background_colour)
            pygame.font.init()
            
            pygame.draw.rect(screen, (200,220,220), (0, 400,1000,600))
            screen.blit(text2, (50,500))
            screen.blit(Aniimg, leftinitial)
            
            
            Hasanrect[0] -= 1.1
            screen.blit(Hasanimg,Hasanrect)
            pygame.display.update()
        for x in range(300):
            pygame.draw.arc(screen,yellow,(200,50,500,250),np.pi/2,1.5*np.pi,10)
            pygame.display.update()
        pygame.font.quit()
        Hasanrect = [700,150] 
        
    pygame.display.update()
    fpsclock.tick(fps)
    pygame.display.flip()