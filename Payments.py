class Payments():
    def __init__(self,paymentID, paymentMethod,paymentAmount):
        self.paymentID = paymentID
        self.paymentMethod = paymentMethod
        self.paymentAmount = paymentAmount

    def getPayment(self):
        return self.paymentID


    def __str__(self):
        return "Payment ID :" + self.paymentID + "\n Payment Method :" + self.paymentMethod + "\n Payment Amount :" + self.paymentAmount