# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100
number_of_guess = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print "New Game Starts!"    
    print ""
    global secret_number
    global number_of_guess
    
    number_of_guess = 7
    secret_number = random.randrange(0,100)    
    if num_range == 1000:
        range1000()
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global number_of_guess
    global num_range
    num_range = 100
    #number_of_guess = 7
    new_game()
    secret_number = random.randrange(0,100)
  
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    global secret_number
    global number_of_guess
    
    num_range = 1000
    number_of_guess = 10
    print "New Game starts with range [0, 1000) !"
    print ""    
    #new_game()
    secret_number = random.randrange(0,1000)
    
def input_guess(guess):
    # main game logic goes here	
    global player_number 
    global number_of_guess
    player_number = int(guess)
    print "Guess was", player_number
    
    
    if player_number > secret_number:
       print "Lower"
    elif player_number < secret_number:
       print "Higher"
    elif player_number == secret_number:
       print "Correct"
       return new_game()
    else:
       print "Please try with numbers"       
    
    
    
    number_of_guess = number_of_guess - 1
    print "Number of remaining guesses", number_of_guess
    print ""
    if number_of_guess == 0 and number_of_guess != secret_number:
      print "Sorry, You ran out of guesses ! It's", secret_number
      new_game()
    #elif number_of_guess < 0:
      #new_game()
    
        
# create frame

frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range 100", range100, 100)
frame.add_button("Range 1000", range1000, 100)
frame.add_input("Input Guess", input_guess, 100)
frame.start()

# call new_game 
new_game()


