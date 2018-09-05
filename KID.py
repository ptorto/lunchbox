import cPickle

class Kid:

    kidName = ""
    kidAge = ""
    kidFavColor = ""
    parentID = ""

    def __init__(self, kidName):
        self.kidName = kidName

    def setName(self, kidName):
        self.kidName = kidName

    def getName(self):
        return self.kidName

    def setAge(self, kidAge):
        self.kidAge = kidAge

    def getAge(self):
        return self.kidAge

    def setFavColor(self, kidFavColor):
        self.kidFavColor = kidFavColor

    def getFavColor(self):
        return self.kidFavColor

    def saveKid(self):
        filename = 'bin/kid.pkl'
        with open(filename, 'wb') as output:
            cPickle.dump(self, output, cPickle.HIGHEST_PROTOCOL)
