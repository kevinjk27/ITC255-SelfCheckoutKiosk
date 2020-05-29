class Kiosks():
    def __init__(self, kioskID, kioskStatus):
        self.kioskID = kioskID
        self.kioskStatus = kioskStatus

    def getStatus(self):
        return self.kioskStatus


    def __str__(self):
        return "Kiosk #" + self.kioskID + " is " + self.kioskStatus