# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1,1]

paddle1_pos = 200
paddle2_pos = 200
paddle1_vel = 1
paddle2_vel = 1

    

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel# these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [1,1]
       
    if (direction == RIGHT):        
        right_right = random.randrange(120/60, 240/60)
        right_up = random.randrange(60/60, 180/60)
        ball_vel = [right_right, -right_up]
        
    elif (direction == LEFT):        
        left_left = random.randrange(120/60, 240/60)
        left_up = random.randrange(60/60 , 180/60)
        ball_vel = [-left_left, -left_up]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints  
    score1 = 0
    score2 = 0
    paddle1_pos = 200
    paddle2_pos = 200
    
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball(RIGHT)
   
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if (paddle1_pos >= HEIGHT - 40):
       paddle1_vel = 0
    if (paddle1_pos <= 40):
        paddle1_vel = 0
    if (paddle2_pos >= HEIGHT - 40):
       paddle2_vel = 0
    if (paddle2_pos <= 40):
        paddle2_vel = 0
   
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
      
       if (paddle1_pos + HALF_PAD_HEIGHT) >= ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT):
            ball_vel[0] *= -1.1
            ball_vel[1] *= -1.1            
       else:              
            spawn_ball(RIGHT) 
            score2 += 1
         
    if ball_pos[0] >= (WIDTH-PAD_WIDTH) - BALL_RADIUS:
       
       if (paddle2_pos + HALF_PAD_HEIGHT) >= ball_pos[1] >= (paddle2_pos - HALF_PAD_HEIGHT):
            ball_vel[0] *= -1.1
            ball_vel[1] *= -1.1
       else:            
            spawn_ball(LEFT)
            score1 += 1
       
    if ball_pos[1] <= (BALL_RADIUS):
       ball_vel[1] = -ball_vel[1]
  
    if ball_pos[1] >= (HEIGHT-1) - BALL_RADIUS:
       ball_vel[1] = -ball_vel[1]    
    
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    
        
    
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS , 0.5 ,"White","White")
    
   
    
    # draw paddles   
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos+HALF_PAD_HEIGHT], 8,"White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH, paddle2_pos+HALF_PAD_HEIGHT], 8,"White")
    
    # draw scores
    canvas.draw_text( str(score1), [150,75], 50, "White")
    canvas.draw_text( str(score2), [450,75], 50, "White")
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
   
    vel = 2
    
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += vel 
        if (paddle1_pos >= HEIGHT - 40):
            paddle1_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += vel
        if (paddle2_pos >= HEIGHT - 40):
            paddle2_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= vel
        if (paddle1_pos <= 40):
            paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= vel
        if (paddle2_pos <= 40):
            paddle2_vel = 0 
    
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    
    vel = 2
    
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0   
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    
def restart():
    global score1, score2
    score1 = 0
    score2 = 0
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",restart,100)


# start frame
new_game()
frame.start()
