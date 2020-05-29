import datetime
from Customers import Customers
from Employees import Employees
from Items import Items
from Discounts import Discounts
from Kiosks import Kiosks
from Payments import Payments
from Taxes import Taxes


class Transactions():
    def __init__(self, transactionID, item, customer, payment, discount, register, tax, total):
        self.transactionID = transactionID
        self.transactionDate = datetime.date.today()
        self.transactionTime = datetime.time.strftime()
        self.item = []
        self.customer = customer
        self.payment = payment
        self.discount = discount
        self.register = register
        self.tax = tax
        self.total = total

    def getTransactionID(self):
        return self.transactionID

    def getItem(self):
        return self.item

    def getCustomer(self):
        return self.customer

    def getPayment(self):
        return self.payment

    def getDiscount(self):
        return self.discount

    def getRegister(self):
        return self.register

    def getTax(self):
        return self.tax

    def getTotal(self):
        total=0
        for i in self.item:
            total += i.price
        return total

    def addItem(self, item):
        self.item.append(item)

    def addCustomer(self, customer):
        self.customer = customer

    def addDiscount(self, discount):
        self.discount = discount

    def __str__(self):
        return self.transactionID + " item bought: " + len(self.item) + " Thank You!"
