"""An implementation of a hierarchy of different ball classes for simulation"""
# Stuart Ray
# Adam Behun
# a world supports methods getWidth() and getHeight() and getBalls()
from world import World

####################################################################

class Ball:
    def __init__(self, r, x, y, vx, vy):
        self._r = r
        self._x = x
        self._y = y
        self._vx = vx
        self._vy = vy

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getRadius(self):
        return self._r

    def getColor(self):
        return 'black'

    def advance(self, world):
        self._x += self._vx
        self._y += self._vy

        try:
            super().advance(world)
            print("HELLO")
        except AttributeError:
            pass

####################################################################

class BouncingBall(Ball):
    def getColor(self):
        return 'skyblue'

    def advance(self, world):
        super().advance(world)
        w = world.getWidth()
        h = world.getHeight()

        if self._x >= w - self._r:                         # right edge of ball contacts right wall
            self._x -= 2 * (self._x - (w - self._r))       # fix the "overshoot"
            self._vx = -self._vx                           # and invert x-velocity
        elif self._x <= self._r:                           # left edge of ball contacts left wall
            self._x += 2 * (self._r - self._x)             # fix the "overshoot"
            self._vx = -self._vx                           # and invert x-velocity

        if self._y >= h - self._r:                         # bottom edge of ball contacts bottom wall
            self._y -= 2 * (self._y - (h - self._r))       # fix the "overshoot"
            self._vy = -self._vy                           # and invert y-velocity
        elif self._y <= self._r:                           # top edge of ball contacts top wall
            self._y += 2 * (self._r - self._y)             # fix the "overshoot"
            self._vy = -self._vy                           # and invert y-velocity

####################################################################

class DampeningBall(Ball):
    def getColor(self):
        return 'orange'
    def advance(self, world):
        super().advance(world)
        w = world.getWidth()
        h = world.getHeight()

        if self._x >= w - self._r:                         # right edge of ball contacts right wall
            self._x -= 2 * (self._x - (w - self._r))       # fix the "overshoot"
            self._vx = (-self._vx * .5)                         # and invert x-velocity and velocity is 50%
        elif self._x <= self._r:                           # left edge of ball contacts left wall
            self._x += 2 * (self._r - self._x)             # fix the "overshoot"
            self._vx = (-self._vx * .5)                           # and invert x-velocity and velocity is 50%

        if self._y >= h - self._r:                         # bottom edge of ball contacts bottom wall
            self._y -= 2 * (self._y - (h - self._r))       # fix the "overshoot"
            self._vy = (-self._vy * .5)                          # and invert y-velocity and velocity is 50%
        elif self._y <= self._r:                           # top edge of ball contacts top wall
            self._y += 2 * (self._r - self._y)             # fix the "overshoot"
            self._vy = (-self._vy * .5)                           # and invert y-velocity and velocity is 50%


class WrappingBall(Ball):
    def getColor(self):
        return 'lightgreen'
    def advance(self, world):
        super().advance(world)
        w = world.getWidth()
        h = world.getHeight()

        if self._x >= w - self._r:                         # right edge of ball contacts right wall
            self._x -= w                                    # wraps
        elif self._x <= self._r:                           # left edge of ball contacts left wall
            self._x += w                                    # wraps
        if self._y >= h - self._r:                         # bottom edge of ball contacts bottom wall
            self._y -= h                                     # wrap
        elif self._y <= self._r:                           # top edge of ball contacts top wall
            self._y += h                                     # wrap


####################################################################

class ExplosiveBall(Ball):
    def getColor(self):
        return 'red'
    x = Ball.getX()
    y = Ball.getY()
    ballList = World.getBalls()
    if x and y in ballList:
        pass


####################################################################

#class ExplosiveWrappingBall(ExplosiveBall, WrappingBall):
#    def getColor(self):
#        return 'darkgreen'

####################################################################

#class ExplosiveBouncingBall(ExplosiveBall, BouncingBall):
#    def getColor(self):
#        return 'blue'

####################################################################
