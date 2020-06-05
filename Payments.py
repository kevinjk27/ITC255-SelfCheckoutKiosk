class Payments():
    def __init__(self,paymentID, paymentMethod,paymentAmount):
        self.paymentID = paymentID
        self.paymentMethod = paymentMethod
        self.paymentAmount = paymentAmount

    def getPayment(self):
        return self.paymentID


    def __str__(self):
        return "Payment ID :" + str(self.paymentID) + "\n Payment Method :" + str(self.paymentMethod) + "\n Payment Amount :$" + str(self.paymentAmount)