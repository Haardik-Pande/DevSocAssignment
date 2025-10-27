import pygame, sys, random
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x+=ball_speed_x
    ball.y+=ball_speed_y

    if ball.top <=0 or ball.bottom>=screen_height:
        ball_speed_y*=-1
    if ball.left <=0 or ball.right>=screen_width:
        update_score()
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x*=-1
def player_animation():
    player.y+=player_speed
    if player.top<=0:
        player.top=0
    if player.bottom>=screen_height:
        player.bottom=screen_height
def opponent_animation():
    opponent.y+=opponent_speed
    if opponent.top<=0:
        opponent.top=0
    if opponent.bottom>=screen_height:
        opponent.bottom=screen_height
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center=(screen_width/2,screen_height/2)
    ball_speed_y*=random.choice((1,-1))
    ball_speed_x*=random.choice((1,-1))
def update_score():
    global player_score, opponent_score
    if ball.left<=0:
        player_score+=1
    if ball.right>=screen_width:
        opponent_score+=1

#General setup        
pygame.init()
clock=pygame.time.Clock()
screen_width=1280
screen_height=800
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')


ball=pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player=pygame.Rect(screen_width-20,screen_height/2-70,10,140)
opponent=pygame.Rect(10,screen_height/2-70,10,140)


bg_color=pygame.Color('black')
light_grey=(200,200,200)
blue=(0,0,255)
red=(255,0,0)
ball_speed_x=7*random.choice((1,-1))
ball_speed_y=7*random.choice((1,-1))
player_speed=0
opponent_speed=0
player_score=0
opponent_score=0
game_font=pygame.font.Font(None,74)

game_state="PLAY"
winner=""

while True:
    #Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if game_state=="PLAY":
                if event.key==pygame.K_DOWN:
                    player_speed+=7
                if event.key==pygame.K_UP:
                    player_speed-=7  
                if event.key==pygame.K_s:
                    opponent_speed+=7
                if event.key==pygame.K_w:
                    opponent_speed-=7 
            elif game_state=="PAUSE":
                if event.key==pygame.K_SPACE:
                    # reset game
                    player_score=0
                    opponent_score=0
                    ball_restart()
                    game_state="PLAY"
        if event.type==pygame.KEYUP and game_state=="PLAY":
            if event.key==pygame.K_DOWN:
                player_speed-=7
            if event.key==pygame.K_UP:
                player_speed+=7
            if event.key==pygame.K_s:
                opponent_speed-=7
            if event.key==pygame.K_w:
                opponent_speed+=7

    if game_state=="PLAY":            
        ball_animation()
        player_animation()
        opponent_animation()

        if player_score>=3:
            game_state="PAUSE"
            winner="BLUE" 
        if opponent_score>=3:
            game_state="PAUSE"
            winner="RED"

    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, blue, player)
    pygame.draw.rect(screen, red, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0),(screen_width/2,screen_height))
    pygame.draw.circle(screen, 'white', (screen_width/2,screen_height/2), 100, 1)

    #Display scores
    player_text=game_font.render(f"{player_score}",True,light_grey)
    opponent_text=game_font.render(f"{opponent_score}",True,light_grey)
    screen.blit(player_text,(screen_width/2+40,20))
    screen.blit(opponent_text,(screen_width/2-80,20))

    #Game Over Screen
    if game_state=="PAUSE":
        screen.fill(bg_color)
        over_font=pygame.font.Font(None,100)
        text=over_font.render(f"GAME OVER - {winner} WINS!",True,light_grey)
        restart_font=pygame.font.Font(None,50)
        restart_text=restart_font.render("Press SPACE to restart",True,light_grey)
        screen.blit(text,(screen_width/2-text.get_width()/2,screen_height/2-60))
        screen.blit(restart_text,(screen_width/2-restart_text.get_width()/2,screen_height/2+40))

    #Updating the window
    pygame.display.flip()
    clock.tick(60)
