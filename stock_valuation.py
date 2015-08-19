class stockBlock(object):
    '''A block of stock.'''

    def __init__(self, purch_date, purch_price, shares):
        self.purch_date = purch_date
        self.purch_price = purch_price
        self.shares = shares

    def __str__(self):
        return "Date of purchase: %s; Price of shares: %s; Number of shares: %s" % (self.purch_date, self.purch_price, self.shares)

    def getPurchaseValue(self):
        return self.purch_price * self.shares

    def getSaleValue(self, salePrice):
        return salePrice * self.shares

    def getROI(self, salePrice):
        return (self.getSaleValue(salePrice) - self.getPurchaseValue()) / float(self.getPurchaseValue())



class position(object):
    """docstring for position"""
    def __init__(self, name, symbol, * blocks):
        self.name = name
        self.symbol = symbol
        self.blocks =  blocks

    #def __str__(self):
    #    return "%s, %s" % (self.symbol,  )


    #def sumShares(self):
    #    sum = 0
    #    for b in self.blocks:
    #        sum += b.shares



blocksGM = [
    stockBlock( purch_date='25-Jan-2001', purch_price=44.89, shares=17 ),
    stockBlock( purch_date='25-Apr-2001', purch_price=46.12, shares=17 ),
    stockBlock( purch_date='25-Jul-2001', purch_price=52.79, shares=15 ),
    stockBlock( purch_date='25-Oct-2001', purch_price=37.73, shares=21 )
]
blocksEK = [
    stockBlock( purch_date='25-Jan-2001', purch_price=35.86, shares=22 ),
    stockBlock( purch_date='25-Apr-2001', purch_price=37.66, shares=21 ),
    stockBlock( purch_date='25-Jul-2001', purch_price=38.57, shares=20 ),
    stockBlock( purch_date='25-Oct-2001', purch_price=27.61, shares=28 )
]


a = position("GenM", "GM", blocksGM)
print a.blocks
