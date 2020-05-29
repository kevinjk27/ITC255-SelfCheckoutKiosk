class Items():
    def __init__(self, itemID, itemName, itemPrice):
        self.itemID = itemID
        self.itemName = itemName
        self.itemPrice = itemPrice

    def getItemName(self):
        return self.itemName

    def addNewItem(self, itemID, itemName, itemPrice):
        self.itemID = itemID
        self.itemName = itemName
        self.itemPrice = itemPrice


    def __str__(self):
        return "Item ID :" + self.itemID + "\n Item Name :" + self.itemName + "\n Item Price :" + self.itemPrice