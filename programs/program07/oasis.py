from world import World

class Oasis(World):
  eggs_set = [] # pairs of egg locations (x,y)
  score = 0 # keeping the score of a player

  def addEgg(self, row, column): # adding eggs to specific positions on the board
    if (row, column) not in self.eggs_set: # only allow adding an egg not in the set
      if row >= 0 and column >= 0:  # only positive inputs because we need to keep them on the board
        if World.numRows(self) > row and World.numColumns(self) > column: # the World (board) has to be bigger than the inputs so that the eggs are on the board
          if (row, column) != (0,0): # we do not allow the egg on (0,0) because that is the initial position of the player
            self.eggs_set.append((row, column))

  def eggLocations(self):
    return self.eggs_set # getting the positions of the eggs

  def getScore(self): #
    if World.playerLocation(self) in self.eggs_set:
      self.eggs_set.remove(World.playerLocation(self)) # removing the egg that was hit
      self.score += 1 # increasing the score of a player if he/she hits the egg
      return self.score