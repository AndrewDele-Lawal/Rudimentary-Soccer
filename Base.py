import random

# Super Limited Soccer

class playerActions:
  # Keeps track of Player's goals scored
    def __init__(self):
        self.tally = 0

    def gettally(self):
       return self.tally

  # Adds a point to the player's tally
    def addTally(self):
       self.tally += 1



Player = playerActions()

Direction = ["Left", "Straight", "Right"]

pointsGoal = int(input("Enter the number of points you wish to play to:\n"))

while (Player.gettally() < pointsGoal) :
  # User input for which direction they want to kick the ball
  kick = str(input("Do you wish to kick the ball: 'Straight', 'Left', or to the 'Right'\n"))

  # Generates a new direction every time the code loops
  Directional_Key = random.SystemRandom().randint(0, len(Direction) - 1)

  if kick == Direction[Directional_Key]:
    print("The Goally jumped", Direction[Directional_Key], "blocking the ball")
  else:
    print("The Goally jumped", Direction[Directional_Key], "allowing your shot to hit ", kick)
    Player.addTally()
