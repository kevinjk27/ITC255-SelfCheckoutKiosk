class Customers():
    def __init__(self, customerID, customerLastName, customerFirstName, customerPhoneNumber, customerRewardsPoint):
        self.customerID = customerID
        self.customerLastName = customerLastName
        self.customerFirstName = customerFirstName
        self.customerPhoneNumber = customerPhoneNumber
        self.customerRewardsPoint = customerRewardsPoint

    def getCustomerName(self):
        return self.customerFirstName + " " + self.customerLastName

    def setCustomerName(self, customerFirstName, customerLastName):
        self.customerFirstName = customerFirstName
        self.customerLastName = customerLastName

    def inputRewardsPoint(self, customerID, customerRewardsPoint):
        self.customerID = customerID
        self.customerRewardsPoint = customerRewardsPoint

    def __str__(self):
        return self.customerFirstName + " " + self.customerLastName + ",\n" + "You have : " + str(self.customerRewardsPoint) + " reward points"
