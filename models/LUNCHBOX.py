class LunchBox:

    ##### BOX INFO #### INFORMACION GENERAL DE LUNCHBOX#####
    boxId = 0
    boxConnected = False
    boxName = ""
    boxStartTime = ""
    boxEndTime = ""
    boxIsNew = True

    ##### INFORMACION DE RED WIFI ####
    boxInternetSSID = ""
    boxInternetPsswd = ""
    boxInternetPaired = False

    
    def __init__(self, boxId, boxName):
        self.boxId = boxId
        self.boxName = boxName
        
    def getConnected(self):
        return self.boxConnected

    def setConnected(self):
        self.boxConnected = True

    def setName(self, boxName):
        self.boxName=boxName

    def getName(self):
        return self.boxName

    def setStartTime(self, boxStartTime):
        self.StartTime = boxStartTime
