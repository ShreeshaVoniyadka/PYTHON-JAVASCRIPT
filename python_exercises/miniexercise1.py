import pygame
import os
pygame.mixer.init()
pygame.font.init()
W,H=800,500
white=(255,225,255)
black=(0,0,0)
RED=(225,0,0)
YELLOW=(255,255,0)
FPS=60
VEL=5
sw=40
sh=40
maxi=20
WIN=pygame.display.set_mode((W,H))
WINNER_FONT=pygame.font.SysFont('comicsan',100)
BULLET_VEL=7
BORDER=pygame.Rect((W//2)-4,0,4,H)
pygame.display.set_caption("GAME1")

HEALTH_FONT=pygame.font.SysFont('comicsan',40)
BULLETS_FIRE=pygame.mixer.Sound(os.path.join(
    os.getcwd(),"EXERCISES","PygameForBeginners-main","Assets","Grenade+1.mp3"))
BULLET_HITS=pygame.mixer.Sound(os.path.join(
    os.getcwd(),"EXERCISES","PygameForBeginners-main","Assets","Gun+Silencer.mp3"))
yellow_hit=pygame.USEREVENT+1
red_hit=pygame.USEREVENT+2

YELLOW_SPACESHIP_IMAGE=pygame.image.load(
    os.path.join(os.getcwd(),"EXERCISES", "PygameForBeginners-main",'Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(sw,sh)),90  )
RED_SPACESHIP_IMAGE=pygame.image.load(
    os.path.join(os.getcwd(),"EXERCISES", "PygameForBeginners-main",'Assets','spaceship_yellow.png'))
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(sw,sh)),270)
SPACE=pygame.transform.scale(pygame.image.load(
    os.path.join(os.getcwd(),"EXERCISES","PygameForBeginners-main",'Assets',"space.png")),(W,H))


def draw(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,black,BORDER)
    red_health_text=HEALTH_FONT.render("Health:"+str(red_health),1,white)
    yellow_health_text=HEALTH_FONT.render("Health:"+str(yellow_health),1,white)
    WIN.blit(red_health_text,(W-red_health_text.get_width()-10,10))
    WIN.blit(yellow_health_text,(10,10))


    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    for bullet in  yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)
    pygame.display.update()


def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x+=BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x>W:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x-=BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)
        elif bullet.x<0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text=WINNER_FONT.render(text,1,white)
    WIN.blit(draw_text,(W/2-draw_text.get_width()/2,H/2-draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def yellow_handlemovement(key_pressed,yellow):
    
        if key_pressed[pygame.K_a] and yellow.x-VEL>0:#left
            yellow.x-=VEL
        if key_pressed[pygame.K_d] and yellow.x+VEL+yellow.width<BORDER.x:#right
            yellow.x+=VEL
        if key_pressed[pygame.K_w] and yellow.y-VEL>0:#up
            yellow.y-=VEL
        if key_pressed[pygame.K_s]and yellow.y+VEL+yellow.height<H:#down
            yellow.y+=VEL


def red_handlemovement(key_pressed,red):
    if key_pressed[pygame.K_UP] and red.y-VEL>0:#up
        red.y-=VEL
    if key_pressed[pygame.K_DOWN] and red.y+VEL<H-45:#down
        red.y+=VEL
    if key_pressed[pygame.K_LEFT]and red.x-VEL-red.width>BORDER.x-40:#left
        red.x-=VEL
    if key_pressed[pygame.K_RIGHT]and red.x+VEL+red.width<W:#right
        red.x+=VEL


def main():
    red=pygame.Rect(700,300,sw,sh)
    yellow=pygame.Rect(100,300,sw,sh)
    red_bullets=[]
    yellow_bullets=[]
    red_health=10
    yellow_health=10

    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
            if  event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL and len(yellow_bullets)<maxi:
                    bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                    yellow_bullets.append(bullet)
                    BULLETS_FIRE.play()

                if event.key==pygame.K_RCTRL and len(red_bullets)<maxi:
                    bullet=pygame.Rect(red.x,red.y+red.height//2-2,10,5)
                    red_bullets.append(bullet)
                    BULLETS_FIRE.play()
            if event.type==red_hit:
                red_health-=1    
            if event.type==yellow_hit:
                yellow_health-=1
        winner_text=""        
        if red_health<=0:
            winner_text="yellow wins"
        if yellow_health<=0:
            winner_text="red wins"
        if winner_text!="":
            draw_winner(winner_text)
            break



        
        key_pressed=pygame.key.get_pressed()
        yellow_handlemovement(key_pressed,yellow)
        red_handlemovement(key_pressed,red)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        draw(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)
    main()
    

if __name__=="__main__":
    main()