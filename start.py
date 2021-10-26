from turtle import Screen
from clickableturtle import ClickableTurtle

# set up instance of the screen
window = Screen()
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

start_button = ClickableTurtle(name = "start")


window.listen()
window.mainloop()
