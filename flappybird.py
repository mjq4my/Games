#Michael Quinn mjq4my
import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)
character = gamebox.from_color(200, 250, "yellow", 27, 27)     #(xcoord, ycoord, color, width, height)
ground = gamebox.from_color(-100, 600, "brown", 3000, 100)  #cretes ground
game_over = gamebox.from_text(camera.x, camera.y, "You Lost", "Impact", 120, "purple")

bottom_pillars = []
top_pillars = []
for x in range(600,1401,400):       #Making initial pillars
    y=random.randrange(100,700)
    bottom_pillars.append(gamebox.from_color(x,550,'dark green',130,y))
    top_pillars.append(gamebox.from_color(x,0,'dark green',130,875-y))


def end_game(keys):
    camera.clear('white')
    camera.draw(game_over)
    time_lasted = gamebox.from_text(camera.x, camera.bottom-30,
                                    "You traveled "+str(int(9.36*frame/ticks_per_second))+" feet",  #random constant multiplied by time
                                    "Arial", 60, 'purple')
    time_lasted.bottom = camera.bottom
    camera.draw(time_lasted)
    camera.display()
frame = 0
def tick(keys):
    global frame
    for pillar in bottom_pillars:
        if character.bottom_touches(ground) or character.touches(pillar):
            character.yspeed=0
            return end_game(keys)
    for pillar in top_pillars:
        if character.bottom_touches(ground) or character.touches(pillar):
            character.yspeed=0
            return end_game(keys)
    frame+=1
    if pygame.K_SPACE in keys:
        character.speedy =-8
        keys.clear()

    character.yspeed+=0.8
    character.move_speed()
    camera.clear("sky blue")           #background color
    camera.draw(character)
    camera.draw(ground)
    if character.y<=20:         #Can't go above top
        character.y=20

    z= random.randrange(100,700)        #var to make random height of pillar

    for pillar in bottom_pillars:
        camera.draw(pillar)
        pillar.x-=7
        if pillar.left < camera.left-130:
            pillar.x=1130
            pillar.size=130,z
    for pillar in top_pillars:
        camera.draw(pillar)
        pillar.x-=7
        if pillar.left<camera.left-130:
            pillar.x=1130
            pillar.size=130,875-z

    camera.display()
ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)