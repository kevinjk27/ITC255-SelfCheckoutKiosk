import unittest
from Items import Items
from Taxes import Taxes
from Discounts import Discounts
from Customers import Customers
from Employees import Employees
from Transactions import Transactions
from Payments import Payments
from Kiosks import Kiosks


# Testing Items.py
class TestItems(unittest.TestCase):
    def setUp(self):
        self.items = Items(209321299, "Sour Patch Watermelon Soft & Chewy Candy - 8oz", 1.99)

    def test_ItemString(self):
        self.assertEquals(str(self.items), "Item ID : 209321299\n Item Name : Sour Patch Watermelon Soft & Chewy Candy - 8oz\n Item Price : $1.99")

    def test_GetItemName(self):
        self.assertEqual(self.items.getItemName(), 'Sour Patch Watermelon Soft & Chewy Candy - 8oz')

    def test_AddNewItem(self):
        self.items.addNewItem(209321300, "Chips Ahoy! Original Chocolate Chip Cookies -13oz", 2.59)
        self.assertEqual(self.items.getItemName(), "Chips Ahoy! Original Chocolate Chip Cookies -13oz")

    def test_GetItemPrice(self):
        self.assertEqual(self.items.getItemPrice(), 1.99)


# Testing Taxes.py
class TestTaxes(unittest.TestCase):
    def setUp(self):
        self.taxes = Taxes(209321299, 723608101, 0.00)

    def test_TaxString(self):
        self.assertEquals(str(self.taxes), "Item ID : 209321299\n Tax Amount : $0.0")

    def test_GetTax(self):
        self.assertEquals(self.taxes.getTax(), 0.000)


# Testing Discounts.py
class TestDiscounts(unittest.TestCase):
    def setUp(self):
        self.discounts = Discounts(209321299, 32601, 1.00)

    def test_DiscountString(self):
        self.assertEquals(str(self.discounts), "Discount ID : 32601\n Discount Amount : $1.0")

    def test_GetTax(self):
        self.assertEquals(self.discounts.getDiscount(), 1.00)


# Testing Customers.py
class TestCustomers(unittest.TestCase):
    def setUp(self):
        self.customers = Customers(400901, "Sukamanja", "Raisa", "206-930-5021", "12")

    def test_GetCustomerName(self):
        self.assertEquals(self.customers.getCustomerName(), "Raisa Sukamanja")


    def test_SetCustomerName(self):
        self.customers.setCustomerName("Bagas", "Sucipto")
        self.assertEqual(self.customers.getCustomerName(), "Bagas Sucipto")

    def test_CustomerString(self):
        self.assertEquals(str(self.customers), "Raisa Sukamanja,\nYou have : 12 reward points")



# Testing Employees.py
class TestEmployees(unittest.TestCase):
    def setUp(self):
        self.employees = Employees(775501, "Mangosteen", "Mickey", "206-601-7812", "Cashier", "$15.63")

    def test_GetEmployeeName(self):
        self.assertEquals(self.employees.getemployeeName(), "Mickey Mangosteen")

    def test_EmployeeString(self):
        self.assertEquals(str(self.employees), "775501 => Mickey Mangosteen\nPosition: Cashier")

    def test_UpdateEmployeePosition(self):
        self.employees.updateEmployeePosition(775501, "Manager")
        self.assertEqual(str(self.employees), "775501 => Mickey Mangosteen\nPosition: Manager")


# Testing Transactions.py
class TestTransactions(unittest.TestCase):
    def setUp(self):
        self.transactions = Transactions(321001, "2020-06-04", "20:33:51", ['Gala Apple', 'Sour Patch Watermelon Soft & Chewy Candy - 8oz','Organic Green Bell Pepper'], 400901, 5.97, 0.05, "K0091", 0.00, 5.92)

    def test_AddItem(self):
        self.assertEquals(self.transactions.addItem("Gala Apple"),['Gala Apple'])
        self.assertEquals(self.transactions.addItem('Sour Patch Watermelon Soft & Chewy Candy - 8oz'),['Gala Apple', 'Sour Patch Watermelon Soft & Chewy Candy - 8oz'])
        self.assertEquals(self.transactions.addItem('Organic Green Bell Pepper'),['Gala Apple', 'Sour Patch Watermelon Soft & Chewy Candy - 8oz','Organic Green Bell Pepper'])

    def test_EmployeeString(self):
        self.assertEquals(str(self.transactions), "Transaction #321001 item bought: 3 Thank You!")

    



# Testing Payments.py
class TestPayment(unittest.TestCase):
    def setUp(self):
        self.payments = Payments(55001, "visa card", 6.39)

    def test_PaymentString(self):
        self.assertEquals(str(self.payments),"Payment ID :55001\n Payment Method :visa card\n Payment Amount :$6.39")



# Testing Kiosks.py
class TestKiosks(unittest.TestCase):
    def setUp(self):
        self.kiosks = Kiosks("K0091", "active")

    def test_PaymentString(self):
        self.assertEquals(str(self.kiosks),"Kiosk #K0091 is active!")
