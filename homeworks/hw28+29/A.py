def index(self, value, start=0):
    if self._isEmpty():
        raise ValueError('OurList.index(x): x not in list')
    elif self._head == value:
        return 0
    else:
        return 1 + self._value.index(start)