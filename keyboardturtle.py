from turtle import Turtle

class KeyboardTurtle(Turtle):
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               window,
               turn_right = "Right",
               turn_left = "Left",
               other_player = None):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.window = window
    self.turn_right = turn_right
    self.turn_left = turn_left
    self.other_player = other_player

    #set turtle starting states
    self.shape("square")
    self.shapesize(1, 4)
    self.color("green")
    self.penup()

    # Sets up keyboard command examples
    self.window.onkey(self.go_right, self.turn_right)
    self.window.onkey(self.go_left, self.turn_left)

    #sets up controlling variables (y not implemented)
    self.movement_speed = 20
    self.turn_speed = 45
    self.collision_distance = 20

  # Movement Methods
  def go_right(self):
    self.forward(self.movement_speed)

  def go_left(self):
    self.backward(self.movement_speed)


  # Useful Methods

  # This checks if object collides with another object.  
  # Right now it checks against the other player, but 
  # it doesn't NEED to.  It can check against any
  # other turtle object

  def check_collision(self, obj_to_check):
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < self.collision_distance and distance_y < self.collision_distance:
      return True
    else:
      return False


    # TODO: finish setting up the inputs (left and down)
    