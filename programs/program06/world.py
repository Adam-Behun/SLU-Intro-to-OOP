# Adam Behun -> Program 06: Ready Player One

class World:

    def __init__(self,rows=0,columns=0):

        if rows < 1 or columns < 1:                     # only positive inputs for rows and columns
            raise ValueError('Rows and columns must be positive integers.')
        if not isinstance(rows, int):                   # rows must be an integer
            raise TypeError('Rows must be an integer.')
        if not isinstance(columns, int):                # columns must be an integer
            raise TypeError('Columns must be an integer.')

        self._y = rows
        self._x = columns

# Getting a position of the player

    def playerLocation(self):
        self._position = (self._y, self._x)
        return self._position

# Defining number of rows and columns of the table

    def numRows(self):
        return self._y

    def numColumns(self):
        return self._x

# Moving to a specific (row, column) pair in the table

    def moveTo(self, newRow, newColumn):
        if newRow >= 0 and newColumn >= 0:     # only positive inputs for newRow and newColumn
            self._y = newRow
            self._x = newColumn
            return True
        else:
            return False

# Moving one step at a time within the table

    def moveUp(self):
        self._y += 1
        return True

    def moveDown(self):
        if (self._y -1) < 0:      # checking validity of the input
            return False
        else:
            self._y -= 1
            return True

    def moveRight(self):
        self._x += 1
        return True

    def moveLeft(self):
        if (self._x -1) < 0:      # checking validity of the input
            return False
        else:
            self._x -= 1
            return True