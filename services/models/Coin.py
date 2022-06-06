
import random


class Coins:
 
    def __init__(self, cmc_id, symbol, name, logo, active):
        self.cmc_id = cmc_id
        self.symbol = symbol
        self.name = name
        self.logo = logo
        self.active = active
        coin_rank = random.randint(0, 1000)
