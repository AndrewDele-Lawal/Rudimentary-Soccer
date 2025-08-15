import random
import time

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

  # Handles invalid inputs
  while kick != "Straight" and kick != "Left" and kick != "Right":
    print("Input the right thing dummy")
    time.sleep(2)
    kick = str(input("Alright lets do this again lil bro.\nEnter 'Straight', 'Left', or 'Right' Otherwise your ##### won't be able to play the game:\n"))
    time.sleep(2)

  # Generates a new direction every time the code loops
  Directional_Key = random.SystemRandom().randint(0, len(Direction) - 1)

  print("Goalie is gearing up to block")
  time.sleep(2)

  # Score logic
  if kick == Direction[Directional_Key]:
    print("The Goalie jumped", Direction[Directional_Key], "blocking the ball")
  else:
    print("The Goalie jumped", Direction[Directional_Key], "allowing your shot to hit ", kick)
    Player.addTally()
    time.sleep(1)
    print("Current score is",Player.gettally(),"\n")
  print("GAME OVER, you got", pointsGoal)


