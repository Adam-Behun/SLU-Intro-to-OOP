from ChargeCard import ChargeCard

class RewardsChargeCard(ChargeCard):

    def __init__(self, limit, rate, balance=0):
        super().__init_(limit, balance)
        self._rate = rate
        self._rewards = 0

    def charge(self, amount):
        if super(RewardsChargeCard, self).charge(amount):
            self._rewards += amount * self._rate
            return True
        else:
            return False

    def getRewards(self):
        return self._rewards

    def useRewards(self):
        super().deposit(self._rewards)
        self._rewards = 0
        
