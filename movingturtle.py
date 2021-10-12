from turtle import Turtle


class MovingTurtle(Turtle):
  def __init__(self, width, height, x,  y, player):
    Turtle.__init__(self)
    self.player = player
    self.width = width
    self.height = height
    self.x = x
    self.y = y

    #initial setup
    self.shape("circle")
    self.shapesize(.5,  .5, 1)
    self.penup()
    

    #variables
    self.x_spd = 4
    self.y_spd = 4

  def move_self(self):
    self.goto(self.xcor() +  self.x_spd, self.ycor() +  self.y_spd)

    if self.at_edge_x():
      self.x_spd = -self.x_spd

    if self.at_edge_y():
      self.y_spd = -self.y_spd

  def at_edge_x(self):
    if self.xcor() >= self.width/2 or self.xcor() <= -self.width/2:
      return True
    else:
      return False

  def at_edge_y(self):
    if self.ycor() >= self.height/2 or self.ycor() <= -self.height/2:
      return True
    else:
      return False

  def at_edge_y(self):
    if self.player.ycor() >= self.height/2 or self.player.ycor() <= -self.height/2:
      return True
    else:
      return False