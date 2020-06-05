class Items():
    def __init__(self, itemID, itemName, itemPrice):
        self.itemID = itemID
        self.itemName = itemName
        self.itemPrice = itemPrice

    def getItemName(self):
        return self.itemName

    def getItemPrice(self):
        return self.itemPrice

    def addNewItem(self, itemID, itemName, itemPrice):
        self.itemID = itemID
        self.itemName = itemName
        self.itemPrice = itemPrice


    def __str__(self):
        return "Item ID : " + str(self.itemID) + "\n Item Name : " + str(self.itemName) + "\n Item Price : $" + str(self.itemPrice)