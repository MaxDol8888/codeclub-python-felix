#!/usr/bin/env python
"""
This is a Python / PyGame version of "Felix and Herbert" for CodeClub
"""

#Import Modules
import pygame, codeclub
from pygame.locals import *

def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything
    pygame.init()
    screensize = (800, 600)
    screen = pygame.display.set_mode(screensize)
    pygame.mouse.set_visible(0)

#create the wallpaper, and make it fill the screen
    wallpaper = codeclub.load_image('hall.jpg')
    wallpaper = pygame.transform.scale(wallpaper, (screensize))
    background = pygame.Surface(screensize)
    background.blit(wallpaper, (0, 0))
    
#Prepare Game Objects
    clock = pygame.time.Clock()
    felix = codeclub.sprite()
    felix.set_costume('cat1-a.gif', 100)
    herbert = codeclub.sprite()
    herbert.set_costume('mouse1.png', 60)
    allsprites = pygame.sprite.Group((herbert, felix))
    score = 0
    highscore = 0
    font = pygame.font.Font(None, 36)
    
#Main Loop
    while True:
        clock.tick(60)

    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return

    #Move the sprites
        felix.point_towards(herbert)
        felix.move_unless_frozen(2)
        herbert.move_to(pygame.mouse.get_pos())
        herbert.point_towards(felix)
        
    #See whether Felix has caught Herbert
        if felix.has_caught(herbert):
            felix.freeze(20)
            felix.say("I've got you!", 60)
            score = score - 1000
            if score < 0:
                score = 0
            
    #update score
        score = score + 1
        if score > highscore:
            highscore = score
                
    #Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        felix.speak(screen)
        score_text = font.render("Score :" + str(score), 1, (10, 10, 10))
        highscore_text = font.render("High Score :" + str(highscore), 1, (10, 10, 10))
        screen.blit(score_text, (0, 0))
        screen.blit(highscore_text, (0, 25))
        pygame.display.flip()

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
pygame.quit ()

