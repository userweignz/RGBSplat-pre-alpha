from ursina import * 
from world_setgs import *


scoreui = Entity(
    model='quad',              
    texture='textures/sb.png',
    parent=camera.ui,
    scale=(0.3,0.2),               
    position=(-0.74, 0.4, 0)         
)

lrgbui = Entity(
    model='quad',              
    texture='textures/lrgb.png',
    parent=camera.ui,
    scale=(0.3,0.2),               
    position=(0.74, 0.4, 0)         
)


scoretext = Text(score_str, position=(-0.85, 0.45), scale=5, color=color.red)
    

    
room1f = Entity(
    model='models/room1floor.obj',
    texture='textures/floor.png',
    texture_scale=(10, 4),
    double_sided=True,
    scale=2,
    z=3,
    color=color.white,
    collider='mesh'
)
  
ground = Entity(
    model='models/room1walls.obj',
    texture='textures/wall.png',
    texture_scale=(4, 1),
    double_sided=True,
    scale=2,
    z=3,
    color=color.white,
    collider='mesh'
)



redgun = Entity(parent=player, rotation_y=-100)

rg_main = Entity(
    model='models/redgun_main.obj',
    color=color.gray,
    parent=redgun,
    scale=(0.1, 0.1, 0.1),
    position=(-1.4,-0.2,-0.5)
)
rg_barrel = Entity(
    model='models/redgun_barrel.obj',
    color=color.white,
    parent=redgun,
    scale=(0.1, 0.1, 0.1),
    position=(-1.4,-0.2,-0.5)
)
rg_paint = Entity(
    model='models/redgun_paint.obj',
    color=color.red,
    parent=redgun,
    scale=(0.1, 0.1, 0.1),
    position=(-1.4,-0.2,-0.5)
)

redsplat = Entity(
    model='plane',
    texture='textures/splat.png',
    color=color.red
    )