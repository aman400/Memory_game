# implementation of card game - Memory
# Author :  Amanadeep 

import simplegui
import random

# helper function to initialize globals
def new_game():
    global list_nums, turn, card_list, turns, exposed
    exposed = []       #stores the exposed set of cards in last two moves
    turn = 0		   
    turns = 0		   #stores total number of turns that are to be displayed
    label.set_text("Turns = "+str(turns))
    
    #generate random list of elements
    list_nums = [[i%8+1, False] for i in range(16)]
    
    #radomly shuffle list of numbers
    random.shuffle(list_nums)
    
# define event handlers
def mouseclick(pos):
    global turns, turn, exposed
    for card in range(16):
        if pos[0] > (card*50) and pos[0] < (card*50+48) and not (list_nums[card][1]):
            list_nums[card][1] = True
            
            # Keep track of the current state of game
            if turn == 0:
                turn = 1
                exposed.append(card)
            elif turn == 1:
                exposed.append(card)
                turn = 2
                turns += 1
                label.set_text("Turns = "+str(turns))
            else:
                if not (list_nums[exposed[0]] == list_nums[exposed[1]]):
                    list_nums[exposed[0]][1] = False
                    list_nums[exposed[1]][1] = False
                exposed = []
                exposed.append(card)
                turn = 1
                    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card in range(16):
        #Draw cards that are visible
        if list_nums[card][1]:
            canvas.draw_text(str(list_nums[card][0]),[card + 50*card + 10, 70], 45, "white")
        #Draw cards that are not visible
        else:
            canvas.draw_polygon([[card*50+25, 0], [card*50+25, 100]], 48, "green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
