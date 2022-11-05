class Radio:
    def init(self):                           #should be __init__ otherwise the variables would not be accessed
        self._powerOn = False
        self._volume = 5
        self._station = 90.7
        self._presets = [ 90.7, 92.3, 94.7, 98.1, 105.7, 107.7 ]

    def togglePower(self):
        self._powerOn = not self._powerOn

    def setPreset(self, ind):
        self._presets[ind] = _station    #replace _station with self._station as it can be used for the whole class (we initialized it that way)

    def gotoPreset(self, ind):
        self._station = self._presets[self._ind]    #self._ind should only be ind - it is only a local variable for that one function

  def increaseVolume(self):
      self._volume = self._volume + 1          #indentation is not correct here - should be like the ones before (4 from class and 4 from def)

    def decreaseVolume(self):
        self._volume = self._volume - 1

    def increaseStation(self)                       # we are missing a semicollon here
        self._station = self._station + .2

    def decreaseStation(self):
      self._station = self._station - .2
