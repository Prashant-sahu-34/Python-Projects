import pygame
import os
from pygame import mixer
mixer.init()
a=b=mixer.music
a.load("music01.wav")
b.load("music02.mp3")

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame")
whitecolor=(255,255,255)
FPS=60
center_border=pygame.Rect(400,0,10,800)

pygame.font.init()
note=pygame.font.SysFont("Lucida Handwriting",25)
health_font=pygame.font.SysFont("Lucida Handwriting",25)
winner_font_text=pygame.font.SysFont("Lucida Handwriting",50)

space_ship_01=pygame.image.load(os.path.join("image1.png"))
sship01_size=pygame.transform.rotate(pygame.transform.scale(space_ship_01,(80,80)),270)

space_ship_02=pygame.image.load(os.path.join("image2.png"))
sship02_size=pygame.transform.rotate(pygame.transform.scale(space_ship_02,(80,80)),90)

background=pygame.transform.scale(pygame.image.load(os.path.join("image3.jpg")),(800,600))

winner_screen=pygame.transform.scale(pygame.image.load(os.path.join("image4.png")),(800,600))

ship_01_hit=pygame.USEREVENT+1
ship_02_hit=pygame.USEREVENT+2

'''for j in range(4):
    for i in range(214):
        if i<10:
            game_loading=pygame.transform.scale(pygame.image.load(
                os.path.join("image5","frame_00"+str(i)+"_delay-0.02s.gif")),(600,600))
        elif i>=10 and i<100:
            game_loading=pygame.transform.scale(pygame.image.load(
                os.path.join("image5","frame_0"+str(i)+"_delay-0.02s.gif")),(600,600))
        else:
            game_loading=pygame.transform.scale(pygame.image.load(
                os.path.join("image5","frame_"+str(i)+"_delay-0.02s.gif")),(600,600))
        screen.blit(game_loading,(0,0))
        pygame.display.update()
        pygame.time.delay(1000*(1//2))'''

for i in range(10):
    game_loading=pygame.transform.scale(pygame.image.load(
                os.path.join("image6","frame_"+str(i)+"_delay-0.5s.gif")),(800,600))    
    screen.blit(game_loading,(0,0))
    
    '''note_points=note.render("NOTE POINTS:- A)For Left Space-Ship following key must be used-->\
                        1.Move Left='S' key\
                        2.Move Right='D' key\
                        3.Move Up='E' key\
                        4.Move Down='X' key\
                        5.TO fire bullet='Left control' key\
                  B)For Right Space-Ship following key must be used-->\
                        1.Move Left=Left arrow key\
                        2.Move Right=Right key\
                        3.Move Up=Up key\
                        4.Move Down=Down key\
                        5.TO fire bullet='Right control' key",1,(189, 181, 213))                        
    screen.blit(note_points,(100,500))'''
                            
    pygame.display.update()
    pygame.time.delay(1000)
b.set_volume(0.2)
b.play()
        
def draw_window(ship_01,ship_02,ship_01_bullets,ship_02_bullets,ship_01_health,ship_02_health):
    #screen.fill(whitecolor)     #colered are filled in rgb(red,greeen,blue) format
    screen.blit(background,(0,0))
    #pygame.draw.rect(screen,(0,0,0),center_border)
    ship_01_healthtext=health_font.render("Ship-01 Health:"+str(ship_01_health),1,(189, 181, 213))
    ship_02_healthtext=health_font.render("Ship-02 Health:"+str(ship_02_health),1,(189, 181, 213))
    screen.blit(ship_01_healthtext,(50,50))
    screen.blit(ship_02_healthtext,(500,50))
    
    for bullet in ship_01_bullets:
        pygame.draw.rect(screen,(255,0,0),bullet)
    for bullet in ship_02_bullets:
        pygame.draw.rect(screen,(255,0,0),bullet)
    screen.blit(sship01_size,(ship_01.x,ship_01.y))
    screen.blit(sship02_size,(ship_02.x,ship_02.y))
    pygame.display.update()

def Winner(winner):
    screen.blit(background,(0,0))
    b.stop()
    winner_text=winner_font_text.render(winner,1,(189, 181, 213))
    screen.blit(winner_text,(130,250))
    pygame.display.update()
    pygame.time.delay(3000)
    screen.blit(winner_screen,(0,0))
    pygame.display.update()
    pygame.time.delay(3000)
    
def key_ship_01(key_pressed,ship_01):
    if(key_pressed[pygame.K_s] and ship_01.x>0):            #left key=s
        ship_01.x-=5
    elif(key_pressed[pygame.K_d] and ship_01.x<320):        #right key=d
        ship_01.x+=5
    elif(key_pressed[pygame.K_e] and ship_01.y>100):        #up key=e
        ship_01.y-=5
    elif(key_pressed[pygame.K_x] and ship_01.y<520):        #down key=x
        ship_01.y+=5
    
def key_ship_02(key_pressed,ship_02):
    if(key_pressed[pygame.K_LEFT] and ship_02.x>390):       #left key=left arrow
        ship_02.x-=5
    elif(key_pressed[pygame.K_RIGHT] and ship_02.x<720):    #right key=right arrow
        ship_02.x+=5
    elif(key_pressed[pygame.K_UP] and ship_02.y>100):       #up key=up arrow
        ship_02.y-=5
    elif(key_pressed[pygame.K_DOWN] and ship_02.y<520):     #down key=down arrow
        ship_02.y+=5

def bullet_collide(ship_01,ship_02,ship_01_bullets,ship_02_bullets):
    for bullet in ship_01_bullets:
        bullet.x+=5
        if ship_02.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ship_02_hit))
            ship_01_bullets.remove(bullet)
        elif bullet.x>1550:
            ship_01_bullets.remove(bullet)

    for bullet in ship_02_bullets:
        bullet.x-=5
        if ship_01.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ship_01_hit))
            ship_02_bullets.remove(bullet)
        elif bullet.x<0: 
            ship_02_bullets.remove(bullet)

done=False
def main():
    ship_01=pygame.Rect(50,300,50,50)
    ship_02=pygame.Rect(670,300,50,50)
    ship_01_bullets=[]
    ship_02_bullets=[]
    ship_01_health=10
    ship_02_health=10
    
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                run=False
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_LCTRL):
                    bullet=pygame.Rect(ship_01.x+ship_01.width+10,ship_01.y+ship_02.height/2+10,20,5)
                    ship_01_bullets.append(bullet)
                if(event.key==pygame.K_RCTRL):
                    bullet=pygame.Rect(ship_02.x+ship_02.width+10,ship_02.y+ship_02.height/2+10,20,5)
                    ship_02_bullets.append(bullet)
            if(event.type==ship_01_hit):
                ship_01_health-=1
                a.set_volume(100)
                a.play()
            if(event.type==ship_02_hit):
                ship_02_health-=1                
                a.set_volume(100)
                a.play()
                
        winner=""
        if ship_01_health<0:
            winner="SPACE-SHIP-02 WINS"
        if ship_02_health<0:
            winner="SPACE-SHIP-01 WINS"
        if winner!="":
            Winner(winner)
            break
        
        key_pressed=pygame.key.get_pressed()       
        key_ship_01(key_pressed,ship_01)
        key_ship_02(key_pressed,ship_02)

        bullet_collide(ship_01,ship_02,ship_01_bullets,ship_02_bullets)
           
        draw_window(ship_01,ship_02,ship_01_bullets,ship_02_bullets,ship_01_health,ship_02_health)
        
    pygame.quit()
    
main()
