#Michael Quinn mjq4my & Daniel Forsman dhf5qe
#Zombies
import pygame
import gamebox
import random
import os

camera = gamebox.Camera(1200,700)

# shooter = gamebox.from_image(135,350,"http://images.clipartpanda.com/shooter-clipart-shooter-clipart-1.jpg")
# backgr = gamebox.from_image(600,350,"http://orig12.deviantart.net/eced/f/2014/312/f/c/abandoned_factory_by_stgspi-d85o7fq.png")
# start_pic = gamebox.from_image(600,350,"http://img08.deviantart.net/e319/i/2013/334/8/8/the_pale_forest_by_nelleke-d6w6lnu.png")
shooter = gamebox.from_image(135,350,"http://images.clipartpanda.com/shooter-clipart-shooter-clipart-1.jpg")
backgr = gamebox.from_image(600,350,"http://orig12.deviantart.net/eced/f/2014/312/f/c/abandoned_factory_by_stgspi-d85o7fq.png")
start_pic = gamebox.from_image(600,350,"http://img08.deviantart.net/e319/i/2013/334/8/8/the_pale_forest_by_nelleke-d6w6lnu.png")

intro = gamebox.from_text(camera.x, 100, "Welcome to Zombies", "Impact", 60, "white")
instructions = gamebox.from_text(camera.x, 600, "Instructions: Press up and down to move, space to shoot. Defeat all three waves of zombies.", "Impact", 30, "white")
# names = gamebox.from_text(camera.x, 170, "Michael Quinn (mjq4my) & Daniel Forsman (dhf5qe)", "Impact", 30, "white")
starting = gamebox.from_text(camera.x, 650, "Press s to start", "Impact", 40, "white")
wave1 = gamebox.from_text(camera.x, 50, "WAVE 1", "Impact", 30, "red")
wave2 = gamebox.from_text(camera.x, 50, "WAVE 2", "Impact", 30, "red")
finalwave = gamebox.from_text(camera.x, 50, "FINAL WAVE", "Impact", 30, "red")

start_pic.size = 1200,700
lose_pic = gamebox.from_image(600,350,"http://1.bp.blogspot.com/--ZtvnMlMDcs/Usr205F1wiI/AAAAAAAAPYU/B2JGrSPBOgg/w1200-h630-p-k-no-nu/walkers-photo-walking-dead.png")
lose_pic.size = 1200,700
# win_pic = gamebox.from_image(600,350,"http://primalsurvivor.com/wp-content/uploads/2014/10/apocalypsesurvivor1.png")
win_pic = gamebox.from_image(600,350,"http://1.bp.blogspot.com/--ZtvnMlMDcs/Usr205F1wiI/AAAAAAAAPYU/B2JGrSPBOgg/w1200-h630-p-k-no-nu/walkers-photo-walking-dead.png")
win_pic.size = 1200,700
game_over = gamebox.from_text(camera.x, 100, "The zombies ate you, sorry.", "Impact", 70, "red")
game_winner = gamebox.from_text(camera.x, 500, "You won! You slayed all the zombies!", "Impact", 70, "white")
backgr.size = 1200,700
shooter.size = 100,150
first_zombies =[]
second_zombies = []
last_zombies = []
bullets = []

gunshot = gamebox.load_sound("sounds/gunshot01.wav")
# reload = gamebox.load_sound("sounds/gun_cocking.wav")
zombiedie = gamebox.load_sound("sounds/zombie_attack.wav")

ammo = 100
zombie_speed = 4
shooter_speed=10
frame = 0
frames = str(frame)
game_on = False
lose_game=False

for z in range(15):
    x = random.randrange(1250, 1850)
    y = random.randrange(50,650)
    first_zombies.append(gamebox.from_image(x,y,"pics/zombie.png"))
for z in range(20):
    x = random.randrange(1300, 1900)
    y = random.randrange(50,650)
    second_zombies.append(gamebox.from_image(x,y,"pics/zombie.png"))
for z in range(25):
    x = random.randrange(1300, 1900)
    y = random.randrange(50,650)
    last_zombies.append(gamebox.from_image(x,y,"pics/zombie.png"))

def reload():
    one = gamebox.load_sound("sounds/outofammo.wav")
    one.play()
    two = gamebox.load_sound("sounds/weapload.wav")
    two.play()
    return

def losegame(keys):
    camera.clear("white")
    camera.draw(lose_pic)
    camera.draw(game_over)
    reload()
    gunshot.stop()
    camera.display()

def win_game(keys):
    camera.draw(win_pic)
    camera.draw(game_winner)
    reload()
    gunshot.stop()
    camera.display()

def tick(keys):
    global frame
    global game_on, lose_game
    global ammo
    frames = str(int(frame/22))                         # approximate time in seconds
    timer = gamebox.from_text(900, 50, "Timer: " + frames, 'impact', 30, 'red')
    if game_on == False:
        camera.clear("white")
        camera.draw(start_pic)
        camera.draw(intro)
        camera.draw(instructions)
        camera.draw(starting)
        # camera.draw(names)
        camera.display()
        if pygame.K_s in keys:
            game_on = True
    if game_on == True:                                 # start game
        frame+=1
        camera.clear("grey")
        camera.draw(backgr)
        ammo_str = gamebox.from_text(80, 50, "Ammo: " + str(ammo), "Impact", 34, "white")
        camera.draw(ammo_str)
        camera.draw(shooter)
        camera.draw(timer)
        if shooter.y <= 100:                            # shooter boundaries
            shooter.y = 100
        if shooter.y >=650:
            shooter.y = 650
        if len(first_zombies)!=0:                       # Setting up wave number
            camera.draw(wave1)
        elif len(first_zombies)==0 and len(second_zombies)!=0:
            camera.draw(wave2)
        else:
            camera.draw(finalwave)
        for zombie in first_zombies:                    # if bullet touches zombie, kill zombie
            for bullet in bullets:
                if bullet.touches(zombie) and zombie.x<=1230:
                    first_zombies.remove(zombie)
                    zombiedie.play()
                    bullets.remove(bullet)
        for zombie in second_zombies:
            for bullet in bullets:
                if bullet.touches(zombie) and zombie.x<=1230:
                    second_zombies.remove(zombie)
                    zombiedie.play()
                    bullets.remove(bullet)
        for zombie in last_zombies:
            for bullet in bullets:
                if bullet.touches(zombie) and zombie.x<=1230:
                    last_zombies.remove(zombie)
                    zombiedie.play()
                    bullets.remove(bullet)
        for zombie in first_zombies:
            zombie.size = 80, 130
            camera.draw(zombie)
            zombie.x-=zombie_speed
            if frame%10 == 1:                           # animation
                zombie.image = os.getcwd()+"/pics/zombies/walk/go_1.png"
            elif frame%10 == 2:
                zombie.image = os.getcwd()+"/pics/zombies/walk/go_2.png"
            elif frame%10 == 3:
                zombie.image = os.getcwd()+"/pics/zombies/walk/go_3.png"
            elif frame%10 == 4:
                zombie.image = os.getcwd()+"/pics/zombies/walk/go_4.png"
            elif frame % 10 == 5:
                zombie.image = os.getcwd()+"/pics/zombies/walk/go_5.png"
            elif frame%10 == 6:
                zombie.image = os.getcwd()+"/pics/zombies/walk/go_6.png"
            elif frame%10 == 7:
                zombie.image = os.getcwd()+"/pics/zombies/walk/go_7.png"
            elif frame%10 == 8:
                zombie.image = os.getcwd()+"/pics/zombies/walk/go_8.png"
            elif frame%10 == 9:
                zombie.image = os.getcwd()+"/pics/zombies/walk/go_9.png"
        if pygame.K_UP in keys:
            shooter.y -= shooter_speed
        if pygame.K_DOWN in keys:
            shooter.y += shooter_speed
        if pygame.K_SPACE in keys:
            bullet = gamebox.from_color(150, shooter.y - 55, "orange", 10, 2)
            gunshot.play()
            bullets.append(bullet)
            ammo-=1
            if ammo%10==0 and ammo>0:
                for a in range(1):             # make reload sound after every 10 shots
                    reload()
                    keys.clear()
                    break
            keys.clear()
        if ammo<=0:                             # no more ammo
            bullets. clear()
            reload()
            gunshot.stop()
            ammo =0
        for bullet in bullets:                  # shoot the bullets
            bullet.x+=80
            camera.draw(bullet)
        for zombie in first_zombies:
            if zombie.x<=shooter.x:
                lose_game= True
        for zombie in second_zombies:
            if zombie.x <= shooter.x:
                lose_game=True
        for zombie in last_zombies:
            if zombie.x<=shooter.x:
                lose_game=True
        if len(first_zombies)==0:
            for zombie in second_zombies:
                zombie.size = 80, 130
                camera.draw(zombie)
                zombie.x -= zombie_speed +1
                if frame % 10 == 1:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_1.png"
                elif frame % 10 == 2:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_2.png"
                elif frame % 10 == 3:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_3.png"
                elif frame % 10 == 4:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_4.png"
                elif frame % 10 == 5:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_5.png"
                elif frame % 10 == 6:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_6.png"
                elif frame % 10 == 7:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_7.png"
                elif frame % 10 == 8:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_8.png"
                elif frame % 10 == 9:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_9.png"
        if len(second_zombies)==0:
            for zombie in last_zombies:
                zombie.size = 80, 130
                camera.draw(zombie)
                zombie.x -= zombie_speed +2
                if frame % 10 == 1:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_1.png"
                elif frame % 10 == 2:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_2.png"
                elif frame % 10 == 3:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_3.png"
                elif frame % 10 == 4:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_4.png"
                elif frame % 10 == 5:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_5.png"
                elif frame % 10 == 6:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_6.png"
                elif frame % 10 == 7:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_7.png"
                elif frame % 10 == 8:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_8.png"
                elif frame % 10 == 9:
                    zombie.image = os.getcwd()+"/pics/zombies/walk/go_9.png"
        if lose_game==True:
            losegame(keys)
            first_zombies.clear()
            second_zombies.clear()
            last_zombies.clear()
        elif len(first_zombies)==0 and len(second_zombies)==0 and len(last_zombies)==0:
            win_game(keys)
        camera.display()
ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)