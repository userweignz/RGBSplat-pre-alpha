from ursina import * 
from ursina.prefabs.first_person_controller import *
import math
from random import randint
from world_setgs import *
from logic import *
from world_ents import *



def update():
    
    
    ai_enabled = True
    
    global walk_bob_timer
    global velocity_y
    global timer
    global score
    
    timer += time.dt
    interval = 4.0
    
    if timer >= interval:
        create_npc((randint(-10,10),1,randint(-10,10)), color.red, 1)
        timer = 0
        
    desired_distance = 3
    
    score_str = str(score)
    scoretext.text = score_str
    
    camera_direction = camera.forward
    hit_info = raycast(camera.world_position, camera_direction, distance=desired_distance, ignore=[camera, redgun])
    if hit_info.hit:
        redgun.world_position = hit_info.world_point - camera_direction*0.1
    else:
        redgun.world_position = camera.world_position + camera_direction*desired_distance
        
   
    for npc in npcs:
        
        direction = player.position - npc.position
        direction.y = 0  
        rotation_speed = 1
        
        
        distance_to_player = distance(npc.position, player.position)
        target_angle = math.degrees(math.atan2(direction.x, direction.z)) - 180
        
        if ai_enabled:     
            if distance_to_player > 1.5:
                direction = (player.position - npc.position).normalized()
                npc.position += direction * npc_speed * time.dt
    
            if direction.length() > 0.001:
                 npc.rotation_y = lerp_angle(
                     npc.rotation_y,
                     target_angle,
                     2 * time.dt
                    )
                 npc.face.rotation_y = lerp_angle(
                     npc.face.rotation_y,
                     0,
                     8 * time.dt
                    )
         
         
    
    bullet_speed = 100
    for bullet in bullets[:]:
        bullet.position += bullet.direction * bullet_speed * time.dt
    
        hit_info = raycast(bullet.position - bullet.direction * bullet_speed * time.dt,
                           bullet.direction,
                           distance=bullet_speed * time.dt,
                           ignore=[bullet])
        
        if hit_info.hit:
            hit_entity = hit_info.entity

            hit_npc = None
            for npc in npcs:
                if hit_entity == npc.face or hit_entity == npc.body:
                    hit_npc = npc
                    
                
            if hit_npc:
                destroy(hit_npc)
                npcs.remove(hit_npc)                  
                hit_npc = npc
                bullet.disable()
                bullets.remove(bullet)
                destroy(bullet)
                score += 1
        
                
                
            else:
                decal = Entity(
                    model='plane',
                    texture='textures/splat.png',
                    color=color.red,
                    double_sided=True,
                    scale=(3,3,3),
                    position=hit_info.world_point + hit_info.normal * 0.01
                    )
                decal.look_at(decal.position + hit_info.normal, 'up') 
                splats.append(decal)
                bullet.disable()
                bullets.remove(bullet)
                destroy(bullet)
        

    if len(splats) > 10:
        old_decal = splats.pop(0)
        destroy(old_decal)
        
            
            
        
    is_moving = held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']
    if is_moving and held_keys['shift'] and player.grounded:
        walk_bob_timer += time.dt * walk_bob_speed * 1.5
        player.camera_pivot.y = default_cam_y + math.sin(walk_bob_timer) * walk_bob_amount
        player.speed = 15
    elif is_moving and not held_keys['shift'] and player.grounded:
        walk_bob_timer += (time.dt * walk_bob_speed) 
        player.speed = 7
        player.camera_pivot.y = default_cam_y + math.sin(walk_bob_timer) * walk_bob_amount
    else:
        
        player.camera_pivot.y = lerp(player.camera_pivot.y, default_cam_y, 4 * time.dt)
        
    
    
        
        
def input(key):
    if key == 'left mouse down':
        create_bullet()
        
app.run()
