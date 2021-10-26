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
    self.collision_distance = 32

    #variables
    self.x_spd = 2.2
    self.y_spd = 2.2

  def move_self(self):
    self.goto(self.xcor() +  self.x_spd, self.ycor() +  self.y_spd)

    if self.at_edge_x():
      self.x_spd = -self.x_spd

    if self.at_edge_y():
      self.y_spd = -self.y_spd
      if self.ycor() <0:
        quit()
    if self.check_collision(self.player):
      self.y_spd= - self.y_spd
  

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

  def check_collision(self, obj_to_check):
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < self.collision_distance and distance_y < self.collision_distance:
      return True
    else:
      return False