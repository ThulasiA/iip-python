# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

#T
import random

# helper functions
def name_to_number(name):
    
    # T's code
    
    if (name == 'rock'):
      return 0
    elif (name == 'Spock'):
      return 1
    elif (name == 'paper'):
      return 2
    elif (name == 'lizard'):
      return 3
    elif (name == 'scissors'):
      return 4
    else:
      print 'Name not in the game'  
    #T's code ends

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    
    #T's code
    if (number == 0):
      return "rock"
    elif (number == 1):
      return "Spock"
    elif (number == 2):
      return "paper"
    elif (number == 3):
      return "lizard"
    elif (number == 4):
      return "scissors"
    else:
      print 'Number not in the game' 
    #T's code ends
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    # T
    print ""

    # print out the message for the player's choice
    # T
    print "Player chooses" + " " + player_choice
    #print name_to_number('rock')
   
    # convert the player's choice to player_number using the function name_to_number()
    #T
    player_number = name_to_number(player_choice)
    #print "Player chooses" + " " + player_choice

    # compute random guess for comp_number using random.randrange()
    #T
    comp_number = random.randrange(0,5)
    
    
    # convert comp_number to comp_choice using the function number_to_name()
    #T
    comp_choice = number_to_name (comp_number)
    
    # print out the message for computer's choice
    #T
    print "Computer chooses" + " " + comp_choice

    # compute difference of comp_number and player_number modulo five
    #T
    diff = (player_number - comp_number) % 5
    #print player_number
    #print comp_number
    #print diff

    # use if/elif/else to determine winner, print winner message
    #T
    if diff == 1:
      print "Player wins !"
    elif diff == 2:
      print "Player wins !"
    elif diff == 3:
      print "Computer wins !"
    elif diff == 4:
      print "Computer wins !"
    elif diff == 0:
      print "Player and Computer Tie !"
    else:
      print "Option not in the game"
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




