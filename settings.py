# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:31:42 2020

@author: Lc
"""

class Settings():
    def __init__(self):
        #screen settings
        self.screen_width=1280
        self.screen_height=720
        #ship settings       
        self.ship_limit=3
        #bullet settings
        self.bullet_width=4
        self.bullet_height=18
        self.bullet_color=0,0,0
        self.bullets_allowed=5
        #alien settings        
        self.fleet_drop_speed=10
        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()  
        
    def initialize_dynamic_settings(self):
        self.ship_speed_factor=5.5
        self.bullet_speed_factor=12
        self.alien_speed_factor=2
        self.fleet_direction=1
        self.alien_points=50
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points =int(self.alien_points*self.score_scale)
        