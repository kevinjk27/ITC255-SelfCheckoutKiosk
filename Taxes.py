from Items import Items
class Taxes(Items):
    def __init__(self, itemID, taxID, taxAmount):
        Items.__init__(self,itemID)
        self.taxID = taxID
        self.taxAmount = taxAmount


    def getTax(self):
        return self.taxAmount


    def __str__(self):
        return "Item ID :" + self.itemID + "\n Tax Amount :" + self.taxAmount