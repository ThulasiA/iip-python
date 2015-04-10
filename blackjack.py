# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
message = ""
score = 0

player_hand = []
dealer_hand = []
deck_shuffle = []
hand_value = 0 

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    
    # create Hand object
    def __init__(self):
       self.hand_list = []	
        
    # return a string representation of a hand
    def __str__(self):
        result = "Hand Contains "
        for i in range(len(self.hand_list)):
            result += str(self.hand_list[i]) + " "
        return result	

    # add a card object to a hand
    def add_card(self, card):
        self.hand_list.append(card)	
        
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        
        for i in self.hand_list:     
            hand_value += VALUES[Card.get_rank(i)]
        for i in self.hand_list:
            if Card.get_rank(i) != 'A': 
                hand_value = hand_value
            elif Card.get_rank(i) == 'A' and hand_value <= 11:             
                hand_value = hand_value+10           
              
        return hand_value
           
    # draw a hand on the canvas, use the draw method for cards
    def draw(self, canvas, pos):
        x = 30
        for card in self.hand_list:
            card.draw(canvas, (x, pos[1]))
            x += 80
       
            
# define deck class 
class Deck:
    def __init__(self):
        self.deck_list =[]# create a Deck object
        for i in SUITS:
            for j in RANKS:
                self.deck_list.append(Card(i,j))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck_list)    

    def deal_card(self):
        return self.deck_list.pop()	# deal a card object from the deck
    
    # return a string representing the deck
    def __str__(self):
        result1 = "Deck Contains "
        for i in range(len(self.deck_list)):
            result1 += str(self.deck_list[i]) + " "
        return result1	
    

#define event handlers for buttons
def deal():
    global outcome, in_play, score, message
    global player_hand, dealer_hand, deck_shuffle
    
    player_hand = Hand()
    dealer_hand = Hand()
    deck_shuffle = Deck()  
    #in_play = True
       
    deck_shuffle.shuffle()  
    
    for i in range(2):
        dealer_hand.add_card(deck_shuffle.deal_card())
        player_hand.add_card(deck_shuffle.deal_card())
        
    if in_play == True:
        
        message = "You lose last round.. New game."
        score -= 1
        
               
    else:       
        in_play = True
        message = ""    
        outcome = "Hit or Stand ?"        
      
    #print "Dealer", dealer_hand
    #print "Player", player_hand 
    #c3 = player_hand.get_value()
    #print c3    
    #in_play = True

def hit():
    global outcome, in_play, score, message
    
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    
    if in_play:
      if player_hand.get_value() <=21:
          player_hand.add_card(deck_shuffle.deal_card())
          #print player_hand
          if player_hand.get_value() > 21:
          
             message = "You went bust and lose"
             outcome = "New Deal?"
             in_play = False
             score -= 1  
       
def stand():
    global outcome, in_play, score, message
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    
    if player_hand.get_value() > 21 :       
       message = "You have busted"
       outcome = "New Deal?"
              
    else:
        while (dealer_hand.get_value()) < 17:
            dealer_hand.add_card(deck_shuffle.deal_card())
            #hit()
        if dealer_hand.get_value() > 21:             
             message = "Dealer busted. You win"
             outcome = "New Deal?"
             in_play = False
             score += 1
        else:
            if player_hand.get_value() <= dealer_hand.get_value():               
               message = "You lose. Dealer wins"
               outcome = "New Deal?"
               in_play = False
               score -= 1
            else:                
                message = "You Win"
                outcome = "New Deal?"
                in_play = False
                score += 1
    #outcome = "New Deal?"   

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below    
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    dealer_hand.draw(canvas, [50,150])
    if in_play == True:
        card_location = (CARD_BACK_CENTER[0],CARD_BACK_CENTER[1] )
        canvas.draw_image(card_back, card_location, CARD_BACK_SIZE, [30 + CARD_BACK_CENTER[0], 
                                                            150 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    
    player_hand.draw(canvas, [50,330])
    canvas.draw_text("Blackjack", [100,75], 30, "Aqua", "monospace")
    canvas.draw_text("Score = " + str(score), [350,75], 25, "Black", "monospace")
    canvas.draw_text("Dealer", [30,130], 25, "Black", "monospace")
    canvas.draw_text("Player", [30,310], 25, "Black", "monospace")
    canvas.draw_text(outcome, [200,310], 20, "Black", "monospace")
    canvas.draw_text(message, [200,130], 20, "Black", "monospace")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric