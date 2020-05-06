# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:01:40 2020

@author: Lc
"""

import pygame
from pygame import mixer
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf




#inizializza una finestra
pygame.init()
ai_settings=Settings()
screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
pygame.display.set_caption("Alien Invasion")
play_button=Button(ai_settings,screen, "Play")
icon=pygame.image.load('images/icon.png')
background=pygame.image.load('images/background.jpg')
pygame.display.set_icon(icon)
bb_sound=mixer.music.load('sounds/background.wav')
mixer.music.play(-1)
stats=GameStats(ai_settings)
sb=Scoreboard(ai_settings,screen,stats)
ship = Ship(ai_settings,screen)
bullets=Group()
aliens=Group()
gf.create_fleet(ai_settings,screen,ship,aliens)
alien=Alien(ai_settings,screen)
#start loop
while True:
    gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)
    if stats.game_active:
        ship.update()
        gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)   
        gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)    
    gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button,background)    
   
    
       