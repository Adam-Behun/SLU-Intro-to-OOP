# Adam Behun -> hw25b

from account import Account

account_1 = Account(100.0)
account_2 = Account(250.0)

myAssets = [account_1, account_2]
spouseAssets = [account_1, account_2]

account_3 = Account(500.0)

spouseAssets.append(account_3)

spouseRetirement = account_3