class Employees():
    def __init__(self, employeeID, employeeLastName, employeeFirstName, employeePhoneNumber, position, salary):
        self.employeeID = employeeID
        self.employeeLastName = employeeLastName
        self.employeeFirstName = employeeFirstName
        self.employeePhoneNumber = employeePhoneNumber
        self.position = position
        self.salary = salary

    def getemployeeName(self):
        return self.employeeFirstName + " " + self.employeeLastName

    def setemployeeName(self, employeeFirstName, employeeLastName):
        self.employeeFirstName = employeeFirstName
        self.employeeLastName = employeeLastName

    def updateEmployeePosition(self,employeeID, position):
        self.employeeID = employeeID
        self.position = position


    def __str__(self):
        return str(self.employeeID) + " => " + self.employeeFirstName + " " + self.employeeLastName + "\nPosition: " + self.position