from Items import Items
class Taxes(Items):
    def __init__(self, itemID, taxID, taxAmount):
        Items.__init__(self, itemID, taxID, taxAmount)
        self.taxID = taxID
        self.taxAmount = taxAmount


    def getTax(self):
        return self.taxAmount


    def __str__(self):
        return "Item ID : " +  str(self.itemID) + "\n Tax Amount : $" +  str(self.taxAmount)