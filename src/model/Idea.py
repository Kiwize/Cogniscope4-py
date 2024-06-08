

class Idea:

    def __init__(self, num, text = None, classNo = None, votes = None, stat = None, clarification = ""):
        self.num = num
        self.text = text
        self.classNo = classNo
        self.votes = votes
        self.stat = stat
        self.clarification = clarification

    def isComplete(self) -> bool :
        if not self.text is None and not self.classNo is None and not self.votes is None and not self.stat is None:
            return True
        
        return False

    def getNum(self):
        return self.num
    
    def getText(self):
        return self.text
    
    def getClassNo(self):
        return self.classNo
    
    def getVotes(self):
        return self.votes
    
    def getStat(self):
        return self.stat
    
    def getClarification(self):
        return self.clarification
    
    def setText(self, text):
        self.text = text

    def setClusterNum(self, num):
        self.classNo = num

    def setVotes(self, votes):
        self.votes = votes

    def setStat(self, stat):
        self.stat = stat

    def setClarification(self, clarification):
        self.clarification = clarification