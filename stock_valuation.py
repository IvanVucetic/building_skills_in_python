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
    
    def __init__(self, name, symbol, blocks):
        self.name = name
        self.symbol = symbol
        self.blocks = blocks
        self.sum_shares = self.sumShares(self.blocks)
        self.sum_purch_price = self.sumPurchPrice()
        # TODO
        self.current_price = self.setCurrentPrice() 
           
    
    def __str__(self):
        return "%s, total shares: %s, total purchase price: %s" % (self.symbol, self.sum_shares, self.sum_purch_price )

    def sumShares(self, blocks):
        sum = 0
        if type(blocks) is list:    # might be a single block or a list of
            for block in blocks:
                sum += block.shares
        else:
            sum = blocks.shares
        return sum

    def sumPurchPrice(self):
        sum = 0
        if type(self.blocks) is list:
            for block in self.blocks:
                sum += block.purch_price
        else:
            sum = self.blocks.purch_price
        return sum

    def getPurchValue(self):
        sum = 0
        if type(self.blocks) is list:
            for block in self.blocks:
                sum += block.getPurchaseValue()
        else:
            sum = self.blocks.getPurchaseValue()
        return sum

    def getSaleValue(self, sale_price):
        sum = 0
        if type(self.blocks) is list:
            for block in self.blocks:
                sum += block.getSaleValue(sale_price)
        else:
            sum = self.blocks.getSaleValue(sale_price)
        return sum

    def getROI(self, sale_price):
        return self.getSaleValue(sale_price) - self.getPurchValue()

    # TODO
    def setCurrentPrice(self):
        print "Enter current price: "
        return raw_input('> ')

    # TODO
    def getCurrentValue(self, current_price):
        sum_current_value = 0
        for block in self:
            sum_current_value += block.getSaleValue(self.current_price)
        print sum_current_value



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

portfolio = [
    position("General Motors", "GM", blocksGM),
    position("Eastman Kodak", "EK", blocksEK),
    position("Caterpillar", "CAT",
        [ stockBlock(purch_date='25-Oct-2001',
            purch_price=42.84, shares=18) ])
]



def report1(portf):
    '''Purchase values of individual Blocks in Positions.'''

    for posit in portf:
        for block in posit.blocks:
            print posit.symbol, block.getPurchaseValue()

def report2(portf):
    '''Summarize each position with symbol, total number of shares,
    total value of the stock purchased and average price paid.'''

    for posit in portf:
        shares = 0
        tot_val = 0
        for block in posit.blocks:
            shares += block.shares
            tot_val += block.getPurchaseValue()

        print "Position: %s, shares: %s, value: %s, average: %s." % (posit.symbol, shares, tot_val, (tot_val / shares))




report1(portfolio)
report2(portfolio)









