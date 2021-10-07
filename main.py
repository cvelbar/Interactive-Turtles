from turtle import Screen
from keyboardturtle import KeyboardTurtle
from clickableturtle import ClickableTurtle
from movingturtle import MovingTurtle

# set up instance of the screen
window = Screen()
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)


#set up players
player_1 = KeyboardTurtle(window)

player_1.goto(0,-180)

# set target of other player(our collison check) to the opposite player

#player_1.other_player = player_2
#player_2.other_player = player_1

ball = MovingTurtle(screen_width)

# This is needed to listen for inputs
window.listen()
window.mainloop()


# be CAREFUL. We aren't controlling the screen draws in this program, so NO while True loops

#TODO:  Check the classes and complete TODOs
#push to github repo.
#link repo to assignment