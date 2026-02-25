from ursina import * 
from ursina.prefabs.first_person_controller import *
import math
from random import randint
from world_setgs import *

def create_npc(npc_position, npc_color, size):
    npc = Entity(position=npc_position, scale=size)
    
    npc.body = Entity(
        model='models/body.obj',
        parent=npc,
        collider='mesh',
        color=npc_color
        )
    
    npc.face = Entity(  
        model='models/face.obj',
        parent=npc,
        
        color=color.black
    )
    
    npcs.append(npc)
    return npc

  
def create_bullet():
    bullet = Entity(
        model='sphere',
        color=color.red,
        collider='sphere',
        position=camera.world_position + camera.forward + Vec3(0.74,-0.4,0)
        )
    
    bullet.direction = camera.forward
    bullets.append(bullet)