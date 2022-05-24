def idNotInCoinList(toSave, CoinList):
    for id in toSave:
        for coin in CoinList:
            if int(id) == coin['cmc_id']:
                toSave.remove(id)
    return toSave