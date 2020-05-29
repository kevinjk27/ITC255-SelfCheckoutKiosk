from Items import Items
class Discounts(Items):
    def __init__(self, itemID, discountID, discountAmount):
        Items.__init__(self, itemID)
        self.discountID = discountID
        self.discountAmount = discountAmount


    def getDiscount(self):
        return self.discountAmount


    def __str__(self):
        return "Discount ID :" + self.discountID + "\n Tax Amount :" + self.discountAmount