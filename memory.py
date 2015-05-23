# implementation of card game - Memory

import simplegui
import random

cards1 = [0,1,2,3,4,5,6,7]
cards2 = [0,1,2,3,4,5,6,7]
cards = cards1 + cards2

exposed = [False]*16
state = 0
first_card = 0
second_card = 0
turn = 0

# helper function to initialize globals
def new_game():
    
    global exposed
    global turn
    global state
    state = 0
    turn = 0
    exposed = [False]*16
    random.shuffle(cards)    
    
# define event handlers
def mouseclick(pos):
    # game state logic here
    
    i = pos[0]//50
    global state 
    global first_card 
    global second_card
    global turn
    
   
    if exposed[i] == False:
       exposed[i] = True
    
       if state == 0: 
          state = 1
          exposed[i] = True
          first_card = i           
        
       elif state == 1:
          state = 2
          exposed[i] = True
          second_card = i
          turn += 1
            
       else:
          state = 1
          if cards[first_card] != cards[second_card]:
            exposed[first_card] = exposed[second_card] = False            
          first_card = i
          
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    pos = [0, 100]    
    
    for i in range(len(cards)):       
        if exposed[i] == True:
                 canvas.draw_text(str(cards[i]), [i*50,70], 50, "White")                 
                 pos[0] = i * 50
                 pos[1] = pos[1]
                 
        else:
           Rectangle_x = i * 50
           Rectangle_y =  Rectangle_x + 50
           canvas.draw_polygon([( Rectangle_x, 0), (Rectangle_y, 0), (Rectangle_y, 100), ( Rectangle_x,100)], 4, 'Black', 'Green')
          
    label.set_text("Turns=" + str(turn))       
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()