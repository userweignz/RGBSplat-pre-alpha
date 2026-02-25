from ursina import * 
from ursina.prefabs.first_person_controller import *
import math
from random import randint


app = Ursina()

bullets = []
splats = []
npcs = []



score = 0
score_str = str(score)
player = FirstPersonController()
player.fov = 90
player.speed = 10


Sky()

timer = 1

mouse.locked = True
mouse.visible = False




walk_bob_amount = 0.05 
walk_bob_speed = 16    
walk_bob_timer = 0

default_cam_y = player.camera_pivot.y

player.jump_height = 2      
player.jump_duration = 0    
player.gravity = 0.98

npc_speed = 5